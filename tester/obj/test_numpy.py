# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import List, Optional
from unittest import TestCase, main, skipIf

from type_serialize.driver.numpy import HAS_NUMPY, numpy_deserialize, numpy_serialize
from type_serialize.obj.deserialize import deserialize
from type_serialize.obj.serialize import serialize


@skipIf(not HAS_NUMPY, "Not has numpy")
class NumpyTestCase(TestCase):
    def test_numpy_serialize(self):
        import numpy as np

        image = np.random.randint(0, 255, size=(1270, 1920, 3), dtype=np.uint8)
        self.assertEqual((1270, 1920, 3), image.shape)
        self.assertEqual(np.uint8, image.dtype)
        proto = numpy_serialize(image)
        result = numpy_deserialize(proto)
        self.assertTrue((result == image).all())

    def test_numpy_serialize_tuple(self):
        import numpy as np

        image = np.random.randint(0, 255, size=(1270, 1920, 3), dtype=np.uint8)
        self.assertEqual((1270, 1920, 3), image.shape)
        self.assertEqual(np.uint8, image.dtype)
        proto = numpy_serialize(image)
        result = numpy_deserialize(tuple(proto))
        self.assertTrue((result == image).all())

    def test_default(self):
        import numpy as np

        @dataclass
        class Sample:
            test1: str
            test2: Optional[List[np.ndarray]] = None

        array0 = np.random.rand(10, 20, 30)
        array1 = np.random.randint(0, 255, size=(1270, 1920, 3), dtype=np.uint8)
        test_data = Sample("test1", [array0, array1])

        encoded_data = serialize(test_data)

        result_data = deserialize(encoded_data, Sample)
        self.assertEqual(test_data.test1, result_data.test1)
        self.assertEqual(len(test_data.test2), len(result_data.test2))
        self.assertTrue((test_data.test2[0] == result_data.test2[0]).all())
        self.assertTrue((test_data.test2[1] == result_data.test2[1]).all())
        self.assertEqual(test_data.test2[0].dtype, result_data.test2[0].dtype)
        self.assertEqual(test_data.test2[1].dtype, result_data.test2[1].dtype)


if __name__ == "__main__":
    main()
