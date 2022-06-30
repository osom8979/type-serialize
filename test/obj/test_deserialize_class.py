# -*- coding: utf-8 -*-

from typing import Any, Dict, List, Optional
from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize


class Sample0:
    def __init__(self):
        pass


class Sample1:
    a: int
    b: float
    c: str

    def __init__(self):
        pass


class Sample2:
    name: str
    data1: Sample1
    data2: List[Sample1]
    data3: Dict[str, Sample1]

    def __init__(self):
        pass


class Sample3:
    data1: Optional[Sample1]
    data2: Any

    def __init__(self):
        pass


class Sample4:
    data1: List[int]
    data2: List[Sample1]
    data3: Dict[str, int]
    data4: Optional[Dict[str, int]]

    def __init__(self):
        pass


class DeserializeClassTestCase(TestCase):
    def test_sample0(self):
        result = deserialize({"E": 100, "W": 3.14, "Q": "?"}, Sample0)
        self.assertIsInstance(result, Sample0)
        self.assertEqual(100, getattr(result, "E"))
        self.assertEqual(3.14, getattr(result, "W"))
        self.assertEqual("?", getattr(result, "Q"))

    def test_sample1(self):
        result = deserialize({"a": 100, "b": 3.14, "c": "?"}, Sample1)
        self.assertIsInstance(result, Sample1)
        self.assertEqual(100, result.a)
        self.assertEqual(3.14, result.b)
        self.assertEqual("?", result.c)

    def test_sample2_1(self):
        data = {
            "name": "test2",
            "data1": {"a": 100, "b": 3.14, "c": "?"},
            "data2": [{"a": 2}, {"b": 0.1}, {"c": "/"}],
            "data3": {"AA": {"a": 200}, "BB": {"b": 9.1}, "CC": {"c": "M"}},
        }
        result = deserialize(data, Sample2)
        self.assertIsInstance(result, Sample2)
        self.assertEqual("test2", result.name)
        self.assertEqual(100, result.data1.a)
        self.assertEqual(3.14, result.data1.b)
        self.assertEqual("?", result.data1.c)
        self.assertIsInstance(result.data2, list)
        self.assertEqual(3, len(result.data2))
        self.assertEqual(2, result.data2[0].a)
        self.assertEqual(0.1, result.data2[1].b)
        self.assertEqual("/", result.data2[2].c)
        self.assertIsInstance(result.data3, dict)
        self.assertEqual(200, result.data3["AA"].a)
        self.assertEqual(9.1, result.data3["BB"].b)
        self.assertEqual("M", result.data3["CC"].c)

    def test_sample3_1(self):
        data = {
            "data1": {"a": 100, "b": 3.14, "c": "?"},
            "data2": [{"a": 1, "b": 2}],
            "data3": 100,
        }
        result = deserialize(data, Sample3)
        self.assertIsInstance(result, Sample3)

        test1 = result.data1
        self.assertIsInstance(test1, Sample1)
        self.assertEqual(100, test1.a)
        self.assertEqual(3.14, test1.b)
        self.assertEqual("?", test1.c)

        self.assertEqual([{"a": 1, "b": 2}], result.data2)
        self.assertEqual(100, getattr(result, "data3", None))

    def test_sample3_2(self):
        data = {
            "data1": None,
            "data3": 100,
        }
        result = deserialize(data, Sample3)
        self.assertIsInstance(result, Sample3)
        self.assertIsNone(getattr(result, "data1", None))
        self.assertIsNone(getattr(result, "data2", None))
        self.assertEqual(100, getattr(result, "data3", None))

    def test_sample3_3(self):
        result = deserialize(dict(), Sample3)
        self.assertIsInstance(result, Sample3)
        self.assertIsNone(getattr(result, "data1", None))
        self.assertIsNone(getattr(result, "data2", None))
        self.assertIsNone(getattr(result, "data3", None))

    def test_sample4_data1(self):
        data = {"data1": 2}
        result = deserialize(data, Sample4)
        self.assertIsInstance(result, Sample4)
        self.assertEqual(1, len(result.data1))
        self.assertEqual(2, result.data1[0])

    def test_sample4_data2(self):
        data = {"data2": {"a": 2}}
        result = deserialize(data, Sample4)
        self.assertIsInstance(result, Sample4)
        self.assertEqual(1, len(result.data2))
        self.assertEqual(2, result.data2[0].a)

    def test_sample4_data3(self):
        data = {"data3": [10, 20, 30]}
        result = deserialize(data, Sample4)
        self.assertIsInstance(result, Sample4)
        self.assertEqual(3, len(result.data3))
        self.assertEqual(10, result.data3["0"])
        self.assertEqual(20, result.data3["1"])
        self.assertEqual(30, result.data3["2"])

    def test_sample4_data4(self):
        data = {"data4": 10}
        result = deserialize(data, Sample4)
        self.assertIsInstance(result, Sample4)
        self.assertEqual(1, len(result.data4))
        self.assertEqual(10, result.data4["0"])


if __name__ == "__main__":
    main()
