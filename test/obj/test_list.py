# -*- coding: utf-8 -*-

from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize
from type_serialize.obj.serialize import serialize


class ListTestCase(TestCase):
    def test_list(self):
        data = serialize([1, 2, 3])
        self.assertIsInstance(data, list)
        self.assertListEqual([1, 2, 3], data)

        result = deserialize(data, list)
        self.assertIsInstance(result, list)
        self.assertListEqual(result, [1, 2, 3])


if __name__ == "__main__":
    main()
