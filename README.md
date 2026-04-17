# GEO Monitor Toolkit

**GEO Monitor Toolkit** 是一套面向 **开发者工具、API、SDK 与开源项目** 的 GEO（Generative Engine Optimization）监控与内容优化工具包。它不再只是流程说明，而是同时提供 **可运行 runner、可复现评分 rubric、结构化 schema、多行业 Query Pool 样例、修复验证模板与基础 CI**，帮助团队把 `关键词研究 → 监控 → 打分 → 周报 → 修复 → 回归验证` 串成一条可以落地执行的工作流。

该仓库依然以 **MinerU** 作为主案例，但本次升级后不再停留在文档骨架层，而是补上了最小可运行评估链路，方便团队从“策略讨论”走向“可审计复盘”。仓库设计继续参考可安装 Skill 仓库与 GEO 内容工作流项目的组织方式。[1] [2] [3]

## Why This Repository

| 维度 | 旧式文档型 GEO 仓库 | 本仓库升级后的定位 |
|---|---|---|
| 工作重心 | 方法论说明 | 方法论 + 可运行评估骨架 |
| 主要对象 | 泛内容团队 | 开发者工具、开源项目、技术产品团队 |
| 核心输出 | Playbook、SOP、模板 | Runner、评分草稿、结构化 summary、周报、修复验证记录 |
| 可复现性 | 依赖人工理解 | 通过 rubric、schema、CI 降低口径漂移 |
| 适合场景 | 对齐流程、培训团队 | 监控周会、异常归因、修复跟踪、KPI 审计 |

## Quick Start

如果你希望整库安装并直接复用工作流，可以使用：

```bash
npx skills add veeicwgy/geo-monitor-toolkit
```

如果你只希望安装某一个技能，可以使用：

```bash
npx skills add veeicwgy/geo-monitor-toolkit -s geo-monitor
npx skills add veeicwgy/geo-monitor-toolkit -s geo-content-check
npx skills add veeicwgy/geo-monitor-toolkit -s geo-fix-negative
npx skills add veeicwgy/geo-monitor-toolkit -s geo-keyword-matrix
```

如果你希望直接运行监控骨架，可以先安装依赖：

```bash
pip install -r requirements.txt
```

然后运行样例汇总与周报生成：

```bash
make sample-report
make validate
```

## What Is Now Executable

本仓库新增了一条最小可运行链路，使 GEO 监控可以先离线、后半自动、再逐步走向自动化。

| 步骤 | 输入 | 脚本 | 输出 |
|---|---|---|---|
| 采集 | Query Pool + 模型配置 | `scripts/run_monitor.py` | `raw_responses.jsonl` `score_draft.jsonl` `run_manifest.json` |
| 标注/打分 | score draft 或人工补录 annotation | `scripts/score_run.py` | `summary.json` `metrics.csv` |
| 周报 | `summary.json` | `scripts/generate_weekly_report.py` | `weekly_report.md` |
| 校验 | schema + 样例数据 | `scripts/validate_data.py` | 校验结果，用于本地和 CI |

## Reproducible Scoring System

本仓库把原来抽象的四个指标，落实成了 **0-2 离散评分系统**，再统一换算为 0-100 指标，降低不同标注人之间的漂移。

| 指标 | 评分字段 | 解释 |
|---|---|---|
| 提及率 | `mention_score` | 目标产品是否被提及，以及是否是主推 |
| 正面提及率 | `sentiment_score` | 提及后是负面、中性还是正向推荐 |
| 能力准确率 | `capability_score` | 核心能力是否说对、是否说清边界 |
| 生态准确率 | `ecosystem_score` | SDK、集成、上下游实体关系是否准确 |

判定标准详见 `rubrics/scoring-rubric.md`，标注流程详见 `rubrics/annotation-protocol.md`。

## Data and Artifact Conventions

为了保证团队协作和历史可追踪性，本仓库新增了统一的数据目录和产物结构。

```text
geo-monitor-toolkit/
├── data/
│   ├── query-pools/
│   ├── runs/
│   │   └── sample-run/
│   └── repair-validations/
├── rubrics/
├── schemas/
├── scripts/
├── templates/
└── .github/workflows/
```

| 目录 | 用途 |
|---|---|
| `data/query-pools/` | 不同行业与项目的 Query Pool 样例 |
| `data/runs/` | 每次运行的原始回答、打分草稿、summary、周报 |
| `data/repair-validations/` | 修复动作与 T+7 / T+14 跟踪记录 |
| `schemas/` | Query Pool、run summary、repair validation 的 JSON Schema |
| `scripts/` | 采集、打分、周报、校验脚本 |
| `templates/` | 周报与修复验证模板 |

## Multi-Industry Examples

为了避免仓库只围绕 MinerU 单一案例，本次新增了三个行业样例，证明相同 schema 与 runner 可以复用到不同对象。

| 类型 | 示例文件 | 说明 |
|---|---|---|
| Developer tool | `data/query-pools/mineru-example.json` | 文档解析 / RAG 预处理 / 复杂 PDF 场景 |
| SaaS | `data/query-pools/posthog-saas-example.json` | 产品分析与增长类 SaaS 场景 |
| Open-source library | `data/query-pools/fastapi-open-source-library-example.json` | Python API 框架类开源库场景 |
| Developer tool / LLMOps | `data/query-pools/langfuse-developer-tool-example.json` | LLM 可观测性与评测工作流场景 |

## Repair Validation Loop

仓库新增了结构化修复验证对象，而不只是负向修复 SOP。团队可以把一次修复动作表示成一个实验记录，明确动作类型、目标 query、基线 run、T+7 / T+14 follow-up run 与最终结论。

| 文件 | 作用 |
|---|---|
| `schemas/repair-validation.schema.json` | 统一 repair validation 数据结构 |
| `templates/repair-validation.md` | 生成适合周会复盘的文本模板 |
| `data/repair-validations/sample-repair-validation.json` | 示例化的修复验证记录 |

## Skill Map

| Skill | 用途 | 典型输入 | 典型输出 |
|---|---|---|---|
| `geo-keyword-matrix` | 从产品描述生成场景矩阵与 Query Pool | 产品描述、目标用户、核心能力、竞品 | 核心词/场景词/长尾词、场景矩阵、验证闭环 |
| `geo-monitor` | 跑 Query Pool 并生成四维指标周报 | Query Pool、模型列表、回答样本 | 提及率/正面率/能力准确率/生态准确率周报 |
| `geo-content-check` | 发布前进行 GEO 质检 | 草稿、实体定义、目标模型 | 质检分、结构缺口、引用友好性建议 |
| `geo-fix-negative` | 识别负向类型并生成修复方案 | 负向回答、引用来源、标准事实 | 类型判断、修复动作表、回归验证计划 |

## Repository Map

```text
geo-monitor-toolkit/
├── README.md
├── LICENSE
├── SKILL.md
├── manifest.json
├── requirements.txt
├── Makefile
├── data/
│   ├── models.sample.json
│   ├── query-pools/
│   ├── runs/
│   └── repair-validations/
├── rubrics/
│   ├── scoring-rubric.md
│   └── annotation-protocol.md
├── schemas/
│   ├── query-pool.schema.json
│   ├── run-results.schema.json
│   └── repair-validation.schema.json
├── scripts/
│   ├── run_monitor.py
│   ├── score_run.py
│   ├── generate_weekly_report.py
│   └── validate_data.py
├── templates/
│   ├── weekly-report.md
│   └── repair-validation.md
├── playbooks/
├── examples/
└── skills/
```

## Recommended Adoption Order

| 周期 | 重点动作 | 目标 |
|---|---|---|
| 第 1 周 | 建关键词矩阵、整理 Query Pool、确认模型清单与 rubric | 建好监控地基 |
| 第 2 周 | 跑首轮 sample run、产出周报、校准评分偏差 | 建立基线 |
| 第 3-4 周 | 执行内容铺设与负向修复动作 | 把动作写入 repair validation |
| 第 5 周起 | 做 T+7 / T+14 回归并比较 summary 变化 | 建立闭环证明 |

## Current Boundary

本仓库已经补齐了 **最小可运行骨架**，但仍然刻意保持轻量：它更适合做统一监控结构、评分与复盘，而不是直接替代完整的 GEO SaaS 产品。对于未开放 API 的模型，推荐先用人工复制回答或自建采集层，再接入这里的 schema、rubric 与报告流水线。

## References

[1]: https://github.com/dageno-agents/geo-content-writer "dageno-agents/geo-content-writer"
[2]: https://github.com/aaron-he-zhu/seo-geo-claude-skills "aaron-he-zhu/seo-geo-claude-skills"
[3]: https://github.com/yaojingang/yao-geo-skills/tree/main/skills/geoflow-cli-ops "yaojingang/yao-geo-skills geoflow-cli-ops"
