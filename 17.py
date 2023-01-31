from os import *
from sys import *
from collections import *
from math import *
from typing import List
import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


def f(index, target, arr, dp):
    # Base Case
    # --------------------
    if index == 0:
        if (target == 0 and arr[0] == 0):
            return 2
        if (target == 0 or target == arr[0]):
            return 1
        else:
            return 0
    # --------------------

    # Memo
    # --------------------
    if dp[index][target] != -1:
        return dp[index][target]
    # --------------------

    # Recursion Code
    # --------------------
    else:
        take = 0
        not_take = f(index-1, target, arr, dp)
        if (target - arr[index] >= 0):
            take = f(index-1, target-arr[index], arr, dp)
        dp[index][target] = (take + not_take) % mod
        return dp[index][target]
    # --------------------


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    total_sum = sum(arr)
    if (total_sum - d) < 0 or ((total_sum-d) % 2):
        return 0
    else:
        required_sum = int((total_sum - d) / 2)
        dp = [[-1] * (required_sum + 1) for _ in range(n)]
        return f(n-1, required_sum, arr, dp)

test = int(input())
while (test):
    test = test - 1
    n, diff = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    print(countPartitions(n, diff, arr))
