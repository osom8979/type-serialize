# -*- coding: utf-8 -*-

from typing import Any

try:
    import yaml  # noqa
except ImportError:
    HAS_YAML = False
else:
    HAS_YAML = True


def valid_yaml_module():
    if not HAS_YAML:
        raise ModuleNotFoundError("Yaml module not found")


def yaml_encoder(data: Any) -> bytes:
    valid_yaml_module()
    return yaml.dump(data).encode("utf-8")


def yaml_decoder(data: bytes) -> Any:
    valid_yaml_module()
    return yaml.full_load(data)
