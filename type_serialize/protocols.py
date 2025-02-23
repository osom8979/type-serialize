# -*- coding: utf-8 -*-

from typing import Final, Sequence

TYPING_INTERNALS: Final[Sequence[str]] = (
    "__parameters__",
    "__orig_bases__",
    "__orig_class__",
    "_is_protocol",
    "_is_runtime_protocol",
    "__final__",
)

SPECIAL_NAMES: Final[Sequence[str]] = (
    "__abstractmethods__",
    "__annotations__",
    "__dict__",
    "__doc__",
    "__init__",
    "__module__",
    "__new__",
    "__slots__",
    "__subclasshook__",
    "__weakref__",
    "__class_getitem__",
)

EXCLUDED_ATTRIBUTES: Final[Sequence[str]] = (
    *TYPING_INTERNALS,
    *SPECIAL_NAMES,
    "_MutableMapping__marker",
)


def get_protocol_attrs(cls):
    """Collect protocol members from a protocol class objects.

    This includes names actually defined in the class dictionary, as well
    as names that appear in annotations. Special names (above) are skipped.
    """
    attrs = set()
    for base in cls.__mro__[:-1]:  # without object
        if base.__name__ in ("Protocol", "Generic"):
            continue
        annotations = getattr(base, "__annotations__", {})
        for attr in list(base.__dict__.keys()) + list(annotations.keys()):
            if not attr.startswith("_abc_") and attr not in EXCLUDED_ATTRIBUTES:
                attrs.add(attr)
    return attrs


def is_callable_members_only(cls):
    # PEP 544 prohibits using issubclass() with protocols that have non-method members.
    return all(callable(getattr(cls, attr, None)) for attr in get_protocol_attrs(cls))
