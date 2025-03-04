# -*- coding: utf-8 -*-

from type_serialize.deserialize import deserialize
from type_serialize.interface import Serializable
from type_serialize.serialize import serialize

__version__ = "2.1.0"

__all__ = (
    "__version__",
    "Serializable",
    "deserialize",
    "serialize",
)
