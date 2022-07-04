# -*- coding: utf-8 -*-

from typing import Any, Dict, List, Optional
from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize
from type_serialize.obj.interface import Serializable
from type_serialize.obj.serialize import serialize


class EmptySample:
    def __init__(self):
        pass


class UntypedSample:
    def __init__(self):
        self.name = "test0"
        self.data1 = 0
        self.data2 = 1.1
        self.data3 = [1, 2, 3, 4]
        self.data4 = {"a": 0, "b": 1.2, "c": "?"}


class BuiltinSample:
    a: int
    b: float
    c: str
    d: bool

    def __init__(self):
        pass


class NestedSample:
    a: BuiltinSample

    def __init__(self):
        pass


class ListNestedSample:
    a: List[BuiltinSample]

    def __init__(self):
        pass


class DictNestedSample:
    a: Dict[str, BuiltinSample]

    def __init__(self):
        pass


class OptionalNestedSample:
    a: Optional[BuiltinSample] = None

    def __init__(self):
        pass


class AnySample:
    a: Any

    def __init__(self):
        pass


class SerializableSample(Serializable):
    value: int

    def __serialize__(self) -> Any:
        return {"a": self.value}

    def __deserialize__(self, data: Any) -> None:
        self.value = data["a"]

    def __init__(self, value=100):
        self.value = value


class NotInheritedSerializableSample:
    value: int

    def __serialize__(self) -> Any:
        return {"a": self.value}

    def __deserialize__(self, data: Any) -> None:
        self.value = data["a"]

    def __init__(self, value=100):
        self.value = value


class ClassTestCase(TestCase):
    def test_untyped(self):
        test = UntypedSample()
        data = serialize(test)
        result = {
            "name": "test0",
            "data1": 0,
            "data2": 1.1,
            "data3": [1, 2, 3, 4],
            "data4": {"a": 0, "b": 1.2, "c": "?"},
        }
        self.assertEqual(result, data)

    def test_forced_injection(self):
        result = deserialize({"E": 100, "W": 3.14, "Q": "?"}, EmptySample)
        self.assertIsInstance(result, EmptySample)
        self.assertEqual(100, getattr(result, "E"))
        self.assertEqual(3.14, getattr(result, "W"))
        self.assertEqual("?", getattr(result, "Q"))

    def test_builtin(self):
        result = deserialize({"a": 100, "b": 3.14, "c": "?", "d": True}, BuiltinSample)
        self.assertIsInstance(result, BuiltinSample)
        self.assertEqual(100, result.a)
        self.assertEqual(3.14, result.b)
        self.assertEqual("?", result.c)
        self.assertTrue(result.d)

    def test_nested(self):
        data = {"a": {"a": 100, "b": 3.14, "c": "?"}}
        result = deserialize(data, NestedSample)
        self.assertIsInstance(result, NestedSample)
        self.assertIsInstance(result.a, BuiltinSample)
        self.assertEqual(100, result.a.a)
        self.assertEqual(3.14, result.a.b)
        self.assertEqual("?", result.a.c)

    def test_list_nested(self):
        test = ListNestedSample()
        test.a = [{"a": 2}, {"b": 0.1}, {"c": "/"}]
        data = serialize(test)
        self.assertEqual({"a": [{"a": 2}, {"b": 0.1}, {"c": "/"}]}, data)

        result = deserialize(data, ListNestedSample)
        self.assertIsInstance(result, ListNestedSample)
        self.assertIsInstance(result.a, list)
        self.assertEqual(3, len(result.a))
        self.assertIsInstance(result.a[0], BuiltinSample)
        self.assertIsInstance(result.a[1], BuiltinSample)
        self.assertIsInstance(result.a[2], BuiltinSample)
        self.assertEqual(2, result.a[0].a)
        self.assertEqual(0.1, result.a[1].b)
        self.assertEqual("/", result.a[2].c)

    def test_dict_nested(self):
        test = DictNestedSample()
        test.a = {"A": {"a": 200}, "B": {"b": 9.1}}
        data = serialize(test)
        self.assertEqual({"a": {"A": {"a": 200}, "B": {"b": 9.1}}}, data)

        result = deserialize(data, DictNestedSample)
        self.assertIsInstance(result, DictNestedSample)
        self.assertIsInstance(result.a, dict)
        self.assertEqual(2, len(result.a))
        self.assertIsInstance(result.a["A"], BuiltinSample)
        self.assertIsInstance(result.a["B"], BuiltinSample)
        self.assertEqual(200, result.a["A"].a)
        self.assertEqual(9.1, result.a["B"].b)

    def test_none_nested(self):
        test = OptionalNestedSample()
        data = serialize(test)
        self.assertEqual({}, data)

        result = deserialize(data, OptionalNestedSample)
        self.assertIsInstance(result, OptionalNestedSample)
        self.assertIsNone(result.a)

    def test_any(self):
        test = AnySample()
        test.a = {"b": 100}
        data = serialize(test)
        self.assertEqual({"a": {"b": 100}}, data)

        result = deserialize(data, AnySample)
        self.assertIsInstance(result, AnySample)
        self.assertIsInstance(result.a, dict)
        self.assertEqual({"b": 100}, result.a)

    def test_serializable(self):
        test = SerializableSample()
        data = serialize(test)
        self.assertEqual({"a": 100}, data)

        result = deserialize(data, SerializableSample)
        self.assertIsInstance(result, SerializableSample)
        self.assertTrue(100, result.value)

    def test_not_inherited_serializable(self):
        test = NotInheritedSerializableSample()
        data = serialize(test)
        self.assertEqual({"a": 100}, data)

        result = deserialize(data, NotInheritedSerializableSample)
        self.assertIsInstance(result, NotInheritedSerializableSample)
        self.assertTrue(100, result.value)


if __name__ == "__main__":
    main()
