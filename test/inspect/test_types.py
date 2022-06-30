# -*- coding: utf-8 -*-

from typing import Optional, get_type_hints
from unittest import TestCase, main

from type_serialize.inspect.member import get_public_attributes
from type_serialize.inspect.types import (
    is_serializable_pod_cls,
    is_serializable_pod_obj,
)


class Sample1:
    def __init__(self, number: int = 100, name: Optional[str] = None):
        self._protected = "protected"
        self.number = number
        self.name = name


class Sample2:

    _protected: str
    test: Optional[Sample1]
    name: Optional[str]

    def __init__(self, test: Optional[Sample1] = None, name: Optional[str] = None):
        self._protected = "protected"
        self.test = test
        self.name = name


class TypesTestCase(TestCase):
    def test_public_members_by_obj(self):
        obj1_names = [m[0] for m in get_public_attributes(Sample1())]
        self.assertEqual(2, len(obj1_names))
        self.assertIn("number", obj1_names)
        self.assertIn("name", obj1_names)
        obj2_names = [m[0] for m in get_public_attributes(Sample2())]
        self.assertEqual(2, len(obj2_names))
        self.assertIn("test", obj2_names)
        self.assertIn("name", obj2_names)

    def test_public_members_by_cls(self):
        cls1_names = [m[0] for m in get_public_attributes(Sample1)]
        self.assertEqual(0, len(cls1_names))
        cls2_names = [m[0] for m in get_public_attributes(Sample2)]
        self.assertEqual(0, len(cls2_names))

    def test_is_serializable_pod_cls(self):
        self.assertFalse(is_serializable_pod_cls(Sample1))
        self.assertFalse(is_serializable_pod_cls(Sample2))

        self.assertTrue(is_serializable_pod_cls(str))
        self.assertTrue(is_serializable_pod_cls(int))
        self.assertTrue(is_serializable_pod_cls(float))

        self.assertFalse(is_serializable_pod_cls("a"))
        self.assertFalse(is_serializable_pod_cls(100))
        self.assertFalse(is_serializable_pod_cls(3.14))

    def test_is_serializable_pod_obj(self):
        self.assertFalse(is_serializable_pod_obj(Sample1))
        self.assertFalse(is_serializable_pod_obj(Sample2))

        self.assertFalse(is_serializable_pod_obj(str))
        self.assertFalse(is_serializable_pod_obj(int))
        self.assertFalse(is_serializable_pod_obj(float))

        self.assertTrue(is_serializable_pod_obj("a"))
        self.assertTrue(is_serializable_pod_obj(100))
        self.assertTrue(is_serializable_pod_obj(3.14))

    def test_get_type_hints(self):
        hint1 = get_type_hints(Sample1)
        hint2 = get_type_hints(Sample2)
        self.assertEqual(0, len(hint1))
        self.assertEqual(3, len(hint2))


if __name__ == "__main__":
    main()
