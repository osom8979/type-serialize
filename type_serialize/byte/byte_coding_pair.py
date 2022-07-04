# -*- coding: utf-8 -*-

from inspect import signature
from typing import Any, Callable

ObjectToBytesCallable = Callable[..., bytes]
BytesToObjectCallable = Callable[[bytes], Any]


class ByteCodingPair:
    def __init__(self, encode: ObjectToBytesCallable, decode: BytesToObjectCallable):
        self.has_encode_level_arg = "level" in signature(encode).parameters
        self._encode = encode
        self._decode = decode

    def encode(self, data: Any, level: int) -> bytes:
        if self.has_encode_level_arg:
            return self._encode(data, level=level)
        else:
            return self._encode(data)

    def decode(self, data: bytes) -> Any:
        return self._decode(data)
