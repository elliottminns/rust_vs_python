#!/usr/bin/env python

import common
import librust_vs_python
import pytest


def test_find_multiplier_python(benchmark):
    table_header_same = [
        "header line 1",
        "header line 2",
        "header line 3",
        "dollars in billion",
        "header line 5",
        "header line 6",
        "header line 7"
    ]
    benchmark(common.find_multiplier, table_header_same)


def test_find_multiplier_rust(benchmark):
    table_header_same = [
        "header line 1",
        "header line 2",
        "header line 3",
        "dollars in billion",
        "header line 5",
        "header line 6",
        "header line 7"
    ]
    benchmark(librust_vs_python.find_multiplier, table_header_same)
