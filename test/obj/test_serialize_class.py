# -*- coding: utf-8 -*-

from unittest import TestCase, main

from type_serialize.obj.serialize import serialize


class Sample:
    def __init__(self):
        self.name = "test0"
        self.data1 = 0
        self.data2 = 1.1
        self.data3 = [1, 2, 3, 4]
        self.data4 = {"a": 0, "b": 1.2, "c": "?"}


class SerializeClassTestCase(TestCase):
    def test_class(self):
        test = Sample()
        data = serialize(test)
        result = {
            "name": "test0",
            "data1": 0,
            "data2": 1.1,
            "data3": [1, 2, 3, 4],
            "data4": {"a": 0, "b": 1.2, "c": "?"},
        }
        self.assertEqual(result, data)


if __name__ == "__main__":
    main()
