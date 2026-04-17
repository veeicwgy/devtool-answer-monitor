.PHONY: validate sample-report

validate:
	python3 scripts/validate_data.py --repo-root .

sample-report:
	python3 scripts/score_run.py --input data/runs/sample-run/annotations.jsonl --output-dir data/runs/sample-run
	python3 scripts/generate_weekly_report.py --summary data/runs/sample-run/summary.json --output data/runs/sample-run/weekly_report.md
