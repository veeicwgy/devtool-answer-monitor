#!/usr/bin/env python3
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt

METRICS = ["mention_rate", "positive_mention_rate", "capability_accuracy", "ecosystem_accuracy"]


def load_summary(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def collect_rows(root):
    rows = []
    for path in sorted(Path(root).glob("*/summary.json")):
        summary = load_summary(path)
        for model_row in summary.get("by_model", []):
            rows.append({"run_id": summary["run_id"], "project": summary["project"], **model_row})
    return rows


def write_csv(rows, path):
    fields = ["run_id", "project", "model_id", *METRICS]
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k) for k in fields})


def aggregate(rows):
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["model_id"]].append(row)
    output = []
    for model_id, items in grouped.items():
        latest = items[-1]
        prev = items[-2] if len(items) > 1 else None
        agg = {"model_id": model_id, "run_count": len(items)}
        for metric in METRICS:
            values = [r[metric] for r in items if r.get(metric) is not None]
            agg[f"avg_{metric}"] = round(sum(values) / len(values), 2) if values else None
            agg[f"latest_{metric}"] = latest.get(metric)
            agg[f"delta_{metric}"] = round(latest.get(metric, 0) - prev.get(metric, 0), 2) if prev and prev.get(metric) is not None else None
        output.append(agg)
    return sorted(output, key=lambda x: (x.get("latest_mention_rate") or 0), reverse=True)


def write_md(rows, path):
    lines = [
        "# Model Leaderboard",
        "",
        "| Model | Runs | Latest Mention | Latest Positive | Latest Capability | Latest Ecosystem | Δ Mention |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        delta = "NA" if row["delta_mention_rate"] is None else f"{row['delta_mention_rate']:+.2f}"
        lines.append(
            f"| {row['model_id']} | {row['run_count']} | {row['latest_mention_rate']:.2f} | {row['latest_positive_mention_rate']:.2f} | {row['latest_capability_accuracy']:.2f} | {row['latest_ecosystem_accuracy']:.2f} | {delta} |"
        )
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_png(rows, path):
    labels = [row["model_id"] for row in rows]
    values = [row["latest_mention_rate"] for row in rows]
    plt.figure(figsize=(8, 4.5))
    plt.bar(labels, values, color="#2563eb")
    plt.ylabel("Mention Rate")
    plt.title("Model Leaderboard Snapshot")
    plt.ylim(0, 100)
    for i, value in enumerate(values):
        plt.text(i, value + 1, f"{value:.0f}", ha="center", fontsize=9)
    plt.tight_layout()
    plt.savefig(path, dpi=160)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-root", default="data/runs")
    ap.add_argument("--output-dir", default="data/leaderboards")
    ap.add_argument("--image-output", default="assets/leaderboard-sample.png")
    args = ap.parse_args()

    rows = collect_rows(args.runs_root)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    Path(args.image_output).parent.mkdir(parents=True, exist_ok=True)
    write_csv(rows, output_dir / "model_leaderboard.csv")
    aggregated = aggregate(rows)
    write_md(aggregated, output_dir / "model_leaderboard.md")
    write_png(aggregated, args.image_output)
    print(json.dumps({"rows": len(rows), "models": len(aggregated), "output_dir": str(output_dir), "image": args.image_output}, ensure_ascii=False))


if __name__ == "__main__":
    main()
