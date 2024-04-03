# -*- coding: utf-8 -*-

from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize
from type_serialize.obj.serialize import serialize


class TupleTestCase(TestCase):
    def test_tuple(self):
        test = [1, 2], "uint8", bytearray(b"abcd"), []
        data = serialize(test)
        self.assertEqual([[1, 2], "uint8", b"abcd", []], data)

        result = deserialize(data, tuple)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 4)
        self.assertEqual([1, 2], result[0])
        self.assertEqual("uint8", result[1])
        self.assertEqual(b"abcd", result[2])
        self.assertListEqual([], result[3])


if __name__ == "__main__":
    main()
