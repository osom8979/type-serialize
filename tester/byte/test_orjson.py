# -*- coding: utf-8 -*-

import os
from unittest import TestCase, main, skipIf

from type_serialize.byte.orjson import (
    orjson_byte_decoder,
    orjson_byte_encoder,
    orjson_bz2_decoder,
    orjson_bz2_encoder,
    orjson_gzip_decoder,
    orjson_gzip_encoder,
    orjson_lzma_decoder,
    orjson_lzma_encoder,
    orjson_zlib_decoder,
    orjson_zlib_encoder,
)
from type_serialize.driver.json import HAS_ORJSON

SAMPLE_JSON_PATH = os.path.join(os.path.dirname(__file__), "sample.json")
SAMPLE_JSON = open(SAMPLE_JSON_PATH).read()


@skipIf(not HAS_ORJSON, "orjson module not found")
class OrjsonTestCase(TestCase):
    def test_orjson(self):
        serialize_data = orjson_byte_encoder(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = orjson_byte_decoder(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)

    def test_orjson_zlib(self):
        serialize_data = orjson_zlib_encoder(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = orjson_zlib_decoder(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)

    def test_orjson_gzip(self):
        serialize_data = orjson_gzip_encoder(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = orjson_gzip_decoder(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)

    def test_orjson_lzma(self):
        serialize_data = orjson_lzma_encoder(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = orjson_lzma_decoder(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)

    def test_orjson_bz2(self):
        serialize_data = orjson_bz2_encoder(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = orjson_bz2_decoder(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)


if __name__ == "__main__":
    main()
