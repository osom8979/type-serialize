# -*- coding: utf-8 -*-

from typing import List, Optional
from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize


class Sample:
    a: int
    b: float
    c: str

    def __init__(self):
        pass


class DeserializeHintTestCase(TestCase):
    def test_hint(self):
        data = [{"a": 2}]
        result = deserialize(data, Optional[List[Sample]])
        self.assertIsInstance(result, list)
        self.assertEqual(1, len(result))
        self.assertEqual(2, result[0].a)


if __name__ == "__main__":
    main()
