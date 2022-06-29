#!/usr/bin/env bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit; pwd)

"$ROOT_DIR/python" -m pytest \
     -v \
     --cov \
     --cov-report=term-missing \
     --cov-report=html \
     --cov-config="${ROOT_DIR}/pytest.ini" \
     "$ROOT_DIR/test/" \
     "$@"
