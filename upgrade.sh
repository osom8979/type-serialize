#!/usr/bin/env bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit; pwd)
VERSION=$(cat "$ROOT_DIR/VERSION")

BACKEND_PATH="$ROOT_DIR/type_serialize/__init__.py"

sed -i.tmp -e "s/^__version__ = \".*\"$/__version__ = \"$VERSION\"/" "$BACKEND_PATH"

rm "$BACKEND_PATH.tmp"
