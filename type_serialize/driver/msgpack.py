# -*- coding: utf-8 -*-

from typing import Any

try:
    import msgpack  # noqa
except ImportError:
    HAS_MSGPACK = False
else:
    HAS_MSGPACK = True


def valid_msgpack_module():
    if not HAS_MSGPACK:
        raise ModuleNotFoundError("MsgPack module not found")


def msgpack_encoder(data: Any) -> bytes:
    valid_msgpack_module()
    return msgpack.dumps(data)


def msgpack_decoder(data: bytes) -> Any:
    valid_msgpack_module()
    return msgpack.loads(data)
