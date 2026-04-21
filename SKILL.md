---
name: geo-monitor-toolkit
description: >
  Use when the user wants to monitor how ChatGPT, Claude, Gemini, and other LLMs describe a developer tool, API, SDK, or open-source project. GEO Monitor Toolkit is the companion skill for the geo-monitor-toolkit repo and covers query pool design, four-metric monitoring, model-specific content placement, GEO content checks, negative-answer repair, activation analysis, and T+7 or T+14 regression validation.
license: MIT
allowed-tools: Read, Write, Edit, Bash
metadata:
  openclaw:
    emoji: "📈"
    author: "Manus AI"
    homepage: "https://github.com/veeicwgy/geo-monitor-toolkit"
---

# Monitor How LLMs Describe Your Dev Tool

Use this skill as the **main GEO workflow router** for developer tools and open-source products.

**Brand:** GEO Monitor Toolkit

**Companion repo:** [`geo-monitor-toolkit`](https://github.com/veeicwgy/geo-monitor-toolkit)

Use this when you want an agent to help you monitor how LLMs describe your product, build a GEO query pool, diagnose negative or outdated answers, and plan what to fix next.

## Start Here

Copy one of these prompts to begin:

- `Analyze how ChatGPT and Claude describe my API docs`
- `Build a GEO query pool for my SDK`
- `Find negative or outdated LLM claims about my project`

## 30-Second Result

**Typical input**

- product truth such as a README, docs, changelog, integrations, or positioning page
- GEO evidence such as copied model answers, screenshots, or cited URLs
- scope such as target models, languages, regions, or a repeated query set

**What this skill returns**

- a reusable query pool
- raw evidence and a score draft plan
- a monitoring summary and report outline
- a repair backlog with T+7 or T+14 validation points

**Companion demo and sample outputs**

- Quick demo: [repo quick demo](https://github.com/veeicwgy/geo-monitor-toolkit#30-second-path)
- Sample outputs: [leaderboard snapshot](https://github.com/veeicwgy/geo-monitor-toolkit/blob/main/assets/leaderboard-sample.png) and [repair trend snapshot](https://github.com/veeicwgy/geo-monitor-toolkit/blob/main/assets/repair-trend-sample.png)

## Trigger

Use this skill when the task is any of the following:

1. generate a GEO keyword matrix and Query Pool from product truth;
2. monitor how multiple LLMs mention, recommend, or misunderstand a product;
3. plan model-specific content placement based on datasource patterns;
4. check whether a draft page, FAQ, changelog, or case study is GEO-ready;
5. repair wrong, negative, outdated, or competitor-only answers;
6. verify whether a repair action improved metrics at T+7 or T+14;
7. help a user choose between quickstart replay, manual paste mode, and API collection mode.

## Beginner Routing

When the user is new to the repository, route them in this order.

| Situation | Next step |
|---|---|
| Needs environment check first | run `make doctor` |
| Wants zero-cost first run | run `bash quickstart.sh` |
| Wants a short explanation first | open `docs/for-beginners.md` |
| Wants deeper onboarding | open `docs/getting-started.md` |
| Wants the English repository overview | open `README.md` |
| Wants the Chinese repository overview | open `README.zh-CN.md` |

## GEO Strategy

Always keep the workflow in this order:

| Stage | Goal |
|---|---|
| Keyword strategy | turn product truth into scenario matrix, three-layer keywords, and Query Pool seeds |
| Monitoring | score mention, positive mention, capability accuracy, and ecosystem accuracy |
| Placement | map each target model to likely datasource channels and publication surfaces |
| Repair | classify bad answers into information error, negative evaluation, outdated information, or competitor insertion |
| Activation | analyze whether answers help a user install, integrate, or invoke the product |
| Regression | compare follow-up runs and check whether metrics improved after action |

## Mode Selection

Choose the execution mode before running monitoring.

| Mode | Use when | Typical inputs |
|---|---|---|
| Quickstart replay | user wants the fastest first run without API setup | sample model config + sample manual responses |
| Manual paste mode | user already has copied answers from chat tools | Query Pool + manual response JSON |
| API collection mode | user wants repeatable real monitoring | Query Pool + model config + API credentials |

## Input Contract

Prepare as many of the following as possible before execution.

| Input | Examples |
|---|---|
| Product truth | README, docs, changelog, integrations, positioning |
| GEO evidence | raw answers, screenshots, copied responses, cited links |
| Monitoring scope | models, languages, regions, dates, repeated query set |
| Publishing targets | docs, blog, GitHub, Q&A, partner channels |

## Workflow Router

Choose the next sub-skill according to the user's immediate need.

| Situation | Next Skill |
|---|---|
| Need keyword matrix and Query Pool | `geo-keyword-matrix` |
| Need weekly monitoring, evidence logging, and report output | `geo-monitor` |
| Need pre-publish GEO QA for content | `geo-content-check` |
| Need to repair bad answers and define regression checks | `geo-fix-negative` |

## Required Reading Order

For a full GEO program, read these repository documents in sequence:

1. `playbooks/geo-workflow-architecture.md`
2. `playbooks/keyword-strategy.md`
3. `playbooks/monitoring-system.md`
4. `playbooks/model-datasources.md`
5. `playbooks/content-platform-map.md`
6. `playbooks/negative-fix-sop.md`

## Output Contract

Always preserve the following outputs.

| Output | Description |
|---|---|
| Query foundation | scenario matrix, keyword layers, Query Pool |
| Monitoring outputs | raw evidence, score draft, summary, report, leaderboard or overview |
| GEO action plan | content placement priorities and repair backlog |
| Regression record | T+7 and T+14 comparisons after key fixes |

## Positioning

GEO Monitor Toolkit is the skill layer for the `geo-monitor-toolkit` repo.

- Use the **repo** when you want runnable demos, scripts, and report artifacts.
- Use the **skill** when you want an agent-guided workflow for monitoring, repair, and regression planning.

## Handoff Rules

At the end of each run, preserve:

1. which product was optimized;
2. which models and languages were in scope;
3. which queries are reused in weekly tracking;
4. what the top three GEO weaknesses are;
5. what actions are already completed and what still needs validation.
