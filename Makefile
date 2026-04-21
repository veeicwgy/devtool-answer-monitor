.PHONY: install doctor validate sample-report sample-report-sciverse sample-reports run-demo leaderboard quick-demo quickstart

install:
	bash ./install.sh

doctor:
	bash ./scripts/doctor.sh

validate:
	python3 scripts/validate_data.py --repo-root .

sample-report:
	python3 scripts/score_run.py --input data/runs/sample-run/annotations.jsonl --output-dir data/runs/sample-run
	python3 scripts/generate_weekly_report.py --summary data/runs/sample-run/summary.json --output data/runs/sample-run/weekly_report.md
	python3 scripts/build_leaderboard.py --runs-root data/runs --output-dir data/leaderboards --image-output assets/leaderboard-sample.png
	python3 scripts/build_repair_trend.py

sample-report-sciverse:
	python3 scripts/score_run.py --input data/runs/sciverse-sample-run/annotations.jsonl --output-dir data/runs/sciverse-sample-run
	python3 scripts/generate_weekly_report.py --summary data/runs/sciverse-sample-run/summary.json --output data/runs/sciverse-sample-run/weekly_report.md

sample-reports: sample-report sample-report-sciverse

run-demo:
	python3 -m geo_monitor run --query-pool data/query-pools/mineru-example.json --model-config data/models.multi.sample.json --out-dir data/runs/demo-run --manual-responses data/manual.multi.sample.json

leaderboard:
	python3 scripts/build_leaderboard.py --runs-root data/runs --output-dir data/leaderboards --image-output assets/leaderboard-sample.png
	python3 scripts/build_repair_trend.py

quick-demo: run-demo sample-report validate

quickstart:
	bash ./quickstart.sh
