#!/usr/bin/env bash
# Runs pytest inside every solution folder that has tests.
# Several folders contain files with the same names (test_app.py, for example),
# so each folder must be tested on its own.
set -u
status=0
export MPLBACKEND=Agg
for dir in $(find . -path '*/solution*' -name 'test_*.py' -exec dirname {} \; | sort -u); do
  echo "== $dir"
  (cd "$dir" && python -m pytest -q) || status=1
done
exit $status
