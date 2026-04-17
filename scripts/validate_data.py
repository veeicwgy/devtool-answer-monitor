#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

from jsonschema import validate


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_query_pools(root):
    schema = load_json(root / "schemas/query-pool.schema.json")
    for path in (root / "data/query-pools").glob("*.json"):
        validate(instance=load_json(path), schema=schema)


def validate_repair(root):
    schema = load_json(root / "schemas/repair-validation.schema.json")
    for path in (root / "data/repair-validations").glob("*.json"):
        validate(instance=load_json(path), schema=schema)


def validate_summary(root):
    sample = root / "data/runs/sample-run/summary.json"
    if sample.exists():
        schema = load_json(root / "schemas/run-results.schema.json")
        validate(instance=load_json(sample), schema=schema)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    args = ap.parse_args()
    root = Path(args.repo_root)
    validate_query_pools(root)
    validate_repair(root)
    validate_summary(root)
    print("validation passed")


if __name__ == "__main__":
    sys.exit(main())
