# -*- coding: utf-8 -*-

from typing import Optional


class _Error(BaseException):
    def __init__(self, msg: str, key: Optional[str] = None):
        self.msg = msg
        self.key = key if key else str()

    def insert_first(self, key: Optional[str]) -> None:
        if not key:
            return
        if self.key:
            self.key = key + "." + self.key
        else:
            self.key = key


class SerializeError(_Error):
    def __init__(self, msg: str, key: Optional[str] = None):
        super().__init__(msg, key if key else "")


class DeserializeError(_Error):
    def __init__(self, msg: str, key: Optional[str] = None):
        super().__init__(msg, key if key else "")
