# GEO Monitor Toolkit

![PyCI](https://img.shields.io/badge/PyCI-ready-2563eb)
![Release](https://img.shields.io/github/v/release/veeicwgy/geo-monitor-toolkit)
![Python](https://img.shields.io/badge/python-3.11-blue)

> **GEO monitoring operating system for dev tools**

**GEO Monitor Toolkit** 是一套面向 **开发者工具、API、SDK 与开源项目** 的 GEO（Generative Engine Optimization）监控与修复中台工具包。它不仅提供 playbook，也提供 **可运行 runner、可复现评分 rubric、结构化 schema、CLI、leaderboard、repair loop 样例和 sample run 快照**，帮助团队把 `关键词研究 → 监控 → 打分 → 周报 → 修复 → 回归验证` 串成一条能演示、能协作、能复盘的工作流。本仓库继续以 **MinerU** 作为主案例，并扩展到 SaaS、开源库和开发者工具多类 Query Pool。[1] [2] [3]

## Quick Demo

如果你只想最快看见“跑完会得到什么”，推荐从下面两个命令开始。

| 命令 | 类型 | 你会看到什么 |
|---|---|---|
| `make sample-report` | **离线样本重放** | 基于仓库内现成 `annotations.jsonl` 生成 `summary.json`、`weekly_report.md` 与 leaderboard |
| `make run-demo` | **手工模式演示** | 基于仓库内 `manual.sample.json` 生成 `raw_responses.jsonl` 与 `score_draft.jsonl` |

请注意，**`make sample-report` 是基于现成样本重放，不是全自动采集**。它的作用是让新访客快速理解评分、汇总与周报生成链路，而不是替代真实采集。

## Three Runtime Modes

| 模式 | 输入 | 输出 | 适用场景 |
|---|---|---|---|
| 离线样本重放 | `data/runs/sample-run/annotations.jsonl` | `summary.json`、`weekly_report.md`、leaderboard | 先理解报告生成链路 |
| 手工粘贴回答 | Query Pool + `data/manual.sample.json` | `raw_responses.jsonl`、`score_draft.jsonl` | 没有 API key 时演示从 query 到草稿的闭环 |
| API 采集（单 provider） | Query Pool + `data/models.sample.json` + key | `raw_responses.jsonl`、后续 summary/report | OpenAI 模型，使用 `run_monitor.py` |
| **API 采集（多 provider）** | Query Pool + `data/models.sample.json` + key | `raw_responses.jsonl`、后续 summary/report | **Claude / Gemini / DeepSeek / Qwen / MiniMax / GLM 等，使用 `run_chat_completions.py`** |

## Multi-Provider API Collection

`run_chat_completions.py` 使用通用的 Chat Completions 接口，兼容所有 OpenAI-compatible 网关，可以同时采集多个 AI 厂商的回答：

```bash
export OPENAI_API_KEY=<your-key>
export OPENAI_BASE_URL=<your-gateway-url>  # 如 http://your-gateway/v1

python scripts/run_chat_completions.py \
    --query-pool  data/query-pools/mineru-example.json \
    --model-config data/models.sample.json \
    --out-dir data/runs/multi-provider-run

# 标注打分后生成报告
python -m geo_monitor report \
    --input data/runs/multi-provider-run/raw_responses.jsonl \
    --output-dir data/runs/multi-provider-run
```

在 `data/models.sample.json` 中将需要的模型 `enabled` 设为 `true`，支持的模型示例：

| 模型 | api_model 字段 | 说明 |
|---|---|---|
| GPT-4o | `gpt-4o` | OpenAI 原生 |
| Claude Sonnet | `claude-sonnet-4-6` | 需通过兼容网关 |
| Gemini 2.5 Flash | `gemini-2.5-flash` | 需通过兼容网关 |
| DeepSeek V3 | `deepseek-v3-250324` | 需通过兼容网关 |
| Qwen Max | `qwen-max` | 需通过兼容网关 |
| MiniMax M2 | `minimax/minimax-m2` | 需通过兼容网关 |
| GLM-5 | `glm-5` | 需通过兼容网关 |

## Minimal Files You Can Start From

| 文件 | 作用 |
|---|---|
| [`data/models.sample.json`](data/models.sample.json) | 最小模型配置样例 |
| [`data/manual.sample.json`](data/manual.sample.json) | 最小手工回答样例 |
| [`docs/metric-definition.md`](docs/metric-definition.md) | 指标口径说明页，解释 0-2 打分与 KPI 映射 |
| [`data/query-pools/mineru-example.json`](data/query-pools/mineru-example.json) | 默认 run-demo 使用的 Query Pool |

## CLI

如果你不想直接调用脚本，可以使用统一 CLI：

```bash
python -m geo_monitor run --query-pool data/query-pools/mineru-example.json --model-config data/models.sample.json --out-dir data/runs/demo-run --manual-responses data/manual.sample.json
python -m geo_monitor report --input data/runs/sample-run/annotations.jsonl --output-dir data/runs/sample-run
python -m geo_monitor leaderboard
python -m geo_monitor validate
```

## Expected Output Snapshot

下面这张图展示了跑完 sample 后会得到的轻量 leaderboard 快照：

![Leaderboard Snapshot](assets/leaderboard-sample.png)

下面这张图展示了修复动作落地后，从 baseline 到 `T+7 / T+14` 的指标改善趋势：

![Repair Trend Snapshot](assets/repair-trend-sample.png)

## Sample Run Snapshot

`data/runs/sample-run/` 现在包含一份更完整的快照，用来回答“跑完后到底会得到什么”。

| 文件 | 是否提供 |
|---|---|
| `raw_responses.jsonl` | 是 |
| `score_draft.jsonl` | 是 |
| `annotations.jsonl` | 是 |
| `summary.json` | 是 |
| `metrics.csv` | 是 |
| `weekly_report.md` | 是 |
| `run_manifest.json` | 是 |

## Multi-Industry Query Pools

| 类型 | 示例文件 | 场景 |
|---|---|---|
| Developer tool | `data/query-pools/mineru-example.json` | PDF 解析、RAG 预处理、复杂文档抽取 |
| SaaS | `data/query-pools/posthog-saas-example.json` | 产品分析与增长工作流 |
| Open-source library | `data/query-pools/fastapi-open-source-library-example.json` | Python API 框架与生态判断 |
| Developer tool / LLMOps | `data/query-pools/langfuse-developer-tool-example.json` | LLM 可观测性与评测 |

## Repair Loop Examples

本仓库已经补充 3 个“修复动作 → T+7/T+14 指标变化”案例，用于展示 GEO 修复不是只停留在建议层，而是可以沉淀为结构化实验记录。

| 文件 | 类型 |
|---|---|
| `data/repair-validations/mineru-error-fix-case.json` | 信息错误修复 |
| `data/repair-validations/mineru-outdated-fix-case.json` | 过时信息修复 |
| `data/repair-validations/mineru-competitor-fix-case.json` | 竞品植入修复 |

## Benchmark and Reader Guide

如果你要向团队解释“不同项目如何横向比较”或“非工程同学如何读周报”，可以直接从以下入口开始。

| 文件 | 作用 |
|---|---|
| [`benchmark/README.md`](benchmark/README.md) | 同类 Query Pool 的横向 benchmark 范式 |
| [`notebooks/README.md`](notebooks/README.md) | 非工程同学的阅读路径说明 |

## Collaboration

如果你准备一起扩展这个仓库，可以直接使用以下入口：

| 文件 | 作用 |
|---|---|
| `.github/ISSUE_TEMPLATE/bug_report.md` | 提交运行或数据问题 |
| `.github/ISSUE_TEMPLATE/feature_request.md` | 提出新功能建议 |
| `.github/ISSUE_TEMPLATE/new_query_pool_request.md` | 请求新行业或新语言样例 |
| `CONTRIBUTING.md` | 按模板新增一个行业样例 |

## Release Notes

当前推荐版本是 **v0.2.0**。版本说明见 `CHANGELOG.md` 与 `release-notes/v0.2.0.md`。

## CI Badge Note

当前顶部使用的是静态 **PyCI** 徽章。等 `.github/workflows/ci.yml` 成功进入远端仓库后，可以切换为真实 GitHub Actions 状态徽章，以反映 `make validate`、样例 run 检查和 schema 校验结果。

## References

[1]: https://github.com/dageno-agents/geo-content-writer "dageno-agents/geo-content-writer"
[2]: https://github.com/aaron-he-zhu/seo-geo-claude-skills "aaron-he-zhu/seo-geo-claude-skills"
[3]: https://github.com/yaojingang/yao-geo-skills/tree/main/skills/geoflow-cli-ops "yaojingang/yao-geo-skills geoflow-cli-ops"
