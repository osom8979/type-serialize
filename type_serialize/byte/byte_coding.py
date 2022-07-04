# -*- coding: utf-8 -*-

from enum import Enum, unique


@unique
class ByteCoding(Enum):
    Raw = 0
    Pickle5 = 1

    # Automatically select the installed json library.
    Json = 2
    JsonZlib = 3
    JsonGzip = 4
    JsonLzma = 5
    JsonBz2 = 6

    # System default json library.
    Pyjson = 7
    PyjsonZlib = 8
    PyjsonGzip = 9
    PyjsonLzma = 10
    PyjsonBz2 = 11

    # orjson module
    Orjson = 12
    OrjsonZlib = 13
    OrjsonGzip = 14
    OrjsonLzma = 15
    OrjsonBz2 = 16

    # msgpack module
    Msgpack = 17
    MsgpackZlib = 18
    MsgpackGzip = 19
    MsgpackLzma = 20
    MsgpackBz2 = 21

    # yaml module
    Yaml = 22
    YamlZlib = 23
    YamlGzip = 24
    YamlLzma = 25
    YamlBz2 = 26
