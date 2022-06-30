# -*- coding: utf-8 -*-

import os
from unittest import TestCase, main

from type_serialize.byte.pickle import pickling, unpickling

SAMPLE_JSON_PATH = os.path.join(os.path.dirname(__file__), "sample.json")
SAMPLE_JSON = open(SAMPLE_JSON_PATH).read()


class PickleTestCase(TestCase):
    def test_pickle(self):
        serialize_data = pickling(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = unpickling(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)


if __name__ == "__main__":
    main()
