# -*- coding: utf-8 -*-

from typing import Any, Optional

from type_serialize.byte.byte_coder import DEFAULT_BYTE_CODING_TYPE, bytes_to_object
from type_serialize.obj.deserialize import deserialize


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
