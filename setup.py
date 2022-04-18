#!/usr/bin/env python3

from setuptools import setup

setup(
    name="pyskel",
    version="0.0.0",
    description="A skeleton for python project",
    author="netzego",
    author_email="dev@netzego.de",
    url="https://github.com/netzego/pyskel",
    packages=["pyskel"],
    package_dir={"": "src"},
    entry_points={"console_scripts": ["pyskel=pyskel:main"]},
)
