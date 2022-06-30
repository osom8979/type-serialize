# -*- coding: utf-8 -*-

from dataclasses import dataclass
from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize


@dataclass
class Sample:
    test1: bytes


class DeserializeByteTestCase(TestCase):
    def test_byte(self):
        result = deserialize({"test1": b"abcd"}, Sample)
        self.assertIsInstance(result, Sample)
        self.assertEqual(b"abcd", result.test1)


if __name__ == "__main__":
    main()
