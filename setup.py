# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

PACKAGE_NAME = "type_serialize"
PACKAGE_VERSION = "0.0.1"

SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)


def setup_main():
    setup(
        name=PACKAGE_NAME,
        version=PACKAGE_VERSION,
        packages=find_packages(where=SCRIPT_DIR, exclude=("test*",)),
        package_dir={PACKAGE_NAME: PACKAGE_NAME},
    )


if __name__ == "__main__":
    setup_main()
