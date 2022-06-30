# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional
from unittest import TestCase, main

from type_serialize.obj.serialize import serialize


@dataclass
class Sample:
    test1: str
    test2: Optional[str] = None

    @property
    def test3(self):
        assert self
        return 30

    def test4(self):
        assert self
        return 40


class SerializeDataclassTestCase(TestCase):
    def test_dataclass(self):
        test = Sample("aa")
        data = serialize(test)
        result = {"test1": "aa"}
        self.assertEqual(result, data)


if __name__ == "__main__":
    main()
