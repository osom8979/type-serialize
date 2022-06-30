#!/usr/bin/env bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit; pwd)

"$ROOT_DIR/python" -m black \
    --check \
    --diff \
    --color \
    "$ROOT_DIR/setup.py" \
    "$ROOT_DIR/type_serialize/" \
    "$ROOT_DIR/test/"
