![GEO Monitor Toolkit](assets/logo.png)

# GEO Monitor Toolkit

> Monitor how ChatGPT, Claude, Gemini, and other LLMs describe your developer tool, API, SDK, or open-source project.

[![CI](https://github.com/veeicwgy/geo-monitor-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/veeicwgy/geo-monitor-toolkit/actions/workflows/ci.yml)
![Release](https://img.shields.io/github/v/release/veeicwgy/geo-monitor-toolkit)
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/github/license/veeicwgy/geo-monitor-toolkit)

Prefer agent workflow? Install the [ClawHub skill](https://clawhub.ai/veeicwgy/geo-monitor-os-skill).

**GEO Monitor Toolkit** is a **GEO Monitoring OS for developer tools, APIs, SDKs, and open-source projects**.
It is not a generic content generator. It is a reproducible workflow that connects **Query Pool design, answer monitoring, four-metric scoring, repair loops, activation analysis, and T+7/T+14 regression checks**.

It pairs:

- the **`geo-monitor-toolkit` repo** for runnable demos, artifacts, and reporting scripts
- the **GEO Monitor Toolkit skill on ClawHub** for agent-guided monitoring, query-pool design, and repair workflows

For 中文说明, see [`README.zh-CN.md`](README.zh-CN.md).

## Why this repository exists

If your team is already asking whether LLMs mention your product, describe it correctly, recommend it positively, or improve after documentation fixes, this repository turns that concern into an executable and reviewable workflow.

| What you need to answer | What this repository gives you |
|---|---|
| Do models mention our product at all? | Query Pool + raw responses |
| When they mention us, is it accurate and positive? | Four-metric scoring framework |
| Where should we repair the source of truth? | Placement and repair lens |
| Are we improving installs, API calls, or agent adoption? | Activation metrics + funnel-stage slices |
| Did our fixes actually improve model answers? | T+7 / T+14 regression checks |

## Try the Skill

If you want the agent workflow instead of starting with the CLI, install the companion skill on ClawHub and start with one of these prompts:

- `Analyze how ChatGPT and Claude describe my API docs`
- `Build a GEO query pool for my SDK`
- `Find negative or outdated LLM claims about my project`

The ClawHub skill is the companion agent layer for this repository:

- Skill page: [geo-monitor-os-skill on ClawHub](https://clawhub.ai/veeicwgy/geo-monitor-os-skill)
- Repo quick demo: [30-second path](#30-second-path)

## 30-second path

For a first run, follow this exact order.

```bash
git clone https://github.com/veeicwgy/geo-monitor-toolkit.git
cd geo-monitor-toolkit
bash install.sh
make doctor
bash quickstart.sh
```

## What you will get first

After the first run, start with these outputs.

| Output | Path | Why it matters |
|---|---|---|
| Raw responses | `data/runs/quickstart-run/raw_responses.jsonl` | Review multi-model answer evidence |
| Score draft | `data/runs/quickstart-run/score_draft.jsonl` | Start manual review and annotation |
| Weekly report snapshot | `data/runs/sample-run/weekly_report.md` | See the report format a team can consume |
| Sciverse sample summary | `data/runs/sciverse-sample-run/summary.json` | See a scientific API sample with funnel-stage slices |
| Sciverse sample weekly report | `data/runs/sciverse-sample-run/weekly_report.md` | See a complete second sample for API and agent scenarios |
| Leaderboard snapshot | `assets/leaderboard-sample.png` | Understand the default multi-model comparison |
| Repair trend snapshot | `assets/repair-trend-sample.png` | See how follow-up runs can be visualized over time |

> `quickstart.sh` creates a fresh `quickstart-run` with raw evidence, then replays built-in sample summaries to generate report and chart snapshots. Your first run therefore shows both what a new run looks like and what a mature output package looks like.

## Beginner-first docs

If you are new to GEO monitoring, start with these entry points.

| Document | Purpose |
|---|---|
| `docs/for-beginners.md` | 5-minute path: run it once and read the outputs |
| `docs/getting-started.md` | Long-form onboarding with modes, outputs, and team usage |
| `docs/activation-metrics.md` | Extend GEO from awareness into install, API, and agent adoption |

## Choose your first GEO goal

If you are not sure where to start, pick the path that matches the business outcome you care about most.

| Goal | Start here | Why |
|---|---|---|
| Improve mention and recommendation quality | `data/query-pools/mineru-example.json` + `docs/metric-definition.md` | Baseline the 4 core GEO metrics first |
| Improve downloads and installs | `docs/activation-metrics.md` + `playbooks/developer-tool-surface-priority.md` | Add actionability and source-surface prioritization |
| Improve API calls and agent invocations | `playbooks/agent-readiness.md` + `data/query-pools/sciverse-api-integration-example.json` | Focus on integration and agent-selection queries |
| Improve GEO for scientific products | `playbooks/scientific-product-geo.md` | Use a product model tuned for MinerU, Sciverse API, and research workflows |

## Which mode should you choose

| Your situation | Recommended mode | Entry point |
|---|---|---|
| No API key yet and you only want to see the full workflow | Quickstart replay | `bash quickstart.sh` |
| You already copied answers from external chat products and want to score them | Manual paste mode | `python -m geo_monitor run --manual-responses ...` |
| You want real, repeatable, multi-model GEO monitoring | API collection mode | `python -m geo_monitor run --query-pool ... --model-config ...` |

## Core commands

| Command | What it does |
|---|---|
| `bash install.sh` | Creates `.venv` and installs dependencies |
| `make doctor` | Checks Python, dependencies, sample files, and output directories |
| `bash quickstart.sh` | Runs the zero-API-cost beginner demo |
| `make sample-report` | Rebuilds the MinerU sample report and chart assets |
| `make sample-report-sciverse` | Rebuilds the Sciverse API sample summary and weekly report |
| `make sample-reports` | Rebuilds both default sample report packages |
| `python -m geo_monitor run ...` | Runs custom Query Pool monitoring |

## Default sample inputs

| File | Purpose |
|---|---|
| `data/query-pools/mineru-example.json` | Default Query Pool sample for developer tools |
| `data/query-pools/sciverse-api-integration-example.json` | Scientific API and agent workflow Query Pool sample |
| `data/models.sample.json` | Minimal single-model config |
| `data/models.multi.sample.json` | Default multi-model config |
| `data/manual.sample.json` | Minimal manual-response sample |
| `data/manual.multi.sample.json` | Multi-model manual-response sample |
| `data/runs/sample-run/summary.json` | Complete MinerU sample summary |
| `data/runs/sciverse-sample-run/summary.json` | Complete Sciverse API sample summary |

## Docs

- Getting started: [`docs/getting-started.md`](docs/getting-started.md)
- 5-minute beginner path: [`docs/for-beginners.md`](docs/for-beginners.md)
- Metric definition: [`docs/metric-definition.md`](docs/metric-definition.md)
- Activation metrics: [`docs/activation-metrics.md`](docs/activation-metrics.md)
- Benchmark notes: [`benchmark/README.md`](benchmark/README.md)
- Example case: [`examples/mineru-case-study.md`](examples/mineru-case-study.md)
- Weekly report template: [`templates/weekly-report.md`](templates/weekly-report.md)
- Repair validation template: [`templates/repair-validation.md`](templates/repair-validation.md)
- Agent readiness: [`playbooks/agent-readiness.md`](playbooks/agent-readiness.md)
- Developer-tool surface priority: [`playbooks/developer-tool-surface-priority.md`](playbooks/developer-tool-surface-priority.md)
- Scientific product GEO: [`playbooks/scientific-product-geo.md`](playbooks/scientific-product-geo.md)
- Companion skill: [ClawHub skill page](https://clawhub.ai/veeicwgy/geo-monitor-os-skill)

## Repository positioning

Think of this repository as:

> **GEO Monitoring OS for Developer Tools**
>
> It focuses on **monitoring, scoring, repair, activation, and regression**, not on generic marketing copy generation.

## Contributing

Contributions are welcome.

Useful contributions include:

- new query pool examples
- benchmark cases
- runner improvements
- report improvements
- schema and validation improvements
- documentation and onboarding fixes

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for details.

## License

MIT
