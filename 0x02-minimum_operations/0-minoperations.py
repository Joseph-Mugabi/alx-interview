#!/usr/bin/python3
"""
calculates the fewest number of operations
"""


def num_oper_s(num):
    """ calc fewest number of operations"""
    i = 1
    list_oper_s = []
    value = num
    while value != 1:
        i += 1
        if value % i == 0:
            while (value % i == 0 and value != 1):
                value /= i
                list_oper_s.append(i)

    return list_oper_s


def minOperations(n):
    """returns sum of  max num of operations"""
    if n < 2 or type(n) is not int:
        return 0
    return sum(num_oper_s(n))
