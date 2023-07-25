#!/usr/bin/env python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    bytes_to_follow = 0

    for byte in data:
        if bytes_to_follow > 0:
            if (byte >> 6) != 0b10:
                return False
            bytes_to_follow -= 1
        else:
            if (byte >> 7) == 0b0:
                bytes_to_follow = 0
            elif (byte >> 5) == 0b110:
                bytes_to_follow = 1
            elif (byte >> 5) == 0b1110:
                bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_follow = 3
            else:
                return False

    return bytes_to_follow == 0
