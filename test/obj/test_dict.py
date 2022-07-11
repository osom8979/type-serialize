# -*- coding: utf-8 -*-

from typing import Dict, List
from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize
from type_serialize.obj.serialize import serialize


class DictTestCase(TestCase):
    def test_dict(self):
        data = serialize({1: "A", 2: "B"})
        self.assertIsInstance(data, dict)
        self.assertDictEqual({1: "A", 2: "B"}, data)

        result = deserialize(data, dict)
        self.assertIsInstance(result, dict)
        self.assertDictEqual(result, {1: "A", 2: "B"})

    def test_dict_dict(self):
        data = serialize({1: {2: "B"}})
        self.assertIsInstance(data, dict)
        self.assertIsInstance(data[1], dict)
        self.assertDictEqual({2: "B"}, data[1])

        result = deserialize(data, Dict[int, Dict[int, str]])
        self.assertIsInstance(result, dict)
        self.assertIsInstance(result[1], dict)
        self.assertDictEqual(result[1], {2: "B"})

    def test_dict_list(self):
        data = serialize({1: [2, 3]})
        self.assertIsInstance(data, dict)
        self.assertIsInstance(data[1], list)
        self.assertListEqual([2, 3], data[1])

        result = deserialize(data, Dict[int, List[int]])
        self.assertIsInstance(result, dict)
        self.assertIsInstance(result[1], list)
        self.assertListEqual(result[1], [2, 3])


if __name__ == "__main__":
    main()
