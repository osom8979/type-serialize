# -*- coding: utf-8 -*-

from type_serialize.decode import decode
from type_serialize.encode import encode
from type_serialize.obj.deserialize import deserialize
from type_serialize.obj.serialize import serialize

__version__ = "0.0.1"

__all__ = (
    "__version__",
    "decode",
    "encode",
    "deserialize",
    "serialize",
)
