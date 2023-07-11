#!/usr/bin/python3
"""
calculates the fewest number of operations
"""
import math


def minOperations(n):
    """ calculates the fewest number of operations
    needed to result in exactly n H characters in the file
    returns an int"""
    if not isinstance(n, int) or n < 2:
        return 0

    ncopy_oper_s = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            ncopy_oper_s += i
            n //= i
        if n > 1:
            ncopy_oper_s += n
        return ncopy_oper_s
