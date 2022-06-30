# -*- coding: utf-8 -*-

from dataclasses import dataclass
from unittest import TestCase, main

from type_serialize.obj.serialize import serialize


@dataclass
class Sample:
    test1: bytes


class SerializeByteTestCase(TestCase):
    def test_byte(self):
        test = b"abcd"
        self.assertEqual(test, serialize(test))

    def test_byte_member(self):
        test = Sample(b"abcd")
        data = serialize(test)
        result = {"test1": b"abcd"}
        self.assertEqual(result, data)


if __name__ == "__main__":
    main()
