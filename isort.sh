#!/usr/bin/env bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit; pwd)

"$ROOT_DIR/python" -m isort \
    --check \
    --diff \
    --color \
    --settings-path "$ROOT_DIR/isort.cfg" \
    "$ROOT_DIR/setup.py" \
    "$ROOT_DIR/class_serialize/" \
    "$ROOT_DIR/test/"
