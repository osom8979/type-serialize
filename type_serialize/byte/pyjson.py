# -*- coding: utf-8 -*-

import bz2
import gzip
import lzma
import zlib
from typing import Any

from type_serialize.driver.json import (
    python_json_byte_decoder,
    python_json_byte_encoder,
)
from type_serialize.variables import COMPRESS_LEVEL_BEST


def pyjson_zlib_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 0 <= level <= 9 or level == -1
    return zlib.compress(python_json_byte_encoder(data), level=level)


def pyjson_zlib_decoder(data: bytes) -> Any:
    return python_json_byte_decoder(zlib.decompress(data))


def pyjson_gzip_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 0 <= level <= 9
    return gzip.compress(python_json_byte_encoder(data), compresslevel=level)


def pyjson_gzip_decoder(data: bytes) -> Any:
    return python_json_byte_decoder(gzip.decompress(data))


def pyjson_lzma_encoder(data: Any) -> bytes:
    return lzma.compress(python_json_byte_encoder(data))


def pyjson_lzma_decoder(data: bytes) -> Any:
    return python_json_byte_decoder(lzma.decompress(data))


def pyjson_bz2_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 1 <= level <= 9
    return bz2.compress(python_json_byte_encoder(data), compresslevel=level)


def pyjson_bz2_decoder(data: bytes) -> Any:
    return python_json_byte_decoder(bz2.decompress(data))
