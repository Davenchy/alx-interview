#!/usr/bin/python3
"""This program reads log file from stdin and prints stats to stdout
every 10 lines, when EOF is reached and on KeyboardInterrupt (Ctrl+C)"""

import re
import sys
from typing import Dict, Tuple, Union


def log_line_extractor(line: str) -> Union[None, Tuple[str, str]]:
    """validate and extract data from log line
    Line Format: <IP> - [DATE] "GET /projects/260 HTTP/1.1" <code> <size>

    Returns:
        Extracted data as a tuple of (code, size) or None if line is invalid"""
    results = re.findall(
        r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\]"
        + r" \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$",
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
    fileSize: int = 0
    codes: Dict[str, int] = dict()
    counter = 0

    try:
        for line in sys.stdin:
            results = log_line_extractor(line)
            if not results:
                continue
            code, size = results
            fileSize += int(size)

            if code not in codes:
                codes[code] = 0
            codes[code] = codes[code] + 1

            if counter == 10:
                print_stats(fileSize, codes)
                counter = 0
            else:
                counter += 1
    except KeyboardInterrupt:
        print_stats(fileSize, codes)
        sys.exit(0)

    if counter:
        print_stats(fileSize, codes)
