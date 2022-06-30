# -*- coding: utf-8 -*-

from enum import Enum
from typing import List
from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize


class Sample(Enum):
    Value0 = 0
    Value1 = 1
    Value2 = 2


class DeserializeEnumTestCase(TestCase):
    def test_enum(self):
        result = deserialize([0, 1, 2], List[Sample])
        self.assertIsInstance(result, list)
        self.assertEqual(3, len(result))
        self.assertIsInstance(result[0], Sample)
        self.assertIsInstance(result[1], Sample)
        self.assertIsInstance(result[2], Sample)
        self.assertEqual(result[0], Sample.Value0)
        self.assertEqual(result[1], Sample.Value1)
        self.assertEqual(result[2], Sample.Value2)


if __name__ == "__main__":
    main()
