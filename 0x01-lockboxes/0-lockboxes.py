#!/usr/bin/python3
"""
Lockboxes interview question
"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened

    Args:
        boxes (list): list of boxes and the box is a list of keys(numbers)

    Return:
        True if all boxes can be opened otherwise False

    Examples:
        >>> canUnlockAll([[1], [2], [3], [4], []])
        True

        >>> canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1],
        >>> [6]])
        True

        >>> canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
        False
    """
    if type(boxes) is not list:
        return False

    totalItems = len(boxes)
    openedBoxes = set([])
    collectedKeys = set([0])

    while len(collectedKeys):
        # get the next key
        key = collectedKeys.pop()

        # ignore the key if it has no box or it was used
        if key >= totalItems or key in openedBoxes:
            continue

        # open the box and collect the keys inside
        openedBoxes.add(key)
        for key in boxes[key]:
            collectedKeys.add(key)

    return len(openedBoxes) == totalItems
