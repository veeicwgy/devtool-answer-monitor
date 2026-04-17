# GEO Monitor Toolkit

![CI](https://github.com/veeicwgy/geo-monitor-toolkit/actions/workflows/ci.yml/badge.svg)
![Release](https://img.shields.io/github/v/release/veeicwgy/geo-monitor-toolkit)
![Python](https://img.shields.io/badge/python-3.11-blue)

**GEO Monitor Toolkit** 是一套面向 **开发者工具、API、SDK 与开源项目** 的 GEO（Generative Engine Optimization）监控与内容优化工具包。它现在不仅提供 playbook，也提供 **可运行 runner、可复现评分 rubric、结构化 schema、CLI、leaderboard、repair loop 样例和 sample run 快照**，帮助团队把 `关键词研究 → 监控 → 打分 → 周报 → 修复 → 回归验证` 串成一条能演示、能协作、能复盘的工作流。

本仓库继续以 **MinerU** 作为主案例，并扩展到 SaaS、开源库和开发者工具多类 Query Pool。整体组织方式参考了可安装 Skill 仓库与 GEO 内容工作流项目。[1] [2] [3]

## Quick Demo

最短单命令体验：

```bash
make sample-report
```

执行完成后，你将得到一组完整的演示产物：

| 产物 | 路径 | 作用 |
|---|---|---|
| Raw responses | `data/runs/sample-run/raw_responses.jsonl` | 原始回答快照 |
| Score draft | `data/runs/sample-run/score_draft.jsonl` | 待标注与可复核打分草稿 |
| Summary | `data/runs/sample-run/summary.json` | 结构化指标摘要 |
| Weekly report | `data/runs/sample-run/weekly_report.md` | 可直接周会审阅的报告 |
| Leaderboard | `data/leaderboards/model_leaderboard.md` | 模型维度指标趋势表 |
| Visualization | `assets/leaderboard-sample.png` | 适合 README 展示的轻量证据图 |

## Expected Output Snapshot

下面这张图展示了跑完 sample 后会得到的轻量 leaderboard 快照：

![Leaderboard Snapshot](assets/leaderboard-sample.png)

## Why v0.2.0 Matters

| 维度 | v0.1 风格文档骨架 | v0.2.0 升级后 |
|---|---|---|
| 核心价值 | 方法论对齐 | 方法论 + 可运行演示 |
| 结果呈现 | 文档与 SOP | Raw、summary、weekly report、leaderboard |
| 评分一致性 | 依赖人工理解 | rubric + annotation protocol + schema |
| 闭环能力 | 修复建议为主 | repair validation + T+7 / T+14 案例 |
| 协作入口 | 需要口头说明 | issue templates + CONTRIBUTING |

## CLI

如果你不想直接调用脚本，可以使用统一 CLI：

```bash
python -m geo_monitor run --query-pool data/query-pools/mineru-example.json --model-config data/models.sample.json --out-dir data/runs/demo-run --manual-responses manual.json
python -m geo_monitor report --input data/runs/sample-run/annotations.jsonl --output-dir data/runs/sample-run
python -m geo_monitor leaderboard
python -m geo_monitor validate
```

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
| `run_manifest.json` | 本轮补充 |

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

## References

[1]: https://github.com/dageno-agents/geo-content-writer "dageno-agents/geo-content-writer"
[2]: https://github.com/aaron-he-zhu/seo-geo-claude-skills "aaron-he-zhu/seo-geo-claude-skills"
[3]: https://github.com/yaojingang/yao-geo-skills/tree/main/skills/geoflow-cli-ops "yaojingang/yao-geo-skills geoflow-cli-ops"
