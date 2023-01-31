from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)
mod = 1000000007
INF = 99999999999999999


def f(i, j, height, arr, dp):
    # Base Case
    # ------------------------
    if i == height:
        return arr[i][j]
    # ------------------------

    # Memo Code
    # ------------------------
    if dp[i][j] != -1:
        return dp[i][j]
    # ------------------------

    # Recursion Code
    # ------------------------
    else:
        bottom = INF
        diagonal = INF
        if i+1 <= height:
            bottom = arr[i][j] + f(i+1, j, height, arr, dp)
            diagonal = arr[i][j] + f(i+1, j+1, height, arr, dp)
            dp[i][j] = min(bottom, diagonal)
            return dp[i][j]
        else:
            return INF
    # ------------------------


def minimumPathSum(triangle, n):
    dp = [[-1] * n for _ in range(n)]
    return (f(0, 0, n-1, triangle, dp))


test = int(input())
while (test):
    test = test - 1
    height = int(input())
    triangle = []
    for i in range(height):
        row = list(map(int, input().split(" ")))
        triangle.append(row)
    print(minimumPathSum(triangle, height))
