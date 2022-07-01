# -*- coding: utf-8 -*-

from dataclasses import dataclass
from json import dumps as json_dumps
from json import loads as json_loads
from unittest import TestCase, main

from type_serialize.json import dumps as ts_dumps
from type_serialize.json import loads as ts_loads


@dataclass
class Sample:
    value0: str
    value1: int
    value2: float
    value3: bool


class RootJsonTestCase(TestCase):
    def setUp(self):
        data = Sample("a", 1, 2.0, True)
        encoded_data = ts_dumps(data)
        self.assertIsInstance(encoded_data, bytes)
        self.assertGreater(len(encoded_data), 1)
        result = ts_loads(encoded_data, Sample)
        self.assertEqual(result, data)

        # Serializable Python Object (SPO)
        self.spo_data = ts_loads(encoded_data)

    def test_compatible_json(self):
        encoded_json_data = json_dumps(self.spo_data)
        json_result = json_loads(encoded_json_data)
        self.assertEqual(json_result, self.spo_data)


if __name__ == "__main__":
    main()
