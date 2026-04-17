---
name: geo-monitor
description: >
  Use when the user wants to run or design GEO monitoring for a developer tool, API, SDK, or open-source project. Covers Query Pool execution, evidence logging, four-metric scoring, weekly reporting, anomaly detection, and action prioritization across multiple LLMs and languages.
---

# geo-monitor

Use this skill to turn repeated model checks into a consistent GEO monitoring workflow.

## Trigger

Use this skill when the user already has, or is ready to create, a Query Pool and wants to know:

1. whether the product is being mentioned;
2. whether mentions are positive, neutral, or negative;
3. whether the model understands the product's capabilities;
4. whether the model understands the product's ecosystem and integrations.

## Quick Start

### Choose the right runner

| Runner | API Type | Works with | Use when |
|---|---|---|---|
| `scripts/run_monitor.py` | Responses API | OpenAI models only | GPT-4o, GPT-4.1 and variants |
| `scripts/run_chat_completions.py` | Chat Completions API | Any OpenAI-compatible provider | Claude, Gemini, DeepSeek, Qwen, MiniMax, GLM, or any gateway |

**For multi-model coverage across providers, always use `run_chat_completions.py`.**

```bash
export OPENAI_API_KEY=<your-key>
export OPENAI_BASE_URL=<gateway-url>   # omit to use OpenAI directly

python scripts/run_chat_completions.py \
    --query-pool  data/query-pools/mineru-example.json \
    --model-config data/models.sample.json \
    --out-dir data/runs/my-run
```

Then annotate scores and generate the report:

```bash
python -m geo_monitor report \
    --input data/runs/my-run/raw_responses.jsonl \
    --output-dir data/runs/my-run
```

### Collect or create the following inputs:

| Input | Description |
|---|---|
| Query Pool | brand, capability, ecosystem, competitor, and negative queries |
| Model list | which LLMs, regions, and languages to monitor |
| Evidence samples | raw answers, screenshots, copied text, cited links |
| Entity truth | official facts used to judge correctness |

## Workflow

### 1. Normalize the monitoring scope

Fix the exact query set, language, model list, date, and evaluator so weekly reports stay comparable.

### 2. Capture evidence

For each query-model pair, preserve the answer text, brand mentions, competitor mentions, and any cited links.

### 3. Score the four core metrics

| Metric | Scoring question |
|---|---|
| Mention Rate | Did the model mention the target product in a non-branded query? |
| Positive Mention Rate | Was the product recommended positively? |
| Capability Accuracy | Did the model describe core capabilities correctly? |
| Ecosystem Accuracy | Did the model describe SDK, integrations, and surrounding entities correctly? |

### 4. Tag anomalies

Flag these high-priority cases immediately:

- wrong factual claim;
- negative recommendation;
- missing ecosystem integration;
- competitor-only answer;
- entity confusion.

### 5. Produce the weekly report

The report must include:

1. a model-by-model score table;
2. a list of high-priority broken queries;
3. the top three content or repair actions for the next cycle.

## Outputs

| Output | Description |
|---|---|
| Monitoring summary | overall week snapshot |
| Four-metric score table | mention, positive mention, capability, ecosystem |
| Anomaly list | urgent issues by model and query |
| Action backlog | next content, repair, and verification moves |

## Handoff

Always preserve:

1. the exact Query Pool version;
2. the model list and date window;
3. the top three weak queries;
4. the top three weak models;
5. the actions already completed.

## Next Best Skill

If the main issue is missing or weak content, use `geo-content-check`.

If the main issue is negative or wrong answers, use `geo-fix-negative`.
