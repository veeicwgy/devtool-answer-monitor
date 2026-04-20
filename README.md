# GEO Monitor Toolkit

> Monitor how ChatGPT, Claude, Gemini, and other LLMs describe your developer tool, API, SDK, or open-source project.

[![CI](https://github.com/veeicwgy/geo-monitor-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/veeicwgy/geo-monitor-toolkit/actions/workflows/ci.yml)
![Release](https://img.shields.io/github/v/release/veeicwgy/geo-monitor-toolkit)
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/github/license/veeicwgy/geo-monitor-toolkit)

Prefer agent workflow? Install the [ClawHub skill](https://clawhub.ai/veeicwgy/geo-monitor-os-skill).

GEO Monitor Toolkit is an open-source workflow for **AI visibility monitoring**.

It pairs:

- the **`geo-monitor-toolkit` repo** for runnable demos, artifacts, and reporting scripts
- the **GEO Monitor Toolkit skill on ClawHub** for agent-guided monitoring, query-pool design, and repair workflows

It helps developer tools teams answer questions like:

- Does ChatGPT mention our product at all?
- Does Claude describe our capabilities correctly?
- Does Gemini misunderstand our integrations or ecosystem?
- After we update docs, changelogs, landing pages, or case studies, do model answers actually improve?

Unlike generic GEO or SEO content tools, this repository focuses on **measurement, repair, and regression tracking**.

## Try The Skill

If you want the agent workflow instead of starting with the CLI, install the companion skill on ClawHub and start with one of these prompts:

- `Analyze how ChatGPT and Claude describe my API docs`
- `Build a GEO query pool for my SDK`
- `Find negative or outdated LLM claims about my project`

The ClawHub skill is the companion agent layer for this repository:

- Skill page: [geo-monitor-os-skill on ClawHub](https://clawhub.ai/veeicwgy/geo-monitor-os-skill)
- Repo demo and outputs: [README quick demo](https://github.com/veeicwgy/geo-monitor-toolkit/tree/codex/update-readme-hero#quick-demo)

## Why This Exists

AI products are now a discovery layer.

For developer tools, APIs, SDKs, and open-source projects, the real problem is not just publishing more content. The real problem is whether LLMs:

- mention your product,
- describe it accurately,
- understand its capabilities,
- represent its ecosystem correctly,
- stop inserting competitors when your product should be recommended.

This project gives teams a reproducible way to track that.

## What You Get

- Reproducible query pools for AI-answer monitoring
- Raw response capture across models
- 4 core GEO metrics:
  - mention rate
  - positive mention rate
  - capability accuracy
  - ecosystem accuracy
- Repair workflow for outdated, negative, or competitor-biased answers
- T+7 / T+14 regression validation
- Weekly report and leaderboard outputs for team review

## Who This Is For

- Developer tools teams
- API and SDK companies
- DevRel teams
- Product marketing teams
- Open-source maintainers
- Growth teams running repeatable GEO programs

If you want a generic AI content generator, this repository is probably not the right tool.

## Quick Demo

```bash
git clone https://github.com/veeicwgy/geo-monitor-toolkit.git
cd geo-monitor-toolkit
bash install.sh
bash quickstart.sh
```

The quickstart is designed to show the workflow without requiring API calls.

After it runs, you should see outputs like:

- `data/runs/quickstart-run/raw_responses.jsonl`
- `data/runs/quickstart-run/score_draft.jsonl`
- `data/runs/quickstart-run/run_manifest.json`
- `data/runs/sample-run/summary.json`
- `data/runs/sample-run/weekly_report.md`
- `assets/leaderboard-sample.png`
- `assets/repair-trend-sample.png`

## 30-Second Result

If you want to know what this toolkit produces before reading deeper, here is the fastest path:

**Input**

- a query pool such as `data/query-pools/mineru-example.json`
- a model config such as `data/models.multi.sample.json`
- manual sample answers or live API responses

**Command**

```bash
bash quickstart.sh
```

**Output**

- `data/runs/quickstart-run/raw_responses.jsonl`
- `data/runs/quickstart-run/score_draft.jsonl`
- `data/runs/quickstart-run/run_manifest.json`
- `data/runs/sample-run/summary.json`
- `data/runs/sample-run/weekly_report.md`
- `assets/leaderboard-sample.png`
- `assets/repair-trend-sample.png`

**Artifacts you can hand to a team**

- a reusable query pool
- raw model evidence
- a draft scoring layer for review
- a weekly report
- a leaderboard snapshot
- a repair trend snapshot

## Example Outputs

![Model Leaderboard Snapshot](assets/leaderboard-sample.png)

![Repair Trend Snapshot](assets/repair-trend-sample.png)

## Core Workflow

The toolkit follows a simple loop:

1. Build a query pool for your product
2. Collect model answers
3. Score responses across 4 GEO metrics
4. Identify repair candidates
5. Publish fixes across docs, content, and ecosystem surfaces
6. Re-run the same queries at T+7 or T+14
7. Compare whether metrics improved

## Runtime Modes

| Mode | Inputs | Outputs | Best for |
|---|---|---|---|
| Quickstart replay | sample configs + manual responses | demo run + report snapshots | first-time experience |
| Manual paste mode | query pool + manual response JSON | raw responses + score draft | importing answers from external chats |
| API collection mode | query pool + model config + API key | raw responses + score draft | real GEO monitoring |
| Multi-provider collection | query pool + compatible gateway + enabled models | raw responses + run manifest | cross-model comparison |

## Minimal Files to Start From

| File | Purpose |
|---|---|
| `data/query-pools/mineru-example.json` | sample query pool |
| `data/models.sample.json` | single-model config |
| `data/models.multi.sample.json` | multi-model demo config |
| `data/manual.sample.json` | single-model manual responses |
| `data/manual.multi.sample.json` | multi-model manual responses |
| `docs/metric-definition.md` | metric definitions |

## CLI

```bash
python -m geo_monitor run \
  --query-pool data/query-pools/mineru-example.json \
  --model-config data/models.multi.sample.json \
  --out-dir data/runs/demo-run \
  --manual-responses data/manual.multi.sample.json

python -m geo_monitor report \
  --input data/runs/sample-run/annotations.jsonl \
  --output-dir data/runs/sample-run

python -m geo_monitor leaderboard
python -m geo_monitor validate
```

## Multi-Provider Collection

For OpenAI-compatible gateways:

```bash
export OPENAI_API_KEY=<your-key>
export OPENAI_BASE_URL=<your-gateway-url>

python scripts/run_chat_completions.py \
  --query-pool data/query-pools/mineru-example.json \
  --model-config data/models.sample.json \
  --out-dir data/runs/multi-provider-run
```

Then score and report after annotation.

## Repository Map

| Directory | What it contains |
|---|---|
| `data/` | query pools, sample configs, run outputs, repair validations |
| `schemas/` | structured validation contracts |
| `rubrics/` | scoring rules and annotation protocol |
| `scripts/` | run, score, report, leaderboard, validation scripts |
| `playbooks/` | GEO strategy, monitoring, datasource mapping, repair SOP |
| `examples/` | example cases |
| `templates/` | report and repair templates |

## Docs

- Getting started: [`docs/getting-started.md`](docs/getting-started.md)
- Metric definition: [`docs/metric-definition.md`](docs/metric-definition.md)
- Benchmark notes: [`benchmark/README.md`](benchmark/README.md)
- Example case: [`examples/mineru-case-study.md`](examples/mineru-case-study.md)
- Weekly report template: [`templates/weekly-report.md`](templates/weekly-report.md)
- Repair validation template: [`templates/repair-validation.md`](templates/repair-validation.md)
- Companion skill: [ClawHub skill page](https://clawhub.ai/veeicwgy/geo-monitor-os-skill)

## Positioning

**GEO Monitor Toolkit = AI Visibility Monitoring for Developer Tools**

This repository is not about generic content generation.

It is about measuring whether AI systems actually understand, mention, and recommend your product correctly, then validating whether your fixes improved the outcome.

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
