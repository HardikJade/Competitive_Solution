from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


def f(index, target, arr, dp):
    # Base Case
    # -----------------------
    if (target == 0):
        return True
    elif index == 0:
        return True if arr[0] == target else False
    # -----------------------

    # Memo Code
    # -----------------------
    if dp[index][target] != None:
        return dp[index][target]
    # -----------------------

    # Recursion
    # -----------------------
    else:
        take = False
        not_take = f(index-1, target, arr, dp)
        if arr[index] <= target:
            take = f(index-1, target-arr[index], arr, dp)
        dp[index][take] = take or not_take
        return take or not_take
    # -----------------------
    pass

def f(index, target, arr):
    dp = [[False] * (target+1) for _ in range(index)]
    # Base Case
    # --------------------------
    for i in range(len(dp)):
        dp[i][0] = True    
    if arr[0] <= len(dp[0]):
        dp[0][arr[0]] = True
    # --------------------------

    # Recursion Code
    # --------------------------
    for i in range(1, index):
        for j in range(1, target+1):
            not_take = dp[i-1][j]
            take = False
            if arr[i] <= j:
                take = dp[i-1][j-arr[i]]
            dp[i][j] = take or not_take
    # --------------------------
    return (dp[index-1][target])

def canPartition(arr, n):
    sum_of_arr = sum(arr)
    if (sum_of_arr % 2 == 0):
        half_of_sum = int(sum_of_arr/2)
        return f(n-1, half_of_sum, arr)
    else:
        return False


test = int(input())
while (test):
    test = test - 1
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(canPartition(arr, n))
