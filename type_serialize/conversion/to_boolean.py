# -*- coding: utf-8 -*-

TRUE_LOWERS = [
    "y",
    "yes",
    "true",
    "on",
    "1",
]
FALSE_LOWERS = [
    "n",
    "no",
    "false",
    "off",
    "0",
]


def string_to_boolean(value: str) -> bool:
    v = value.lower()
    if v in TRUE_LOWERS:
        return True
    elif v in FALSE_LOWERS:
        return False
    raise ValueError(f"could not convert string to bool: '{value}'")
