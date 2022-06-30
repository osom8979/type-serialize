# -*- coding: utf-8 -*-

import pickle
from typing import Any

from type_serialize.variables import (
    DEFAULT_PICKLE_ENCODING,
    DEFAULT_PICKLE_PROTOCOL_VERSION,
)


def pickling(data: Any, protocol=DEFAULT_PICKLE_PROTOCOL_VERSION) -> bytes:
    return pickle.dumps(data, protocol=protocol)


def pickling5(data: Any) -> bytes:
    return pickle.dumps(data, protocol=5)


def unpickling(data: bytes, encoding=DEFAULT_PICKLE_ENCODING) -> Any:
    return pickle.loads(data, encoding=encoding)
