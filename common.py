#!/usr/bin/env python

import re

from typing import Iterable, List


def find_multiplier(table_header: List[str]) -> int:
    """
    Finds dollar in thousands, millions etc and returns an integer value to know the multiplier
    needed for currency
    :table_header: meta information for each table
    :return: number corresponding to 1000 for thousand etc as a multiplier to be used later
    """
    mult_conversion = {'THOUSAND': 1000, 'MILLION': 1000000, 'BILLION': 1000000000}
    multiplier = 1
    dollar_lines = [x for x, line in enumerate(table_header)
                    if re.search(r"DOLLAR|USD|\$", line.upper())]
    if len(dollar_lines):
        for dollar_line in dollar_lines:
            for mult in list(mult_conversion.keys()):
                if any(within_lines(table_header, mult, (dollar_line - 1, dollar_line + 2))):
                    multiplier = mult_conversion[mult]
                    return multiplier
    return multiplier


def within_lines(lines: list, text_find: str, lines_range: tuple) -> Iterable[bool]:
    """
    Iterable to quickly go through and find if a lines phrase is within the lines of the table
    :lines: lines within the table
    :text_find: the text to find
    :lines_range: the range within to search
    :return: an iterable T/F boolean
    """
    for line in lines[lines_range[0]:lines_range[1]]:
        yield text_find.upper() in line.upper()
