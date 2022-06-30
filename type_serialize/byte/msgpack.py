# -*- coding: utf-8 -*-

import bz2
import gzip
import lzma
import zlib
from typing import Any

from type_serialize.driver.msgpack import msgpack_decoder, msgpack_encoder
from type_serialize.variables import COMPRESS_LEVEL_BEST


def msgpack_zlib_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 0 <= level <= 9 or level == -1
    return zlib.compress(msgpack_encoder(data), level=level)


def msgpack_zlib_decoder(data: bytes) -> Any:
    return msgpack_decoder(zlib.decompress(data))


def msgpack_gzip_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 0 <= level <= 9
    return gzip.compress(msgpack_encoder(data), compresslevel=level)


def msgpack_gzip_decoder(data: bytes) -> Any:
    return msgpack_decoder(gzip.decompress(data))


def msgpack_lzma_encoder(data: Any) -> bytes:
    return lzma.compress(msgpack_encoder(data))


def msgpack_lzma_decoder(data: bytes) -> Any:
    return msgpack_decoder(lzma.decompress(data))


def msgpack_bz2_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 1 <= level <= 9
    return bz2.compress(msgpack_encoder(data), compresslevel=level)


def msgpack_bz2_decoder(data: bytes) -> Any:
    return msgpack_decoder(bz2.decompress(data))
