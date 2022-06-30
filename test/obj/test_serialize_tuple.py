# -*- coding: utf-8 -*-

from typing import List, NamedTuple
from unittest import TestCase, main

from type_serialize.obj.serialize import serialize


class Sample(NamedTuple):
    shape: List[int]
    dtype: str
    buffer: bytes
    strides: List[int]


class SerializeTupleTestCase(TestCase):
    def test_tuple(self):
        test = Sample([1, 2], "uint8", b"abcd", [])
        data = serialize(test)
        result = [[1, 2], "uint8", b"abcd", []]
        self.assertEqual(result, data)


if __name__ == "__main__":
    main()
