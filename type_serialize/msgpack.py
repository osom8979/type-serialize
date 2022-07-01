# -*- coding: utf-8 -*-

from typing import Any, Optional

from type_serialize.byte.byte_coding import ByteCodingType
from type_serialize.decode import decode
from type_serialize.encode import encode
from type_serialize.variables import COMPRESS_LEVEL_TRADEOFF

CODING = ByteCodingType.Msgpack


def dumps(data: Any, *, level=COMPRESS_LEVEL_TRADEOFF) -> bytes:
    return encode(data, coding=CODING, level=level)


def loads(data: bytes, cls: Optional[Any] = None) -> Any:
    return decode(data, cls, coding=CODING)


def dump(data: Any, fp, *, level=COMPRESS_LEVEL_TRADEOFF) -> None:
    fp.write(dumps(data, level=level))


def load(fp, cls: Optional[Any] = None) -> Any:
    return loads(fp.read(), cls=cls)
