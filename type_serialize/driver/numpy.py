# -*- coding: utf-8 -*-

from sys import platform
from typing import Iterable, List, NamedTuple, Union

try:
    import numpy  # noqa
except ImportError:
    HAS_NUMPY = False
else:
    HAS_NUMPY = True


def valid_numpy_module():
    if not HAS_NUMPY:
        raise ModuleNotFoundError("NumPy module not found")


def is_ndarray_instance(obj) -> bool:
    valid_numpy_module()
    return isinstance(obj, numpy.ndarray)


def is_ndarray_subclass(cls) -> bool:
    valid_numpy_module()
    return issubclass(cls, numpy.ndarray)


def _ndarray_to_bytes_by_darwin(array) -> bytes:
    valid_numpy_module()
    assert isinstance(array, numpy.ndarray)
    return array.tobytes()


def _ndarray_to_bytes(array) -> bytes:
    valid_numpy_module()
    assert isinstance(array, numpy.ndarray)

    if array.flags["C_CONTIGUOUS"]:
        data = array.data
        if isinstance(data, memoryview):
            return data.tobytes()
        else:
            assert isinstance(data, bytes)
            return data
    else:
        return array.tobytes()


if platform == "darwin":
    ndarray_to_bytes = _ndarray_to_bytes_by_darwin
else:
    ndarray_to_bytes = _ndarray_to_bytes


class NumpyProto(NamedTuple):
    shape: List[int]
    dtype: str
    buffer: bytes
    strides: List[int]


def numpy_serialize(array) -> NumpyProto:
    valid_numpy_module()
    assert isinstance(array, numpy.ndarray)

    try:
        numpy.dtype(array.dtype.name)
    except:  # noqa
        if array.dtype.name:
            raise ValueError(f"Unsupported dtype name: {array.dtype.name}")
        else:
            raise ValueError(f"Empty dtype name: {array.dtype}")
    return NumpyProto(
        shape=list(array.shape),
        dtype=array.dtype.name,
        buffer=ndarray_to_bytes(array),
        strides=list(array.strides),
    )


def _numpy_deserialize(proto: NumpyProto):
    valid_numpy_module()
    try:
        dt = numpy.dtype(proto.dtype)
    except:  # noqa
        if proto.dtype:
            raise ValueError(f"Unsupported dtype name: {proto.dtype}")
        else:
            raise ValueError("Empty dtype name")
    return numpy.ndarray(
        shape=proto.shape,
        dtype=dt,
        buffer=proto.buffer,
        strides=proto.strides,
    )


def numpy_deserialize(proto: Union[list, tuple, NumpyProto]):
    valid_numpy_module()
    if isinstance(proto, NumpyProto):
        return _numpy_deserialize(proto)
    elif isinstance(proto, (list, tuple)):
        if len(proto) != 4:
            raise ValueError(
                "There must be 4 elements. "
                f"There are actually {len(proto)} elements."
            )
        if not isinstance(proto[0], Iterable):
            raise ValueError("The first element must be `Iterable`")
        if not isinstance(proto[1], str):
            raise ValueError("The second element must be `str`")
        if not isinstance(proto[2], (bytes, bytearray, memoryview)):
            raise ValueError("The third element must be `bytes-like`")
        if not isinstance(proto[3], Iterable):
            raise ValueError("The forth element must be `Iterable`")
        return _numpy_deserialize(NumpyProto(*proto))
    else:
        raise TypeError(f"Unsupported proto type: {type(proto).__name__}")
