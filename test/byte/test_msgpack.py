# -*- coding: utf-8 -*-

import os
from unittest import TestCase, main, skipIf

from type_serialize.byte.msgpack import (
    msgpack_bz2_decoder,
    msgpack_bz2_encoder,
    msgpack_decoder,
    msgpack_encoder,
    msgpack_gzip_decoder,
    msgpack_gzip_encoder,
    msgpack_lzma_decoder,
    msgpack_lzma_encoder,
    msgpack_zlib_decoder,
    msgpack_zlib_encoder,
)
from type_serialize.driver.msgpack import HAS_MSGPACK

SAMPLE_JSON_PATH = os.path.join(os.path.dirname(__file__), "sample.json")
SAMPLE_JSON = open(SAMPLE_JSON_PATH).read()


@skipIf(not HAS_MSGPACK, "MsgPack module not found")
class MsgpackTestCase(TestCase):
    def test_msgpack(self):
        serialize_data = msgpack_encoder(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = msgpack_decoder(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)

    def test_msgpack_zlib(self):
        serialize_data = msgpack_zlib_encoder(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = msgpack_zlib_decoder(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)

    def test_msgpack_gzip(self):
        serialize_data = msgpack_gzip_encoder(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = msgpack_gzip_decoder(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)

    def test_msgpack_lzma(self):
        serialize_data = msgpack_lzma_encoder(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = msgpack_lzma_decoder(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)

    def test_msgpack_bz2(self):
        serialize_data = msgpack_bz2_encoder(SAMPLE_JSON)
        self.assertLess(0, len(serialize_data))
        deserialize_data = msgpack_bz2_decoder(serialize_data)
        self.assertEqual(SAMPLE_JSON, deserialize_data)


if __name__ == "__main__":
    main()
