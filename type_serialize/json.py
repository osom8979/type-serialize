# -*- coding: utf-8 -*-

from typing import Any, Optional

from type_serialize.byte.byte_coding import ByteCodingType
from type_serialize.decode import decode
from type_serialize.encode import encode
from type_serialize.variables import COMPRESS_LEVEL_TRADEOFF

CODING = ByteCodingType.Json


def dumps(data: Any, *, level=COMPRESS_LEVEL_TRADEOFF) -> bytes:
    return encode(data, coding=CODING, level=level)


def loads(data: bytes, cls: Optional[Any] = None) -> Any:
    return decode(data, cls, coding=CODING)
