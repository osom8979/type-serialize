# type-serialize

![PyPI](https://img.shields.io/pypi/v/type-serialize?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/type-serialize?style=flat-square)
![GitHub](https://img.shields.io/github/license/osom8979/type-serialize?style=flat-square)

Serialize with type annotations

## Features

- Supported in Python 3.8 and later.
- Serialize classes without additional code.
  - Custom classes
  - [@dataclas](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass)
  - [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)
  - [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)
  - (Experimental) [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy-ndarray)
- Deserialization using type annotations.
- Compress serialization results: bz2, gzip, lzma, zlib
- No dependencies

## Overview

To pass a custom object to the [json.dumps](https://docs.python.org/3/library/json.html#json.dumps)
and [json.loads](https://docs.python.org/3/library/json.html#json.loads) functions,
there is the following method.

- Expand [json.JSONEncoder](https://docs.python.org/3/library/json.html#json.JSONEncoder)
  and [json.JSONDecoder](https://docs.python.org/3/library/json.html#json.JSONDecoder).
- Convert to built-in Python object supported by
  [json.JSONEncoder](https://docs.python.org/3/library/json.html#json.JSONEncoder) and
  [json.JSONDecoder](https://docs.python.org/3/library/json.html#json.JSONDecoder).

Both methods require additional code and have some problems.

- Problem of not checking symbols when manipulating strings.
- When adding/deleting/editing a property, all related codes must be changed together.
- Painful typecasting (as the biggest problem).

As a way to hide these problems with a library and use serialization and deserialization,
I chose **[type annotations](https://docs.python.org/3/library/typing.html)**.
(Although the library is complicated; haha...) There are some additional advantages to using this.

- Static type checking using [mypy](https://mypy.readthedocs.io/en/stable/).
- Autocomplete in IDE like PyCharm.

### Things to know

- All public fields are serialized.
- Methods are not serialized.
- Private fields that start with an underscore (`_`) are not serialized.
- Members specified with the `@property` decorator are not serialized.
- When deserializing, all fields must be type-annotated.
- A value of `None` is ignored by the serialization target.
- When deserializing, the `__init__` function must have **NO** required arguments.
- Implement `__serialize__` to override the serialization method.
- Implement `__deserialize__` to override the deserialization method.

## Installation

```shell
pip install type-serialize
```

If you want to add [numpy](https://numpy.org/), [orjson](https://github.com/ijl/orjson),
[msgpack](https://msgpack.org/), [pyyaml](https://pyyaml.org/) support:

```shell
pip install type-serialize[full]
```

## Usage

### Serializable python object

```python
from dataclasses import dataclass
from type_serialize import deserialize, serialize


@dataclass
class Sample:
    field1: str
    field2: int


data = Sample(field1="a", field2=100)
obj = serialize(data)
assert isinstance(obj, dict)
assert obj["field1"] == "a"
assert obj["field2"] == 100
print(obj)

result = deserialize(obj, Sample)
assert isinstance(result, Sample)
assert data == result
print(result)
```

### Override serialize and deserialize

```python
from dataclasses import dataclass
from type_serialize import deserialize, serialize


@dataclass
class Sample:
    value: int

    def __serialize__(self):
        return {"a": self.value}

    def __deserialize__(self, data) -> None:
        self.value = data["a"]

    def __init__(self, value=100):
        self.value = value


test = Sample(value=200)
obj = serialize(test)
assert isinstance(obj, dict)
assert obj["a"] == 200
print(obj)

result = deserialize(obj, Sample)
assert isinstance(result, Sample)
assert test == result
print(result)
```

### JSON dumps/loads

```python
from dataclasses import dataclass
from type_serialize.json import dumps, loads

@dataclass
class Sample:
    field1: str
    field2: int


data = Sample(field1="a", field2=100)
json_data = dumps(data)
print(json_data)

result = loads(json_data, Sample)
print(result)
```

### MsgPack dumps/loads

```python
from dataclasses import dataclass
from type_serialize.msgpack import dumps, loads

@dataclass
class Sample:
    field1: str
    field2: int


data = Sample(field1="a", field2=100)
json_data = dumps(data)
print(json_data)

result = loads(json_data, Sample)
print(result)
```

### Binary encode/decode

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional

from type_serialize import decode, encode


@dataclass
class Sample:
    field1: str
    field2: Optional[str] = None
    field3: Optional[List[int]] = None
    field4: Optional[Any] = None
    field5: Optional[datetime] = None


data = Sample(
    field1="a",
    field3=[0, 1, 2],
    field4={"k": 100},
    field5=datetime.now(),
)

raw = encode(data)
assert isinstance(raw, bytes)
assert len(raw) > 0
print(raw)

result = decode(raw, Sample)
assert isinstance(result, Sample)
assert data == result
print(result)
```

The encoding format can be adjusted with the `coding` argument.

```python
from type_serialize import ByteCoding, decode, encode

data = ...
print(encode(data, coding=ByteCoding.MsgpackGzip))

encoded_data = ...
print(decode(encoded_data, coding=ByteCoding.OrjsonZlib))
```

## orjson support

If [orjson](https://github.com/ijl/orjson) is installed, it is automatically detected and used.

To turn off this option, set the `TYPE_SERIALIZE_DISABLE_ORJSON_INSTALL` environment variable to `1`.

## License

See the [LICENSE](./LICENSE) file for details. In summary,
**type-serialize** is licensed under the **MIT license**.
