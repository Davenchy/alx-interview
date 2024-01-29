#!/usr/bin/python3
"""This program reads log file from stdin and prints stats to stdout
every 10 lines, when EOF is reached and on KeyboardInterrupt (Ctrl+C)"""

import re
import sys
from typing import Dict, Tuple, Union

# A list of the allowed status codes
ALLOWED_CODES = ["200", "301", "400", "401", "403", "404", "405", "500"]


def log_line_extractor(line: str) -> Union[None, Tuple[str, str]]:
    """validate and extract data from log line
    Line Format: <IP> - [DATE] "GET /projects/260 HTTP/1.1" <code> <size>

    Returns:
        Extracted data as a tuple of (code, size) or None if line is invalid"""
    results = re.findall(
        r"^.*\s?-\s?\[.*\]" +
        r" \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$",
        line,
    )

    if not results:
        return None
    return results[0]


def print_stats(fileSize: int, codes: Dict[str, int]):
    """print stats into stdout"""
    print("File size: {}".format(fileSize))
    for key in sorted(codes):
        print("{}: {}".format(key, codes[key]))


if __name__ == "__main__":
    fileSize = 0
    codes = dict()
    counter = 0

    try:
        for line in sys.stdin:
            counter += 1
            results = log_line_extractor(line)
            if results is None:
                continue

            code, size = results
            fileSize += int(size)

            if code in ALLOWED_CODES:
                codes[code] = codes.get(code, 0) + 1

            if counter == 10:
                print_stats(fileSize, codes)
                counter = 0
    except KeyboardInterrupt:
        print_stats(fileSize, codes)
        counter = 0

    if counter > 0:
        print_stats(fileSize, codes)
