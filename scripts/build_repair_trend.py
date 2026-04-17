#!/usr/bin/env python3
import json
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
RUNS = [
    ('Baseline', ROOT / 'data/runs/sample-run/summary.json'),
    ('T+7', ROOT / 'data/runs/repair-t7-run/summary.json'),
    ('T+14', ROOT / 'data/runs/repair-t14-run/summary.json'),
]
METRICS = ['mention_rate', 'positive_mention_rate', 'capability_accuracy', 'ecosystem_accuracy']
LABELS = {
    'mention_rate': 'Mention',
    'positive_mention_rate': 'Positive',
    'capability_accuracy': 'Capability',
    'ecosystem_accuracy': 'Ecosystem',
}

def main():
    names = []
    series = {m: [] for m in METRICS}
    for name, path in RUNS:
        data = json.loads(path.read_text(encoding='utf-8'))
        names.append(name)
        for metric in METRICS:
            series[metric].append(data['metrics'][metric])
    plt.figure(figsize=(8, 4.8))
    colors = ['#2563eb', '#16a34a', '#f59e0b', '#7c3aed']
    for metric, color in zip(METRICS, colors):
        plt.plot(names, series[metric], marker='o', linewidth=2.2, label=LABELS[metric], color=color)
    plt.ylim(0, 100)
    plt.ylabel('Score')
    plt.title('Repair Loop Trend (Baseline vs T+7 vs T+14)')
    plt.grid(axis='y', linestyle='--', alpha=0.25)
    plt.legend(ncols=2)
    plt.tight_layout()
    out = ROOT / 'assets/repair-trend-sample.png'
    out.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out, dpi=160)
    print(out)

if __name__ == '__main__':
    main()
