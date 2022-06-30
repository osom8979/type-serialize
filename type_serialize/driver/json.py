# -*- coding: utf-8 -*-

import json
import os
from typing import Any, Callable

try:
    import orjson  # noqa
except ImportError:
    HAS_ORJSON = False
else:
    HAS_ORJSON = True

from type_serialize.conversion.to_boolean import string_to_boolean
from type_serialize.variables import DISABLE_ORJSON_INSTALL_ENV_NAME

JsonByteEncoder = Callable[[Any], bytes]
JsonByteDecoder = Callable[[bytes], Any]
JsonEncoder = Callable[[Any], str]
JsonDecoder = Callable[[str], Any]


def python_json_byte_encoder(data: Any) -> bytes:
    return json.dumps(data).encode("utf-8")


def python_json_byte_decoder(data: bytes) -> Any:
    return json.loads(data)


def python_json_encoder(data: Any) -> str:
    return json.dumps(data)


def python_json_decoder(data: str) -> Any:
    return json.loads(data)


def valid_orjson_module():
    if not HAS_ORJSON:
        raise ModuleNotFoundError("orjson module not found")


def orjson_byte_encoder(data: Any) -> bytes:
    valid_orjson_module()
    return orjson.dumps(data)


def orjson_byte_decoder(data: bytes) -> Any:
    valid_orjson_module()
    return orjson.loads(data)


def orjson_encoder(data: Any) -> str:
    valid_orjson_module()
    return str(orjson.dumps(data), "utf-8")


def orjson_decoder(data: str) -> Any:
    valid_orjson_module()
    return orjson.loads(data)


_global_json_byte_encoder: JsonByteEncoder = python_json_byte_encoder
_global_json_byte_decoder: JsonByteDecoder = python_json_byte_decoder
_global_json_encoder: JsonEncoder = python_json_encoder
_global_json_decoder: JsonDecoder = python_json_decoder


def global_json_byte_encoder(data: Any) -> bytes:
    return _global_json_byte_encoder(data)


def global_json_byte_decoder(data: bytes) -> Any:
    return _global_json_byte_decoder(data)


def global_json_encoder(data: Any) -> str:
    return _global_json_encoder(data)


def global_json_decoder(data: str) -> Any:
    return _global_json_decoder(data)


def install_orjson_driver():
    global _global_json_byte_encoder
    global _global_json_byte_decoder
    global _global_json_encoder
    global _global_json_decoder

    _global_json_byte_encoder = orjson_byte_encoder
    _global_json_byte_decoder = orjson_byte_decoder
    _global_json_encoder = orjson_encoder
    _global_json_decoder = orjson_decoder


def is_auto_install() -> bool:
    if DISABLE_ORJSON_INSTALL_ENV_NAME in os.environ:
        value = os.environ[DISABLE_ORJSON_INSTALL_ENV_NAME]
        if value and string_to_boolean(value):
            return False
    return HAS_ORJSON


if is_auto_install():
    install_orjson_driver()
