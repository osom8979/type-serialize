# -*- coding: utf-8 -*-

from inspect import Parameter, signature
from typing import List, Type, TypeVar

_T = TypeVar("_T")


def required_init_parameters(cls: Type[_T]) -> List[str]:
    sig = signature(cls.__init__)
    result = list()
    param_keys = list(sig.parameters.keys())
    for key in param_keys[1:]:  # first is 'self'
        param = sig.parameters[key]
        if param.kind != Parameter.POSITIONAL_OR_KEYWORD:
            break
        if param.default != Parameter.empty:
            break
        result.append(key)
    return result
