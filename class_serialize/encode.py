# -*- coding: utf-8 -*-

from typing import Any

from class_serialize.byte.byte_coding import DEFAULT_BYTE_CODING_TYPE, object_to_bytes
from class_serialize.byte.variables import COMPRESS_LEVEL_TRADEOFF
from class_serialize.obj.serialize import serialize


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