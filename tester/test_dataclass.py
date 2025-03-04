# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Dict, List, Optional
from unittest import TestCase, main

from type_serialize.deserialize import deserialize
from type_serialize.serialize import serialize


@dataclass
class Sample:
    test1: str
    test2: Optional[str] = None

    @property
    def test3(self):
        assert self
        return 30

    def test4(self):
        assert self
        return 40


class DataclassTestCase(TestCase):
    def test_dataclass(self):
        test = Sample(test1="aa")
        data = serialize(test)
        self.assertEqual({"test1": "aa"}, data)

        result = deserialize({"test1": "aa"}, Sample)
        self.assertIsInstance(result, Sample)
        self.assertEqual("aa", result.test1)
        self.assertIsNone(result.test2)

    def test_dataclass_list(self):
        result = deserialize([{"test1": "aa"}], List[Sample])
        self.assertIsInstance(result, list)
        self.assertEqual(1, len(result))
        self.assertIsInstance(result[0], Sample)
        self.assertEqual("aa", result[0].test1)
        self.assertIsNone(result[0].test2)

    def test_dataclass_dict(self):
        result = deserialize({"key1": {"test1": "aa"}}, Dict[str, Sample])
        self.assertIsInstance(result, dict)
        self.assertEqual(1, len(result))
        self.assertIn("key1", result)
        self.assertIsInstance(result["key1"], Sample)
        self.assertEqual("aa", result["key1"].test1)
        self.assertIsNone(result["key1"].test2)


if __name__ == "__main__":
    main()
