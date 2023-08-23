#!/usr/bin/python3
"""
making change by counting the number of coins
"""


def makeChange(coins, total):
    """counting, find the number of coins needed
    Time complexity is of bigO OF nlogn
    """
    if total <= 0:
        return 0

    i = 0  # counter to  keep track of e no of coins used
    coins.sort(reverse=True)  # sort coins in desc order
    for coin in coins:
        increment = int(total/coin)  # determne hw mny tms e cur coin fits
        # into the remaining total
        # update remaining total aftr using e cur coin
        total -= (increment * coin)
        i += increment  # increase e counter with e no of coins used

        if total == 0:
            return i  # return no of coins used if total amount is met

    return -1  # return -1 if total cannot be me with e available cons
