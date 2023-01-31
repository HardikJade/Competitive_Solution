from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)

INF = 999999999999999999


def f(m, n, x, y, arr, dp):
    # Base Case
    # -----------------------------------
    if (x == 0 and y == 0):
        return arr[0][0]
    # -----------------------------------

    # Memo Code:
    # -----------------------------------
    if dp[x][y] != -1:
        return dp[x][y]
    # -----------------------------------

    # Recursion Code
    # -----------------------------------
    up = INF
    left = INF
    if x-1 >= 0:
        up = arr[x][y] + f(m, n, x-1, y, arr, dp)
    if y-1 >= 0:
        left = arr[x][y] + f(m, n, x, y-1, arr, dp)
    dp[x][y] = min(left, up)
    return min(left, up)
    # -----------------------------------


def minSumPath(m, n, grid):
    dp = [[-1] * n for _ in range(m)]
    return f(m-1, n-1, m-1, n-1, grid, dp)


# Main.
t = int(input())
while (t > 0):
    l = list(map(int, input().split()))
    n, m = l[0], l[1]
    grid = []
    for i in range(n):
        ll = list(map(int, input().split()))
        grid.append(ll)
    print(minSumPath(n, m, grid))
    t -= 1
