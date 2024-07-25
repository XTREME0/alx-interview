#!/usr/bin/python3
""" making_change problem """
from typing import List


def makeChange(c: List[int], t: int) -> int:
    """
    function: makeChange
    args: coins -> List[int], total: int
    """
    if t <= 0:
        return 0

    sorted_c = sorted(c, reverse=True)
    counter = 0
    copy_t = t

    for coin in sorted_c:
        if coin <= copy_t:
            count = copy_t // coin
            copy_t -= coin * count
            counter += count
        if copy_t == 0:
            break

    if copy_t != 0:
        return -1

    return counter
