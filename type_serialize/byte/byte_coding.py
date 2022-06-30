# -*- coding: utf-8 -*-

from enum import Enum, unique
from inspect import signature
from typing import Any, Callable, Dict, Final

from type_serialize.byte.json import (
    json_bz2_decoder,
    json_bz2_encoder,
    json_gzip_decoder,
    json_gzip_encoder,
    json_lzma_decoder,
    json_lzma_encoder,
    json_zlib_decoder,
    json_zlib_encoder,
)
from type_serialize.byte.msgpack import (
    msgpack_bz2_decoder,
    msgpack_bz2_encoder,
    msgpack_gzip_decoder,
    msgpack_gzip_encoder,
    msgpack_lzma_decoder,
    msgpack_lzma_encoder,
    msgpack_zlib_decoder,
    msgpack_zlib_encoder,
)
from type_serialize.byte.orjson import (
    orjson_bz2_decoder,
    orjson_bz2_encoder,
    orjson_gzip_decoder,
    orjson_gzip_encoder,
    orjson_lzma_decoder,
    orjson_lzma_encoder,
    orjson_zlib_decoder,
    orjson_zlib_encoder,
)
from type_serialize.byte.pickle import pickling5, unpickling
from type_serialize.byte.pyjson import (
    pyjson_bz2_decoder,
    pyjson_bz2_encoder,
    pyjson_gzip_decoder,
    pyjson_gzip_encoder,
    pyjson_lzma_decoder,
    pyjson_lzma_encoder,
    pyjson_zlib_decoder,
    pyjson_zlib_encoder,
)
from type_serialize.driver.json import global_json_byte_decoder as json_byte_decoder
from type_serialize.driver.json import global_json_byte_encoder as json_byte_encoder
from type_serialize.driver.json import orjson_byte_decoder, orjson_byte_encoder
from type_serialize.driver.json import python_json_byte_decoder as pyjson_byte_decoder
from type_serialize.driver.json import python_json_byte_encoder as pyjson_byte_encoder
from type_serialize.driver.msgpack import msgpack_decoder, msgpack_encoder
from type_serialize.variables import COMPRESS_LEVEL_TRADEOFF


@unique
class ByteCodingType(Enum):
    Raw = 0
    Pickle5 = 1

    # Automatically select the installed json library.
    Json = 2
    JsonZlib = 3
    JsonGzip = 4
    JsonLzma = 5
    JsonBz2 = 6

    # System default json library.
    Pyjson = 7
    PyjsonZlib = 8
    PyjsonGzip = 9
    PyjsonLzma = 10
    PyjsonBz2 = 11

    # orjson module
    Orjson = 12
    OrjsonZlib = 13
    OrjsonGzip = 14
    OrjsonLzma = 15
    OrjsonBz2 = 16

    # msgpack module
    Msgpack = 17
    MsgpackZlib = 18
    MsgpackGzip = 19
    MsgpackLzma = 20
    MsgpackBz2 = 21


ObjectToBytesCallable = Callable[..., bytes]
BytesToObjectCallable = Callable[[bytes], Any]


class _ByteCoding:
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


def _unsupported_encode(_: Any) -> bytes:
    raise ValueError("Unsupported encode method")


def _unsupported_decode(_: bytes) -> Any:
    raise ValueError("Unsupported decode method")


_BYTE_CODING_MAP: Final[Dict[ByteCodingType, _ByteCoding]] = {
    ByteCodingType.Raw: _ByteCoding(_unsupported_encode, _unsupported_decode),
    ByteCodingType.Pickle5: _ByteCoding(pickling5, unpickling),
    ByteCodingType.Json: _ByteCoding(json_byte_encoder, json_byte_decoder),
    ByteCodingType.JsonZlib: _ByteCoding(json_zlib_encoder, json_zlib_decoder),
    ByteCodingType.JsonGzip: _ByteCoding(json_gzip_encoder, json_gzip_decoder),
    ByteCodingType.JsonLzma: _ByteCoding(json_lzma_encoder, json_lzma_decoder),
    ByteCodingType.JsonBz2: _ByteCoding(json_bz2_encoder, json_bz2_decoder),
    ByteCodingType.Pyjson: _ByteCoding(pyjson_byte_encoder, pyjson_byte_decoder),
    ByteCodingType.PyjsonZlib: _ByteCoding(pyjson_zlib_encoder, pyjson_zlib_decoder),
    ByteCodingType.PyjsonGzip: _ByteCoding(pyjson_gzip_encoder, pyjson_gzip_decoder),
    ByteCodingType.PyjsonLzma: _ByteCoding(pyjson_lzma_encoder, pyjson_lzma_decoder),
    ByteCodingType.PyjsonBz2: _ByteCoding(pyjson_bz2_encoder, pyjson_bz2_decoder),
    ByteCodingType.Orjson: _ByteCoding(orjson_byte_encoder, orjson_byte_decoder),
    ByteCodingType.OrjsonZlib: _ByteCoding(orjson_zlib_encoder, orjson_zlib_decoder),
    ByteCodingType.OrjsonGzip: _ByteCoding(orjson_gzip_encoder, orjson_gzip_decoder),
    ByteCodingType.OrjsonLzma: _ByteCoding(orjson_lzma_encoder, orjson_lzma_decoder),
    ByteCodingType.OrjsonBz2: _ByteCoding(orjson_bz2_encoder, orjson_bz2_decoder),
    ByteCodingType.Msgpack: _ByteCoding(msgpack_encoder, msgpack_decoder),
    ByteCodingType.MsgpackZlib: _ByteCoding(msgpack_zlib_encoder, msgpack_zlib_decoder),
    ByteCodingType.MsgpackGzip: _ByteCoding(msgpack_gzip_encoder, msgpack_gzip_decoder),
    ByteCodingType.MsgpackLzma: _ByteCoding(msgpack_lzma_encoder, msgpack_lzma_decoder),
    ByteCodingType.MsgpackBz2: _ByteCoding(msgpack_bz2_encoder, msgpack_bz2_decoder),
}

DEFAULT_BYTE_CODING_TYPE: Final[ByteCodingType] = ByteCodingType.JsonGzip


def object_to_bytes(
    coding: ByteCodingType,
    data: Any,
    *,
    level=COMPRESS_LEVEL_TRADEOFF,
) -> bytes:
    return _BYTE_CODING_MAP[coding].encode(data, level=level)


def bytes_to_object(coding: ByteCodingType, data: bytes) -> Any:
    return _BYTE_CODING_MAP[coding].decode(data)
