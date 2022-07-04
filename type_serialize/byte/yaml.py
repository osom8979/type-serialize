# -*- coding: utf-8 -*-

import bz2
import gzip
import lzma
import zlib
from typing import Any

from type_serialize.driver.yaml import yaml_decoder, yaml_encoder
from type_serialize.variables import COMPRESS_LEVEL_BEST


def yaml_zlib_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 0 <= level <= 9 or level == -1
    return zlib.compress(yaml_encoder(data), level=level)


def yaml_zlib_decoder(data: bytes) -> Any:
    return yaml_decoder(zlib.decompress(data))


def yaml_gzip_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 0 <= level <= 9
    return gzip.compress(yaml_encoder(data), compresslevel=level)


def yaml_gzip_decoder(data: bytes) -> Any:
    return yaml_decoder(gzip.decompress(data))


def yaml_lzma_encoder(data: Any) -> bytes:
    return lzma.compress(yaml_encoder(data))


def yaml_lzma_decoder(data: bytes) -> Any:
    return yaml_decoder(lzma.decompress(data))


def yaml_bz2_encoder(data: Any, level=COMPRESS_LEVEL_BEST) -> bytes:
    assert 1 <= level <= 9
    return bz2.compress(yaml_encoder(data), compresslevel=level)


def yaml_bz2_decoder(data: bytes) -> Any:
    return yaml_decoder(bz2.decompress(data))
