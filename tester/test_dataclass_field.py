# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import Optional
from unittest import TestCase, main

from type_serialize.deserialize import deserialize
from type_serialize.serialize import serialize


@dataclass
class FieldSample:
    test1: str
    test2: Optional[str] = None
    test3: str = "A"
    test4: str = field(default_factory=str)
    test5: str = field(default="B")
    test6: str = field(default_factory=lambda: None)  # type: ignore[assignment]


class DataclassFieldTestCase(TestCase):
    def test_dataclass(self):
        test = FieldSample(test1="aa")
        data = serialize(test)
        self.assertEqual({"test1": "aa", "test3": "A", "test4": "", "test5": "B"}, data)

        result = deserialize({"test1": "aa"}, FieldSample)
        self.assertIsInstance(result, FieldSample)
        self.assertEqual("aa", result.test1)
        self.assertIsNone(result.test2)
        self.assertEqual("A", result.test3)
        self.assertEqual("", result.test4)
        self.assertEqual("B", result.test5)
        self.assertIsNone(result.test6)


if __name__ == "__main__":
    main()
