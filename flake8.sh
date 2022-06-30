#!/usr/bin/env bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit; pwd)

"$ROOT_DIR/python" -m flake8 \
    --config="${ROOT_DIR}/flake8.ini" \
    "$ROOT_DIR/setup.py" \
    "$ROOT_DIR/type_serialize/" \
    "$ROOT_DIR/test/"
