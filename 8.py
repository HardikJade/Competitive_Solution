from os import *
from sys import *
from collections import *
from math import *


def f(m, n, x, y, dp):
    # Base Case
    # ----------------------------------
    if (x == 0 and y == 0):
        return 1
    # ----------------------------------
    else:
        # Memo
        # ----------------------------------
        if dp[x][y] != -1:
            return dp[x][y]
        # ----------------------------------

        left = 0
        up = 0
        if x - 1 >= 0:
            up = f(m, n, x-1, y, dp)
        if y-1 >= 0:
            left = f(m, n, x, y-1, dp)
        dp[x][y] = left + up
        return dp[x][y]


def uniquePaths(m, n):
    dp = [[-1] * n for _ in range(m)]
    return f(m-1, n-1, m-1, n-1, dp)


test = int(input())
while (test):
    test = test - 1
    m, n = list(map(int, input().split(" ")))
    print(uniquePaths(m, n))
    # uniquePaths(m, n)
