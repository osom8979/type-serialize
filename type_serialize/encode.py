# -*- coding: utf-8 -*-

from typing import Any

from type_serialize.byte.byte_coding import DEFAULT_BYTE_CODING_TYPE, object_to_bytes
from type_serialize.variables import COMPRESS_LEVEL_TRADEOFF
from type_serialize.obj.serialize import serialize


def encode(
    data: Any,
    coding=DEFAULT_BYTE_CODING_TYPE,
    level=COMPRESS_LEVEL_TRADEOFF,
) -> bytes:
    return object_to_bytes(
        coding=coding,
        data=serialize(data),
        level=level,
    )
