# -*- coding: utf-8 -*-

from typing import Any, Final, Iterable, Mapping

MAPPING_METHOD_ITEMS: Final[str] = "items"
MAPPING_METHOD_KEYS: Final[str] = "keys"
SEQUENCE_METHOD_INSERT: Final[str] = "insert"


def is_serializable_pod_cls(cls: Any) -> bool:
    if not isinstance(cls, type):
        return False
    return issubclass(cls, int) or issubclass(cls, float) or issubclass(cls, str)


def is_serializable_pod_obj(obj: Any) -> bool:
    if isinstance(obj, type):
        return False
    return isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, str)


def is_none(obj: Any) -> bool:
    if isinstance(obj, type):
        return issubclass(obj, type(None))
    else:
        return obj is None


def is_bytes(obj: Any) -> bool:
    if isinstance(obj, type):
        return issubclass(obj, bytes)
    else:
        return isinstance(obj, bytes)


def is_bytearray(obj: Any) -> bool:
    if isinstance(obj, type):
        return issubclass(obj, bytearray)
    else:
        return isinstance(obj, bytearray)


def compatible_iterable(data: Any) -> bool:
    assert not isinstance(data, bytes)
    assert not isinstance(data, bytearray)

    if isinstance(data, Mapping):
        return False
    elif isinstance(data, str):
        return False
    return isinstance(data, Iterable)
