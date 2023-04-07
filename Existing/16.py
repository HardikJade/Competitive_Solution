from typing import List
from os import *
from sys import *
from collections import *
from math import *
import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


def f(index, target, arr, dp):
    # Base Case:
    # -------------------------
    if index == 0:
        if target == 0 and arr[0] == 0: return 2
        if (target == 0 or arr[0] == target): return 1
        return 0
    # -------------------------

    # Memo Code
    # -------------------------
    elif dp[index][target] != -1: return dp[index][target]
    # -------------------------

    # Recursion Code
    # -------------------------
    else:
        take = 0
        not_take = f(index-1, target, arr, dp)
        if (target >= arr[index]): take = f(index-1, target-arr[index], arr, dp)
        dp[index][target] = take+not_take
        return dp[index][target]
    # -------------------------


def findWays(num: List[int], tar: int) -> int:
    dp = [[-1] * (tar + 1) for _ in range(len(num))]
    return f(len(num) - 1, tar, num, dp)


test = int(input())
while (test):
    test -= 1
    num, target = list(map(int, input().split(' ')))
    arr = list(map(int, input().split(' ')))
    print(findWays(arr, target))
