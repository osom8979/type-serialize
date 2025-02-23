# -*- coding: utf-8 -*-

from datetime import datetime
from unittest import TestCase, main

from type_serialize.deserialize import deserialize
from type_serialize.serialize import serialize


class DatetimeTestCase(TestCase):
    def test_datetime(self):
        test = "2021-08-07T09:42:14.776297"

        now = datetime.fromisoformat(test)
        data = serialize(now)
        self.assertIsInstance(data, str)
        self.assertEqual(test, data)

        result = deserialize(test, datetime)
        self.assertIsInstance(result, datetime)
        self.assertEqual(now, result)


if __name__ == "__main__":
    main()
