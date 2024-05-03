#!/usr/bin/python3
""" My solution for stats log parser """

import sys
import signal
import re
from typing import Generator, Dict


class LogLine:
    """ Log line object """
    RE_TEMP = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                         r' - \[[^\]]+\] ".*?" (\d{3}) (\d+)')

    def __init__(self, status: int, size: int):
        """ Initialize a LogLine object """
        self._status = int(status)
        self._size = int(size)

    @staticmethod
    def fromLine(line: str) -> "LogLine":
        """ Parse a log line and return a LogLine object """
        results = LogLine.RE_TEMP.match(line.strip())
        return LogLine(*results.groups())

    @property
    def size(self) -> int:
        """ Return the size of the response file in bytes """
        return self._size

    @property
    def status(self) -> int:
        """ Return the status code of the response """
        return self._status


class StatisticsManager:
    """ Statistics manager object
    Trace all log lines and print statistics for each request """

    def __init__(self):
        """ Initialize a StatisticsManager object """
        self._total_size = 0
        self._codes: Dict[int, int] = {}
        self._counter = 0

    @property
    def total_size(self) -> int:
        """ Return the total size of all requests in bytes """
        return self._total_size

    @property
    def codes(self) -> Dict[int, int]:
        """ Return a dictionary of status codes and their count """
        return {**self._codes}

    @property
    def counter(self) -> int:
        """ Return the number of processed log lines """
        return self._counter

    def readLogLine(self, line: LogLine):
        """ Read a log line and update statistics """
        self._total_size += line.size

        if line.status in self._codes:
            self._codes[line.status] += 1
        else:
            self._codes[line.status] = 1

        self._counter += 1

    def reset(self):
        """ Reset statistics """
        self._total_size = 0
        self._counter = 0
        self._codes = {}

    def print(self):
        """ Print statistics """
        sorted_codes = sorted(self._codes.items(), key=lambda x: x[0])
        print(f'File size: {self.total_size}', flush=False)
        for code, count in sorted_codes:
            print(f'{code}: {count}', flush=False)
        sys.stdout.flush()


if __name__ == "__main__":
    manager = StatisticsManager()

    try:
        for line in sys.stdin:
            if not line:
                raise EOFError()
            try:
                line = LogLine.fromLine(line)
            except AttributeError:
                continue
            manager.readLogLine(line)

            if manager.counter >= 10:
                manager.print()
                manager.reset()
    finally:
        if manager.counter > 0:
            manager.print()
