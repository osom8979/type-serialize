# -*- coding: utf-8 -*-

from unittest import TestCase, main

from type_serialize.obj.serialize import serialize


class SerializeListTestCase(TestCase):
    def test_list(self):
        data = serialize([1, 2, 3])
        self.assertIsInstance(data, list)
        self.assertListEqual([1, 2, 3], data)


if __name__ == "__main__":
    main()
