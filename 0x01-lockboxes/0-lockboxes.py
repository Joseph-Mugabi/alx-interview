#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """initialize the  boxes
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]

    i = 0
    while i < len(keys):  # loop through the list of keys
        if keys[i] < n and not unlocked[keys[i]]:
            unlocked[keys[i]] = True
            keys += boxes[keys[i]]

        i += 1

    return all(unlocked)
