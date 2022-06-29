# -*- coding: utf-8 -*-

from typing import Any, Optional

from class_serialize.byte_coding import (
    DEFAULT_BYTE_CODING_TYPE,
    bytes_to_object,
    object_to_bytes,
)
from class_serialize.deserialize import deserialize
from class_serialize.serialize import serialize
from class_serialize.variables import COMPRESS_LEVEL_TRADEOFF, DEFAULT_PICKLE_ENCODING

__version__ = "0.0.1"


def encode(
    data: Any,
    coding=DEFAULT_BYTE_CODING_TYPE,
    level=COMPRESS_LEVEL_TRADEOFF,
) -> bytes:
    return object_to_bytes(
        data=serialize(data),
        coding=coding,
        level=level,
    )


def decode(
    data: bytes,
    cls: Optional[Any] = None,
    coding=DEFAULT_BYTE_CODING_TYPE,
    encoding=DEFAULT_PICKLE_ENCODING,
) -> Any:
    obj = bytes_to_object(data=data, coding=coding, encoding=encoding)
    if cls is not None:
        return deserialize(obj, cls)
    else:
        return obj
