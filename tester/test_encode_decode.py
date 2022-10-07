# -*- coding: utf-8 -*-

from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional
from unittest import TestCase, main

from type_serialize.decode import decode
from type_serialize.encode import encode


@dataclass
class Sample:
    project: str
    description: Optional[str] = None
    features: Optional[List[str]] = None
    extra: Optional[Any] = None
    updated: Optional[datetime] = None
    _hidden_name: Optional[str] = None

    def get_name(self):
        return self._hidden_name

    @property
    def name(self):
        return self._hidden_name

    @name.setter
    def name(self, value: str):
        self._hidden_name = value


class EncodeDecodeTestCase(TestCase):
    def test_default(self):
        now = datetime.now()
        data = Sample(project="a", description="b", extra={"k": 100}, updated=now)
        encoded_data = encode(data)
        self.assertIsInstance(encoded_data, bytes)
        self.assertGreater(len(encoded_data), 1)
        result = decode(encoded_data, Sample)
        self.assertEqual(result, data)


if __name__ == "__main__":
    main()
