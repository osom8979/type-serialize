# -*- coding: utf-8 -*-

import bz2
import gzip
import lzma
import zlib
from typing import Any

from type_serialize.driver.json import orjson_byte_decoder, orjson_byte_encoder
from type_serialize.variables import COMPRESS_LEVEL_BEST


def orjson_zlib_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 0 <= level <= 9 or level == -1
    return zlib.compress(orjson_byte_encoder(data), level=level)


def orjson_zlib_decoder(data: bytes) -> Any:
    return orjson_byte_decoder(zlib.decompress(data))


def orjson_gzip_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 0 <= level <= 9
    return gzip.compress(orjson_byte_encoder(data), compresslevel=level)


def orjson_gzip_decoder(data: bytes) -> Any:
    return orjson_byte_decoder(gzip.decompress(data))


def orjson_lzma_encoder(data: Any) -> bytes:
    return lzma.compress(orjson_byte_encoder(data))


def orjson_lzma_decoder(data: bytes) -> Any:
    return orjson_byte_decoder(lzma.decompress(data))


def orjson_bz2_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 1 <= level <= 9
    return bz2.compress(orjson_byte_encoder(data), compresslevel=level)


def orjson_bz2_decoder(data: bytes) -> Any:
    return orjson_byte_decoder(bz2.decompress(data))
