#!/usr/bin/python3
""" My solution for stats log parser """

import sys
import signal
import re
from typing import Generator, Dict


class InvalidLogLine(Exception):
    """ Exception raised when invalid log line is parsed """
    pass


class LogLine:
    """ Log line object """
    RE_TEMP = re.compile(r'.*(\d{3}) (\d+)$')

    def __init__(self, status: int, size: int):
        """ Initialize a LogLine object """
        self._status = int(status)
        self._size = int(size)

    @staticmethod
    def fromLine(line: str) -> "LogLine":
        """ Parse a log line and return a LogLine object """
        line = line.strip()
        if not line:
            raise InvalidLogLine()

        line = line.split()[::-1]
        if len(line) < 2:
            raise InvalidLogLine()

        try:
            size = int(line[0])
        except Exception:
            size = 0

        try:
            status = int(line[1])
        except Exception:
            status = -1

        return LogLine(status, size)

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
        self._codes = {}
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

    def resetCounter(self):
        """ Reset the number of processed log lines """
        self._counter = 0

    def readLogLine(self, line: LogLine):
        """ Read a log line and update statistics """
        self._counter += 1
        self._total_size += line.size

        if line.status == -1:
            return
        if line.status in self._codes:
            self._codes[line.status] += 1
        else:
            self._codes[line.status] = 1

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
            except InvalidLogLine:
                continue
            manager.readLogLine(line)

            if manager.counter >= 10:
                manager.print()
                manager.resetCounter()
    finally:
        if manager.counter > 0:
            manager.print()
