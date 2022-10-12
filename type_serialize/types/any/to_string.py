# -*- coding: utf-8 -*-

from typing import Any, List


def any_to_strings(obj: Any) -> List[str]:
    if isinstance(obj, str):
        return [obj]
    elif isinstance(obj, set) or isinstance(obj, list):
        result = list()
        for oo in obj:
            for o in any_to_strings(oo):
                result.append(o)
        return result
    elif isinstance(obj, dict):
        result = list()
        for key, value in obj.items():
            result.append(f"{key}={value}")
        return result
    else:
        return [str(obj)]
