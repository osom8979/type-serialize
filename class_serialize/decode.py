# -*- coding: utf-8 -*-

from typing import Any, Optional

from class_serialize.byte.byte_coding import DEFAULT_BYTE_CODING_TYPE, bytes_to_object
from class_serialize.obj.deserialize import deserialize


def decode(
    data: bytes,
    cls: Optional[Any] = None,
    coding=DEFAULT_BYTE_CODING_TYPE,
) -> Any:
    obj = bytes_to_object(coding=coding, data=data)
    if cls is not None:
        return deserialize(obj, cls)
    else:
        return obj
