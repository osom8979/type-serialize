# -*- coding: utf-8 -*-

from typing import List, NamedTuple
from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize


class Sample(NamedTuple):
    shape: List[int]
    dtype: str
    buffer: bytes
    strides: List[int]


class DeserializeTupleTestCase(TestCase):
    def test_tuple(self):
        buffer = bytearray(b"abcd")
        result = deserialize([[1], "int8", buffer, [2]], Sample)
        self.assertIsInstance(result, Sample)
        self.assertEqual([1], result.shape)
        self.assertEqual("int8", result.dtype)
        self.assertEqual(b"abcd", result.buffer)
        self.assertEqual([2], result.strides)


if __name__ == "__main__":
    main()
