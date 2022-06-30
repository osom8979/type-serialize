# -*- coding: utf-8 -*-

from typing import Any

from type_serialize.conversion.to_boolean import string_to_boolean


def string_to_any(data: str, cls: Any) -> Any:
    assert isinstance(cls, type)

    # [IMPORTANT]
    # Do not change if-else order (Reason: `issubclass(bool, int) == True`)
    if cls == str:
        return data
    elif cls == bool:
        return string_to_boolean(data)
    elif cls == int:
        return int(data)
    elif cls == float:
        return float(data)

    return cls(data)  # type: ignore[call-arg]
