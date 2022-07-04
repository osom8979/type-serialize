# -*- coding: utf-8 -*-

from typing import Any, Dict, Final

from type_serialize.byte.byte_coding import ByteCoding
from type_serialize.byte.byte_coding_pair import ByteCodingPair
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
from type_serialize.byte.yaml import (
    yaml_bz2_decoder,
    yaml_bz2_encoder,
    yaml_gzip_decoder,
    yaml_gzip_encoder,
    yaml_lzma_decoder,
    yaml_lzma_encoder,
    yaml_zlib_decoder,
    yaml_zlib_encoder,
)
from type_serialize.driver.json import global_json_byte_decoder as json_byte_decoder
from type_serialize.driver.json import global_json_byte_encoder as json_byte_encoder
from type_serialize.driver.json import orjson_byte_decoder, orjson_byte_encoder
from type_serialize.driver.json import python_json_byte_decoder as pyjson_byte_decoder
from type_serialize.driver.json import python_json_byte_encoder as pyjson_byte_encoder
from type_serialize.driver.msgpack import msgpack_decoder, msgpack_encoder
from type_serialize.driver.yaml import yaml_decoder, yaml_encoder


def _unsupported_encode(_: Any) -> bytes:
    raise ValueError("Unsupported encode method")


def _unsupported_decode(_: bytes) -> Any:
    raise ValueError("Unsupported decode method")


BYTE_CODING_MAP: Final[Dict[ByteCoding, ByteCodingPair]] = {
    ByteCoding.Raw: ByteCodingPair(_unsupported_encode, _unsupported_decode),
    ByteCoding.Pickle5: ByteCodingPair(pickling5, unpickling),
    ByteCoding.Json: ByteCodingPair(json_byte_encoder, json_byte_decoder),
    ByteCoding.JsonZlib: ByteCodingPair(json_zlib_encoder, json_zlib_decoder),
    ByteCoding.JsonGzip: ByteCodingPair(json_gzip_encoder, json_gzip_decoder),
    ByteCoding.JsonLzma: ByteCodingPair(json_lzma_encoder, json_lzma_decoder),
    ByteCoding.JsonBz2: ByteCodingPair(json_bz2_encoder, json_bz2_decoder),
    ByteCoding.Pyjson: ByteCodingPair(pyjson_byte_encoder, pyjson_byte_decoder),
    ByteCoding.PyjsonZlib: ByteCodingPair(pyjson_zlib_encoder, pyjson_zlib_decoder),
    ByteCoding.PyjsonGzip: ByteCodingPair(pyjson_gzip_encoder, pyjson_gzip_decoder),
    ByteCoding.PyjsonLzma: ByteCodingPair(pyjson_lzma_encoder, pyjson_lzma_decoder),
    ByteCoding.PyjsonBz2: ByteCodingPair(pyjson_bz2_encoder, pyjson_bz2_decoder),
    ByteCoding.Orjson: ByteCodingPair(orjson_byte_encoder, orjson_byte_decoder),
    ByteCoding.OrjsonZlib: ByteCodingPair(orjson_zlib_encoder, orjson_zlib_decoder),
    ByteCoding.OrjsonGzip: ByteCodingPair(orjson_gzip_encoder, orjson_gzip_decoder),
    ByteCoding.OrjsonLzma: ByteCodingPair(orjson_lzma_encoder, orjson_lzma_decoder),
    ByteCoding.OrjsonBz2: ByteCodingPair(orjson_bz2_encoder, orjson_bz2_decoder),
    ByteCoding.Msgpack: ByteCodingPair(msgpack_encoder, msgpack_decoder),
    ByteCoding.MsgpackZlib: ByteCodingPair(msgpack_zlib_encoder, msgpack_zlib_decoder),
    ByteCoding.MsgpackGzip: ByteCodingPair(msgpack_gzip_encoder, msgpack_gzip_decoder),
    ByteCoding.MsgpackLzma: ByteCodingPair(msgpack_lzma_encoder, msgpack_lzma_decoder),
    ByteCoding.MsgpackBz2: ByteCodingPair(msgpack_bz2_encoder, msgpack_bz2_decoder),
    ByteCoding.Yaml: ByteCodingPair(yaml_encoder, yaml_decoder),
    ByteCoding.YamlZlib: ByteCodingPair(yaml_zlib_encoder, yaml_zlib_decoder),
    ByteCoding.YamlGzip: ByteCodingPair(yaml_gzip_encoder, yaml_gzip_decoder),
    ByteCoding.YamlLzma: ByteCodingPair(yaml_lzma_encoder, yaml_lzma_decoder),
    ByteCoding.YamlBz2: ByteCodingPair(yaml_bz2_encoder, yaml_bz2_decoder),
}
