# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from typing import Any


class SerializeInterface(metaclass=ABCMeta):
    @abstractmethod
    def __serialize__(self) -> Any:
        raise NotImplementedError


class DeserializeInterface(metaclass=ABCMeta):
    @abstractmethod
    def __deserialize__(self, data: Any) -> None:
        raise NotImplementedError


SERIALIZE_METHOD_NAME = SerializeInterface.__serialize__.__name__
DESERIALIZE_METHOD_NAME = DeserializeInterface.__deserialize__.__name__


class Serializable(SerializeInterface, DeserializeInterface):
    def __serialize__(self) -> Any:
        raise NotImplementedError

    def __deserialize__(self, data: Any) -> None:
        raise NotImplementedError


def is_serialize_cls(cls: Any) -> bool:
    if not isinstance(cls, type):
        return False
    if issubclass(cls, SerializeInterface):
        return True
    return hasattr(cls, SERIALIZE_METHOD_NAME)


def is_serialize_obj(obj: Any) -> bool:
    if isinstance(obj, type):
        return False
    if isinstance(obj, SerializeInterface):
        return True
    return hasattr(obj, SERIALIZE_METHOD_NAME)


def is_deserialize_cls(cls: Any) -> bool:
    if not isinstance(cls, type):
        return False
    if issubclass(cls, DeserializeInterface):
        return True
    return hasattr(cls, DESERIALIZE_METHOD_NAME)


def is_deserialize_obj(obj: Any) -> bool:
    if isinstance(obj, type):
        return False
    if isinstance(obj, DeserializeInterface):
        return True
    return hasattr(obj, DESERIALIZE_METHOD_NAME)
