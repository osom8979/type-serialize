# -*- coding: utf-8 -*-

from datetime import date, datetime, time
from enum import Enum
from typing import Any, Dict, Iterable, List, Mapping, Optional, Tuple

from type_serialize.driver.numpy import HAS_NUMPY, is_ndarray_instance, numpy_serialize
from type_serialize.inspect.member import get_public_instance_attributes
from type_serialize.inspect.types import (
    MAPPING_METHOD_ITEMS,
    MAPPING_METHOD_KEYS,
    is_serializable_pod_obj,
)
from type_serialize.obj.errors import SerializeError
from type_serialize.obj.interface import SERIALIZE_METHOD_NAME, is_serialize_obj


def _create_serialize_dict(items: Iterable[Tuple[Any, Any]]) -> Dict[Any, Any]:
    result: Dict[Any, Any] = dict()
    for key, val in items:
        if val is None:
            continue
        serialize_value = _serialize_any(val, key)
        if serialize_value is None:
            continue
        result[key] = serialize_value
    return result


def _serialize_interface(obj: Any) -> Any:
    return getattr(obj, SERIALIZE_METHOD_NAME)()


def _serialize_mapping(obj: Mapping) -> Dict[Any, Any]:
    items: List[Tuple[str, Any]]
    if hasattr(obj, MAPPING_METHOD_ITEMS):
        items_func = getattr(obj, MAPPING_METHOD_ITEMS)
        items = items_func()
    elif hasattr(obj, MAPPING_METHOD_KEYS):
        keys_func = getattr(obj, MAPPING_METHOD_KEYS)
        items = [(str(k), getattr(obj, str(k))) for k in keys_func()]
    else:
        items = get_public_instance_attributes(obj)
    return _create_serialize_dict(items)


def _serialize_iterable(obj: Iterable) -> List[Any]:
    result: List[Any] = list()
    for i, item in enumerate(obj):
        serialize_value = _serialize_any(item, i)
        if serialize_value is None:
            continue
        result.append(serialize_value)
    return result


def _serialize_common(obj: Any) -> Dict[str, Any]:
    return _create_serialize_dict(get_public_instance_attributes(obj))


def _serialize_any(obj: Any, key: Optional[Any] = None) -> Any:
    try:
        if obj is None:
            return None
        elif HAS_NUMPY and is_ndarray_instance(obj):
            return numpy_serialize(obj)
        elif isinstance(obj, (bytes, bytearray)):
            return obj
        elif isinstance(obj, memoryview):
            return obj.tobytes()
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, time):
            return obj.isoformat()
        elif isinstance(obj, Enum):
            return obj.value
        elif is_serialize_obj(obj):
            return _serialize_interface(obj)
        elif is_serializable_pod_obj(obj):
            return obj
        elif isinstance(obj, Mapping):
            return _serialize_mapping(obj)
        elif isinstance(obj, Iterable):
            return _serialize_iterable(obj)
        else:
            return _serialize_common(obj)
    except SerializeError as e:
        e.insert_first(key)
        raise
    except BaseException as e:
        raise SerializeError(str(e), key) from e


def serialize(obj: Any) -> Any:
    return _serialize_any(obj)
