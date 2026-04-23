# Contributing

Thank you for contributing to **devtool-answer-monitor**.

## Contribution Paths

| Type | What to add |
|---|---|
| Bug fix | Fix runner, scoring, schema, or documentation issues |
| Feature | Improve CLI, leaderboard, schemas, or reports |
| Query pool | Add a new industry example or language segment |

## Documentation Language Policy

- The root landing pages must always ship in both languages: `README.md` and `README.zh-CN.md`.
- Any new folder-level README must also ship as a pair in the same directory: `README.md` and `README.zh-CN.md`.
- If you update one README, update its language pair in the same commit or PR.
- Benchmark pages and contributor-facing reader guides should follow the same bilingual rule when they are intended as repository entry pages.

## Add a New Industry Example

1. Copy an existing file in `data/query-pools/` as a starting template.
2. Replace `project`, `segments`, `priority`, and `expected_entity` fields with the new industry data.
3. Ensure each query has a clear `id`, `language`, `type`, and target scenario.
4. Run `python -m devtool_answer_monitor validate` to check schema compatibility.
5. If you add a sample run, place artifacts under `data/runs/<run-id>/`.
6. Update `README.md` so the new example appears in the example index.
7. If the change touches any README-style entry page, update both the English and Chinese versions together.

## Validation

```bash
make sample-report
python -m devtool_answer_monitor leaderboard
make validate
```
