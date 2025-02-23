# -*- coding: utf-8 -*-

from enum import Enum
from typing import List
from unittest import TestCase, main

from type_serialize.deserialize import deserialize
from type_serialize.serialize import serialize


class Sample(Enum):
    Value0 = 0
    Value1 = 1
    Value2 = 2


class EnumTestCase(TestCase):
    def test_enum(self):
        data = serialize(Sample.Value0)
        self.assertIsInstance(data, int)
        self.assertEqual(0, data)

        result = deserialize(data, Sample)
        self.assertIsInstance(result, Sample)
        self.assertEqual(result, Sample.Value0)

    def test_enum_list(self):
        data = serialize([Sample.Value0, Sample.Value1, Sample.Value2])
        self.assertIsInstance(data, list)
        self.assertListEqual([0, 1, 2], data)

        result = deserialize(data, List[Sample])
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
