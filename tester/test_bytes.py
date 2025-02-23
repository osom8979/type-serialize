# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import List, Optional
from unittest import TestCase, main

from type_serialize.deserialize import deserialize
from type_serialize.serialize import serialize


@dataclass
class BytesSample:
    a: bytes


@dataclass
class OptionalListBytesSample:
    a: Optional[List[bytes]] = None


class ByteTestCase(TestCase):
    def test_bytes(self):
        test = b"abcd"
        self.assertEqual(test, serialize(test))
        self.assertEqual(test, deserialize(test))

    def test_bytes_member(self):
        test = BytesSample(b"abcd")
        data = serialize(test)
        self.assertEqual({"a": b"abcd"}, data)

        result = deserialize(data, BytesSample)
        self.assertIsInstance(result, BytesSample)
        self.assertEqual(b"abcd", result.a)

    def test_none_list_bytes_member(self):
        test = OptionalListBytesSample()
        data = serialize(test)
        self.assertEqual({}, data)

        result = deserialize(data, OptionalListBytesSample)
        self.assertIsInstance(result, OptionalListBytesSample)
        self.assertEqual(None, result.a)

    def test_list_bytes_member(self):
        test = OptionalListBytesSample([b"abcd"])
        data = serialize(test)
        self.assertEqual({"a": [b"abcd"]}, data)

        result = deserialize(data, OptionalListBytesSample)
        self.assertIsInstance(result, OptionalListBytesSample)
        self.assertListEqual([b"abcd"], result.a)


if __name__ == "__main__":
    main()
