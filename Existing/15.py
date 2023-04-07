from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

INF = 9999999999999999999999999


def f(index, target, arr):
    dp = [[False]*(target+1) for _ in range(index)]
    # Base Case
    # -----------------------------------------
    for i in range(index):
        dp[i][0] = True
    if (len(dp[0]) >= arr[0]):
        dp[0][arr[0]] = True
    # -----------------------------------------

    # Recursion Code
    # -----------------------------------------
    for i in range(1, index):
        for j in range(1, target+1):
            take = False
            not_take = dp[i-1][j]
            if (j-arr[i] >= 0):
                take = dp[i-1][j - arr[i]]
            dp[i][j] = take or not_take
    # -----------------------------------------
    return dp


def minSubsetSumDifference(arr, n):
    total_sum = sum(arr)
    dp = f(n, total_sum, arr)
    minimum_diff = INF
    for index, possible in enumerate(dp[n-1]):
        if (possible):
            S1 = index
            S2 = total_sum - index
            diff = abs(S1-S2)
            minimum_diff = min(minimum_diff, diff)
    return(minimum_diff)

# Taking input using fast I/0.


def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    ans = minSubsetSumDifference(arr, N)
    stdout.write(str(ans) + "\n")
    tc -= 1
