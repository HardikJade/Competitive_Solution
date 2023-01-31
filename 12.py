from os import *
from sys import *
from collections import *
from math import *
import sys
sys.setrecursionlimit(10**7)
mod = 1000000007

INF = -9999999999999999999999999999


def f(m, n, x, y, arr, dp):
    # Base Case
    # ----------------------
    if x == 0:
        return arr[0][y]
    # ----------------------

    # Memo Code
    # ----------------------
    if (dp[x][y] != -1):
        return dp[x][y]
    # ----------------------

    # Recursion Code
    # ----------------------
    else:
        diagonal_left = INF
        up = INF
        diagonal_right = INF
        if x - 1 >= 0 and y-1 >= 0:
            diagonal_left = arr[x][y] + f(m, n, x-1, y-1, arr, dp)
        if x-1 >= 0:
            up = arr[x][y] + f(m, n, x-1, y, arr, dp)
        if x-1 >= 0 and y+1 <= n:
            diagonal_right = arr[x][y] + f(m, n, x-1, y+1, arr, dp)
        dp[x][y] = max(diagonal_left, up, diagonal_right)
        return dp[x][y]
    # ----------------------


def getMaxPathSum(matrix):
    maxi = INF
    m = len(matrix)
    n = len(matrix[0])
    dp = [[-1] * n for _ in range(m)]
    for i in range(n):
        result = f(m-1, n-1, m-1, i, matrix, dp)
        maxi = max(maxi, result)
    return (maxi)


def takeInput():
    n_x = stdin.readline().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    matrix = [list(map(int, stdin.readline().strip().split(" ")))
              for row in range(n)]
    return matrix, n, m


T = int(input())
while (T > 0):
    T -= 1
    matrix, n, m = takeInput()
    print(getMaxPathSum(matrix))
