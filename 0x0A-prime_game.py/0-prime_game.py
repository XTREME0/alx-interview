#!/usr/bin/python3

""" Prime Game ! """


def isWinner(x, nums):
    """ is Winner func """
    if not nums or x < 1:
        return None
    n = max(nums)
    g = [True for _ in range(max(n + 1, 2))]
    for a in range(2, int(pow(n, 0.5)) + 1):
        if not g[a]:
            continue
        for b in range(a * a, n + 1, a):
            g[b] = False
    g[0] = g[1] = False
    d = 0
    for a in range(len(g)):
        if g[a]:
            d += 1
        g[a] = d
    mar1 = 0
    for n in nums:
        mar1 += g[n] % 2 == 1
    if mar1 * 2 == len(nums):
        return None
    if mar1 * 2 > len(nums):
        return "Maria"
    return "Ben"
