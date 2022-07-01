# -*- coding: utf-8 -*-

from type_serialize.byte.byte_coding import ByteCodingType
from type_serialize.decode import decode
from type_serialize.encode import encode
from type_serialize.obj.deserialize import deserialize
from type_serialize.obj.serialize import serialize

__version__ = "1.0.1"

__all__ = (
    "__version__",
    "ByteCodingType",
    "decode",
    "encode",
    "deserialize",
    "serialize",
)
