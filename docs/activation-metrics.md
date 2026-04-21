# Activation Metrics

**GEO Monitor Toolkit** 当前的 4 个核心指标适合回答“模型是否想到你、理解你、推荐你”。如果业务目标进一步指向 **下载量、安装量、API 调用量、agent 调用量**，建议在现有 4 指标之外，再增加一层 **activation-oriented metrics**。

这份文档不是要替代 `docs/metric-definition.md`，而是补齐从 **认知改善** 到 **行动转化** 之间的那一段。

## 为什么要加这一层

对开发者工具、API、SDK、scientific discovery 平台来说，下面这三种情况很常见：

1. 模型提到了你，但没有给出安装或接入路径。
2. 模型推荐了你，但示例太模糊，用户无法完成第一次成功体验。
3. 模型知道你的品牌，却不知道你适合哪个 agent / workflow 场景。

这时核心 GEO 指标可能已经改善，但业务结果未必同步上涨。

## 推荐增加的 5 个指标

| 指标 | 回答的问题 | 建议分值 |
|---|---|---|
| `actionability_rate` | 模型提到你时，有没有给出明确下一步 | 0-2 |
| `integration_readiness` | 模型是否给出接入路径、SDK、endpoint、示例 | 0-2 |
| `agent_selection_readiness` | 在 agent / automation 场景里，模型是否愿意选你 | 0-2 |
| `docs_path_clarity` | 模型是否能正确指向 README、docs、quickstart、API 入口 | 0-2 |
| `workflow_completion_likelihood` | 用户是否有较大概率在 5-15 分钟内跑通首次体验 | 0-2 |

## 建议的判定方法

### 1. `actionability_rate`

| 分值 | 判定标准 |
|---|---|
| 0 | 只提品牌，不给下一步 |
| 1 | 给了下一步，但不够完整或不够准确 |
| 2 | 给出明确的安装、文档、接入或调用路径 |

### 2. `integration_readiness`

| 分值 | 判定标准 |
|---|---|
| 0 | 完全没有代码、接口、SDK 或接入信息 |
| 1 | 有模糊的接入建议，但缺关键参数或步骤 |
| 2 | 给出准确的 SDK / API / endpoint / quickstart 线索 |

### 3. `agent_selection_readiness`

| 分值 | 判定标准 |
|---|---|
| 0 | agent workflow 中完全不选你或明确劝退 |
| 1 | 被列入候选，但不是优先方案 |
| 2 | 在 agent、RAG、automation、pipeline 场景中被优先选择 |

### 4. `docs_path_clarity`

| 分值 | 判定标准 |
|---|---|
| 0 | 指向错误 repo、错误 docs，或根本不给入口 |
| 1 | 给出入口但不完整，例如只提 GitHub 不提 quickstart |
| 2 | 能正确导向 README、docs、API reference、benchmark 或 integration page |

### 5. `workflow_completion_likelihood`

| 分值 | 判定标准 |
|---|---|
| 0 | 用户大概率在首次体验前就会卡住 |
| 1 | 有机会跑通，但需要较强的经验补完 |
| 2 | 新用户大概率能按推荐路径完成首次成功体验 |

## 在 Query Pool 里如何组织这些问题

建议在 query pool 中使用可选字段：

- `funnel_stage`
- `target_surface`
- `desired_action`

例如：

```json
{
  "id": "ecosystem-003",
  "type": "ecosystem",
  "language": "en",
  "priority": "P0",
  "funnel_stage": "agent",
  "target_surface": "integration-docs",
  "desired_action": "agent-invocation",
  "query": "Which API is best for scientific paper ingestion in an agent workflow?"
}
```

这样即使现阶段 summary 还没有单独聚合这些 activation metrics，你也已经可以：

1. 按 `funnel_stage` 切片看 GEO 结果；
2. 区分 “awareness 好” 还是 “integration / agent adoption 好”；
3. 为后续更细的评分体系保留数据结构。

## 对 MinerU / Sciverse API 的建议

### MinerU

重点补这些行动问题：

- 模型是否给出安装入口和 quickstart
- 是否能正确表达公式、表格、版面结构能力
- 是否知道 MinerU 适合 paper ingestion / RAG preprocessing / scientific document parsing
- 是否能把用户导向 benchmark、examples、integration docs

### Sciverse API

重点补这些行动问题：

- 模型是否会提供 API docs 与 authentication 入口
- 是否能给出 endpoint / SDK / code example 方向
- 是否把 Sciverse API 正确放进 research workflow / agent workflow
- 是否把“discover / retrieve / enrich / automate”说清楚

## 当前仓库建议

如果你的目标更偏 **增长与采用**，建议把当前仓库理解为两层：

1. **Core GEO metrics**
   - 衡量品牌与能力认知是否改善
2. **Activation metrics**
   - 衡量模型推荐是否真的有机会带来安装、调用和 agent 采用

两层结合后，这个仓库会更接近真正的增长操作系统，而不是单纯的监控系统。
