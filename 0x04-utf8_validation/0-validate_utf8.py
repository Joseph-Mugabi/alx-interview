#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    state_of_bytes = 0
    for num in data:
        bit = 0b10000000
        if not state_of_bytes:
            while (bit & num):
                state_of_bytes += 1
                bit >>= 1
            if state_of_bytes > 4:
                return False
            elif state_of_bytes:
                state_of_bytes -= 1
                if state_of_bytes == 0:
                    return False
        elif state_of_bytes > 0:
            if num >> 6 != 2:
                return False
            state_of_bytes -= 1
    return not state_of_bytes
