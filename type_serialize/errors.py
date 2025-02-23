# -*- coding: utf-8 -*-

from typing import Any, Optional


class TypeSerializeError(Exception):
    def __init__(self, msg: str, key: Optional[Any] = None):
        self.msg = msg
        self.key = str(key) if key else str()

    def insert_first(self, key: Any) -> None:
        if not key:
            return
        if self.key:
            self.key = str(key) + "." + self.key
        else:
            self.key = str(key)


class SerializeError(TypeSerializeError):
    def __init__(self, msg: str, key: Optional[Any] = None):
        super().__init__(msg, str(key) if key else str())


class DeserializeError(TypeSerializeError):
    def __init__(self, msg: str, key: Optional[Any] = None):
        super().__init__(msg, str(key) if key else str())
