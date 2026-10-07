#!/bin/bash
# Usage: export ANTHROPIC_API_KEY=your_key && ./run_all.sh
mkdir -p outputs
for f in 0*.py; do echo "== $f =="; python3 $f 2>&1 | tee outputs/${f%.py}.txt; done
