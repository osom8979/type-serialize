# -*- coding: utf-8 -*-

from typing import Any, List, Optional
from argparse import ArgumentParser, Namespace

from type_serialize import __version__ as version

PROGRAM = "type_serialize"
DESCRIPTION = "Serialize with type annotations"


def default_argparse(
    cmdline: Optional[List[Any]] = None,
    namespace: Optional[Namespace] = None,
) -> Namespace:
    parser = ArgumentParser(prog=PROGRAM, description=DESCRIPTION)
    parser.add_argument("--version", action="version", version=version)
    return parser.parse_args(
        args=[str(x) for x in cmdline] if cmdline is not None else None,
        namespace=namespace,
    )


def main(cmdline: Optional[List[Any]] = None) -> None:
    default_argparse(cmdline)
    raise NotImplementedError
