# -*- coding: utf-8 -*-

from datetime import datetime
from unittest import TestCase, main

from type_serialize.obj.deserialize import deserialize


class DeserializeDatetimeTestCase(TestCase):
    def test_datetime(self):
        time_format = "2021-08-07T09:42:14.776297"
        result = deserialize(time_format, datetime)
        self.assertIsInstance(result, datetime)
        self.assertEqual(result, datetime.fromisoformat(time_format))


if __name__ == "__main__":
    main()
