# -*- coding: utf-8 -*-

from typing import Any, Final

from type_serialize.byte.byte_coding import ByteCoding
from type_serialize.byte.byte_coding_map import BYTE_CODING_MAP
from type_serialize.variables import COMPRESS_LEVEL_TRADEOFF

DEFAULT_BYTE_CODING_TYPE: Final[ByteCoding] = ByteCoding.JsonGzip


def object_to_bytes(
    coding: ByteCoding,
    data: Any,
    *,
    level=COMPRESS_LEVEL_TRADEOFF,
) -> bytes:
    return BYTE_CODING_MAP[coding].encode(data, level=level)


def bytes_to_object(coding: ByteCoding, data: bytes) -> Any:
    return BYTE_CODING_MAP[coding].decode(data)
