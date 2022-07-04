# -*- coding: utf-8 -*-

from typing import Any, Optional

from type_serialize.byte.byte_coding import ByteCoding
from type_serialize.decode import decode
from type_serialize.encode import encode
from type_serialize.variables import COMPRESS_LEVEL_TRADEOFF

CODING = ByteCoding.Yaml


def dumps(data: Any, *, level=COMPRESS_LEVEL_TRADEOFF) -> bytes:
    return encode(data, level=level, coding=CODING)


def loads(data: bytes, cls: Optional[Any] = None) -> Any:
    return decode(data, cls, coding=CODING)


def dump(data: Any, fp, *, level=COMPRESS_LEVEL_TRADEOFF) -> None:
    fp.write(dumps(data, level=level))


def load(fp, cls: Optional[Any] = None) -> Any:
    return loads(fp.read(), cls=cls)
