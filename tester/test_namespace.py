# -*- coding: utf-8 -*-

from argparse import Namespace
from typing import List, Optional
from unittest import TestCase, main

from type_serialize.deserialize import deserialize


class TestNamespace(Namespace):
    value1: int
    value2: float
    value3: bool
    value4: List[int]
    value5: Optional[int]
    value6: Optional[float]
    value7: Optional[bool]


class NamespaceTestCase(TestCase):
    def test_namespace(self):
        all_string_attributes = Namespace(
            value1="100",
            value2="1.2",
            value3="true",
            value4="999",
            value5="100",
            value6="10.1",
            value7="false",
        )
        test = deserialize(all_string_attributes, TestNamespace)
        self.assertEqual(100, test.value1)
        self.assertAlmostEqual(1.2, test.value2)
        self.assertIsInstance(test.value3, bool)
        self.assertTrue(test.value3)
        self.assertIsInstance(test.value4, list)
        self.assertEqual(1, len(test.value4))
        self.assertEqual(999, test.value4[0])
        self.assertEqual(100, test.value5)
        self.assertAlmostEqual(10.1, test.value6)
        self.assertIsInstance(test.value7, bool)
        self.assertFalse(test.value7)


if __name__ == "__main__":
    main()
