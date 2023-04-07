from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)

def f(m, n, x, y, arr, dp):
    # Base Case
    # ---------------------------------
    if (
        (x > 0 and y > 0)
        and
        (arr[x][y] == -1)
    ):
        return 0
    if x == 0 and y == 0:
        return 1
    # ---------------------------------

    # Memo Code
    # ---------------------------------
    if (dp[x][y] != -1):
        return dp[x][y]
    # ---------------------------------

    # Recursion Code
    # ---------------------------------
    up = 0
    left = 0
    if x - 1 >= 0:
        up = f(m, n, x-1, y, arr, dp)
    if y-1 >= 0:
        left = f(m, n, x, y-1, arr, dp)
    dp[x][y] = up + left
    return up + left
    # ---------------------------------


def mazeObstacles(m, n, mat):
    dp = [[-1] * n for _ in range(m)]
    return (f(m-1, n-1, m-1, n-1, mat, dp))


test = int(input())
while (test):
    test = test - 1
    m, n = list(map(int, input().split(" ")))
    arr = []
    for i in range(m):
        temp = list(map(int, input().split(' ')))
        arr.append(temp)
    print(mazeObstacles(m, n, arr))
