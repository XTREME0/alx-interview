#!/usr/bin/python3
"""Making Change Program"""


def make_change(c, t):
    """calc the number of coins needed"""
    if t <= 0:
        return 0

    current_t = 0
    used_c = 0
    c = sorted(c, reverse=True)
    for coin in c:
        r = (total - current_t) // coin
        current_t += r * coin
        used_c += r
        if current_t == t:
            return used_c
    return -1
