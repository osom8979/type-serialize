# -*- coding: utf-8 -*-

from typing import Any

from type_serialize.byte.byte_coder import DEFAULT_BYTE_CODING_TYPE, object_to_bytes
from type_serialize.obj.serialize import serialize
from type_serialize.variables import COMPRESS_LEVEL_TRADEOFF


def encode(
    data: Any,
    level=COMPRESS_LEVEL_TRADEOFF,
    coding=DEFAULT_BYTE_CODING_TYPE,
) -> bytes:
    return object_to_bytes(
        coding=coding,
        data=serialize(data),
        level=level,
    )
