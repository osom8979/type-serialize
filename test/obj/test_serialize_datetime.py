# -*- coding: utf-8 -*-

from datetime import datetime
from unittest import TestCase, main

from type_serialize.obj.serialize import serialize


class SerializeDatetimeTestCase(TestCase):
    def test_datetime(self):
        now = datetime.fromisoformat("2021-08-07T09:42:14.776297")
        data = serialize(now)
        self.assertIsInstance(data, str)
        self.assertEqual(now, datetime.fromisoformat(data))


if __name__ == "__main__":
    main()
