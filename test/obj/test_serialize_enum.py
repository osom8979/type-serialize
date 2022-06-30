# -*- coding: utf-8 -*-

from enum import Enum
from unittest import TestCase, main

from type_serialize.obj.serialize import serialize


class Sample(Enum):
    Value0 = 0
    Value1 = 1
    Value2 = 2


class SerializeEnumTestCase(TestCase):
    def test_enum(self):
        data1 = serialize(Sample.Value0)
        self.assertIsInstance(data1, int)
        self.assertEqual(0, data1)

        data2 = serialize([Sample.Value0, Sample.Value1, Sample.Value2])
        self.assertIsInstance(data2, list)
        self.assertListEqual([0, 1, 2], data2)


if __name__ == "__main__":
    main()
