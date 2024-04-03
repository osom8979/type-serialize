# -*- coding: utf-8 -*-

from typing import List, NamedTuple
from unittest import TestCase, main

# from type_serialize.obj.deserialize import deserialize
from type_serialize.obj.serialize import serialize


class Sample(NamedTuple):
    shape: List[int]
    dtype: str
    buffer: bytes
    strides: List[int]


class TupleTestCase(TestCase):
    def test_tuple(self):
        test = Sample([1, 2], "uint8", bytearray(b"abcd"), [])
        data = serialize(test)
        self.assertEqual([[1, 2], "uint8", b"abcd", []], data)

        # result = deserialize(data, Sample)
        # self.assertIsInstance(result, Sample)
        # self.assertEqual([1, 2], result.shape)
        # self.assertEqual("uint8", result.dtype)
        # self.assertEqual(b"abcd", result.buffer)
        # self.assertListEqual([], result.strides)


if __name__ == "__main__":
    main()
