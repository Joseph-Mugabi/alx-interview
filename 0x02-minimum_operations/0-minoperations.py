#!/usr/bin/python3
"""
calculates the fewest number of operations
>= float('inf') or type(n) is not int
"""
import math


def minOperations(n):
    """ calculates the fewest number of operations """
    ncopy_oper_s = 0
    npaste_oper_s = 0

    if n <= 1:
        return 0

    while n > 1:
        maxm_num_oper_s = 0
        module_list = []
        for i in range(1, n):
            if n % i == 0:
                module_list.append(i)

        maxm_num_oper_s = max(module_list)
        ncopy_oper_s += 1
        npaste_oper_s += ((n // maxm_num_oper_s) - 1)

        n = maxm_num_oper_s

    sum = ncopy_oper_s + npaste_oper_s
    return sum
