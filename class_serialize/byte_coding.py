# -*- coding: utf-8 -*-

from enum import Enum, unique
from typing import Any, Final

from class_serialize.byte_json import (
    json_bz2_decoder,
    json_bz2_encoder,
    json_gzip_decoder,
    json_gzip_encoder,
    json_lzma_decoder,
    json_lzma_encoder,
    json_zlib_decoder,
    json_zlib_encoder,
)
from class_serialize.byte_msgpack import (
    msgpack_bz2_decoder,
    msgpack_bz2_encoder,
    msgpack_gzip_decoder,
    msgpack_gzip_encoder,
    msgpack_lzma_decoder,
    msgpack_lzma_encoder,
    msgpack_zlib_decoder,
    msgpack_zlib_encoder,
)
from class_serialize.byte_orjson import (
    orjson_bz2_decoder,
    orjson_bz2_encoder,
    orjson_gzip_decoder,
    orjson_gzip_encoder,
    orjson_lzma_decoder,
    orjson_lzma_encoder,
    orjson_zlib_decoder,
    orjson_zlib_encoder,
)
from class_serialize.byte_pickle import pickling5, unpickling
from class_serialize.byte_pyjson import (
    pyjson_bz2_decoder,
    pyjson_bz2_encoder,
    pyjson_gzip_decoder,
    pyjson_gzip_encoder,
    pyjson_lzma_decoder,
    pyjson_lzma_encoder,
    pyjson_zlib_decoder,
    pyjson_zlib_encoder,
)
from class_serialize.driver.json import (
    global_json_byte_decoder,
    global_json_byte_encoder,
    orjson_byte_decoder,
    orjson_byte_encoder,
    python_json_byte_decoder,
    python_json_byte_encoder,
)
from class_serialize.driver.msgpack import msgpack_decoder, msgpack_encoder
from class_serialize.variables import COMPRESS_LEVEL_TRADEOFF, DEFAULT_PICKLE_ENCODING


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


DEFAULT_BYTE_CODING_TYPE: Final[ByteCodingType] = ByteCodingType.JsonGzip


def object_to_bytes(
    data: Any,
    coding: ByteCodingType,
    *,
    level=COMPRESS_LEVEL_TRADEOFF,
) -> bytes:
    if coding == ByteCodingType.Raw:
        raise ValueError("Unsupported raw coding type")
    elif coding == ByteCodingType.Pickle5:
        return pickling5(data)
    # Auto select JSON
    elif coding == ByteCodingType.Json:
        return global_json_byte_encoder(data)
    elif coding == ByteCodingType.JsonZlib:
        return json_zlib_encoder(data, level)
    elif coding == ByteCodingType.JsonGzip:
        return json_gzip_encoder(data, level)
    elif coding == ByteCodingType.JsonLzma:
        return json_lzma_encoder(data)
    elif coding == ByteCodingType.JsonBz2:
        return json_bz2_encoder(data, level)
    # Python JSON
    elif coding == ByteCodingType.Pyjson:
        return python_json_byte_encoder(data)
    elif coding == ByteCodingType.PyjsonZlib:
        return pyjson_zlib_encoder(data, level)
    elif coding == ByteCodingType.PyjsonGzip:
        return pyjson_gzip_encoder(data, level)
    elif coding == ByteCodingType.PyjsonLzma:
        return pyjson_lzma_encoder(data)
    elif coding == ByteCodingType.PyjsonBz2:
        return pyjson_bz2_encoder(data, level)
    # ORJSON
    elif coding == ByteCodingType.Orjson:
        return orjson_byte_encoder(data)
    elif coding == ByteCodingType.OrjsonZlib:
        return orjson_zlib_encoder(data, level)
    elif coding == ByteCodingType.OrjsonGzip:
        return orjson_gzip_encoder(data, level)
    elif coding == ByteCodingType.OrjsonLzma:
        return orjson_lzma_encoder(data)
    elif coding == ByteCodingType.OrjsonBz2:
        return orjson_bz2_encoder(data, level)
    # MsgPack
    elif coding == ByteCodingType.Msgpack:
        return msgpack_encoder(data)
    elif coding == ByteCodingType.MsgpackZlib:
        return msgpack_zlib_encoder(data, level)
    elif coding == ByteCodingType.MsgpackGzip:
        return msgpack_gzip_encoder(data, level)
    elif coding == ByteCodingType.MsgpackLzma:
        return msgpack_lzma_encoder(data)
    elif coding == ByteCodingType.MsgpackBz2:
        return msgpack_bz2_encoder(data, level)
    raise ValueError(f"Unknown coding type: {coding}")


def bytes_to_object(
    data: bytes,
    coding: ByteCodingType,
    *,
    encoding=DEFAULT_PICKLE_ENCODING,
) -> Any:
    if coding == ByteCodingType.Raw:
        raise ValueError("Unsupported raw coding type")
    elif coding == ByteCodingType.Pickle5:
        return unpickling(data, encoding)
    # Auto select JSON
    elif coding == ByteCodingType.Json:
        return global_json_byte_decoder(data)
    elif coding == ByteCodingType.JsonZlib:
        return json_zlib_decoder(data)
    elif coding == ByteCodingType.JsonGzip:
        return json_gzip_decoder(data)
    elif coding == ByteCodingType.JsonLzma:
        return json_lzma_decoder(data)
    elif coding == ByteCodingType.JsonBz2:
        return json_bz2_decoder(data)
    # Python JSON
    elif coding == ByteCodingType.Pyjson:
        return python_json_byte_decoder(data)
    elif coding == ByteCodingType.PyjsonZlib:
        return pyjson_zlib_decoder(data)
    elif coding == ByteCodingType.PyjsonGzip:
        return pyjson_gzip_decoder(data)
    elif coding == ByteCodingType.PyjsonLzma:
        return pyjson_lzma_decoder(data)
    elif coding == ByteCodingType.PyjsonBz2:
        return pyjson_bz2_decoder(data)
    # ORJSON
    elif coding == ByteCodingType.Orjson:
        return orjson_byte_decoder(data)
    elif coding == ByteCodingType.OrjsonZlib:
        return orjson_zlib_decoder(data)
    elif coding == ByteCodingType.OrjsonGzip:
        return orjson_gzip_decoder(data)
    elif coding == ByteCodingType.OrjsonLzma:
        return orjson_lzma_decoder(data)
    elif coding == ByteCodingType.OrjsonBz2:
        return orjson_bz2_decoder(data)
    # MsgPack
    elif coding == ByteCodingType.Msgpack:
        return msgpack_decoder(data)
    elif coding == ByteCodingType.MsgpackZlib:
        return msgpack_zlib_decoder(data)
    elif coding == ByteCodingType.MsgpackGzip:
        return msgpack_gzip_decoder(data)
    elif coding == ByteCodingType.MsgpackLzma:
        return msgpack_lzma_decoder(data)
    elif coding == ByteCodingType.MsgpackBz2:
        return msgpack_bz2_decoder(data)
    raise ValueError(f"Unknown coding type: {coding}")
