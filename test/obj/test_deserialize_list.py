# -*- coding: utf-8 -*-

from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize


class DeserializeListTestCase(TestCase):
    def test_list(self):
        result = deserialize([1, 2, 3], list)
        self.assertIsInstance(result, list)
        self.assertListEqual(result, [1, 2, 3])


if __name__ == "__main__":
    main()
