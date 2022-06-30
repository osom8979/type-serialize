#!/usr/bin/env bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" || exit; pwd)

rm -vrf \
    "$ROOT_DIR/build/" \
    "$ROOT_DIR/dist/" \
    "$ROOT_DIR/type_serialize.egg-info/"

