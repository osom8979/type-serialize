# -*- coding: utf-8 -*-

from typing import Dict, List
from unittest import TestCase, main

from type_serialize.deserialize import deserialize
from type_serialize.serialize import serialize


class ListTestCase(TestCase):
    def test_list(self):
        data = serialize([1, 2, 3])
        self.assertIsInstance(data, list)
        self.assertListEqual([1, 2, 3], data)

        result = deserialize(data, list)
        self.assertIsInstance(result, list)
        self.assertListEqual(result, [1, 2, 3])

    def test_list_list(self):
        data = serialize([[1, 2, 3]])
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], list)
        self.assertListEqual([1, 2, 3], data[0])

        result = deserialize(data, List[List[int]])
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], list)
        self.assertListEqual(result[0], [1, 2, 3])

    def test_list_dict(self):
        data = serialize([{1: "A", 2: "B", 3: "C"}])
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)
        self.assertDictEqual({1: "A", 2: "B", 3: "C"}, data[0])

        result = deserialize(data, List[Dict[int, str]])
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)
        self.assertDictEqual(result[0], {1: "A", 2: "B", 3: "C"})


if __name__ == "__main__":
    main()
