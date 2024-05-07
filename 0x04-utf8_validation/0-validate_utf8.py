#!/usr/bin/python3
""" In this module we will learn how to validate UTF-8 encoding """
from typing import List


Bits = List[int]


class UTF8Byte:
    """ Class representing a UTF-8 byte """
    def __init__(self, byte: int):
        self._byte = byte
        self._bits = UTF8Byte.byteToBits(byte)

    @staticmethod
    def byteToBits(byte: int) -> Bits:
        """ Convert a single byte into a list of bits """
        return [((byte >> i) & 1) for i in range(7, -1, -1)]

    @property
    def isSingle(self) -> bool:
        """ Check if the byte is a single byte character (ASCII)

        Examples:
            >>> UTF8Byte(0b10000000).isSingle
            False
            >>> UTF8Byte(0b00000000).isSingle
            True
            >>> UTF8Byte(0b01000000).isSingle
            True
            >>> UTF8Byte(0b11100000).isSingle
            False
        """
        return self._bits[0] == 0

    @property
    def isContinue(self) -> bool:
        """ Check if the byte is a continue byte

        Examples:
            >>> UTF8Byte(0b10000000).isContinue
            True
            >>> UTF8Byte(0b00000000).isContinue
            False
            >>> UTF8Byte(0b11111111).isContinue
            False
            >>> UTF8Byte(0b11000000).isContinue
            False
            >>> UTF8Byte(0b11100000).isContinue
            False
            >>> UTF8Byte(0b10110000).isContinue
            True
            >>> UTF8Byte(0b10111000).isContinue
            True
        """
        return self._bits[0] == 1 and self._bits[1] == 0

    @property
    def isHead(self) -> bool:
        """ Check if the byte is a head byte

        Examples:
            >>> UTF8Byte(0b10000000).isHead
            False
            >>> UTF8Byte(0b00000000).isHead
            False
            >>> UTF8Byte(0b11000000).isHead
            True
            >>> UTF8Byte(0b11100000).isHead
            True
            >>> UTF8Byte(0b11110000).isHead
            True
            >>> UTF8Byte(0b11111000).isHead
            True
            >>> UTF8Byte(0b11111100).isHead
            True
            >>> UTF8Byte(0b11111110).isHead
            False
            >>> UTF8Byte(0b11111111).isHead
            False
        """
        if self._bits[:2] != [1, 1]:
            return False

        for i in self._bits[2:-1]:
            if i == 0:
                return True
        return False

    @property
    def levels(self) -> int:
        """ Get the number of levels in the byte

        Examples:
            >>> UTF8Byte(0b10000000).levels
            -1
            >>> UTF8Byte(0).levels
            0
            >>> UTF8Byte(0b00111000).levels
            0
            >>> UTF8Byte(0b11000000).levels
            1
            >>> UTF8Byte(0b11100000).levels
            2
            >>> UTF8Byte(0b11110000).levels
            3
            >>> UTF8Byte(0b11111000).levels
            4
            >>> UTF8Byte(0b11111100).levels
            5
            >>> UTF8Byte(0b11111110).levels
            -1
            >>> UTF8Byte(0b11111111).levels
            -1
        """
        if self.isSingle:
            return 0
        elif self.isContinue or not self.isHead:
            return -1

        counter = 0
        for i in self._bits[1:-1]:
            if i == 1:
                counter += 1
            else:
                break
        return counter

    def __getitem__(self, index: int) -> int:
        return self._bits[index]


def validUTF8(data: List[int]) -> bool:
    """ Validate a list of bytes is a valid UTF-8 encoding """

    # level: -1 means no char, 0 means head, 1+ means continue
    index, level, maxLevels = 0, -1, -1

    while index < len(data):
        byte = UTF8Byte(data[index])
        index += 1

        if level == -1:
            # any level -1 must be a head or a single byte
            if byte.isSingle:
                continue
            if not byte.isHead:
                return False
            level, maxLevels = 0, byte.levels
            if maxLevels == -1:
                return False
        elif byte.isContinue and level < maxLevels:
            level += 1
            if level == maxLevels:
                level = -1
        else:
            return False
    return level == -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
