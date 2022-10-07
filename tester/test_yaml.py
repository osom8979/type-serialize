# -*- coding: utf-8 -*-

from dataclasses import dataclass
from unittest import TestCase, main, skipIf

from type_serialize.driver.yaml import HAS_YAML
from type_serialize.yaml import dumps as ts_dumps
from type_serialize.yaml import loads as ts_loads


@dataclass
class Sample:
    value0: str
    value1: int
    value2: float
    value3: bool


@skipIf(not HAS_YAML, "Yaml module not found")
class YamlTestCase(TestCase):
    def test_default(self):
        data = Sample("a", 1, 2.0, True)
        encoded_data = ts_dumps(data)
        self.assertIsInstance(encoded_data, bytes)
        self.assertGreater(len(encoded_data), 1)
        result = ts_loads(encoded_data, Sample)
        self.assertEqual(result, data)


if __name__ == "__main__":
    main()
