# type-serialize

Serialize with type annotations

## Features

- Supported in Python 3.8 and later.
- Serialize classes without additional code.
- Deserialization using type annotations.
- Compress serialization results: bz2, gzip, lzma, zlib
- No dependencies

## Installation

```shell
pip install type-serialize
```

If you want to add [numpy](https://numpy.org/), [orjson](https://github.com/ijl/orjson), [msgpack](https://msgpack.org/) support:
```shell
pip install type-serialize[full]
```

## Note

- All public fields are serialized.
- Methods are not serialized.
- Private fields that start with an underscore (`_`) are not serialized.
- Members specified with the `@property` decorator are not serialized.
- When deserializing, all fields must be type-annotated.

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
from type_serialize import ByteCodingType, decode, encode

data = ...
print(encode(data, coding=ByteCodingType.MsgpackGzip))
```

## orjson support

If [orjson](https://github.com/ijl/orjson) is installed, it is automatically detected and used.

To turn off this option, set the `TYPE_SERIALIZE_DISABLE_ORJSON_INSTALL` environment variable to `1`.

## License

See the [LICENSE](./LICENSE) file for details. In summary, tbag is licensed under the **MIT license**.
