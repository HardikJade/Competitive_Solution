from typing import List
from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


def f(index, target, arr,dp):
    # Base Case
    # ------------------------------------------
    if (index == 0):
        if (target == 0 and arr[0] == 0): return 2
        if (target == 0 or arr[0] == target): return 1
        return 0
    # ------------------------------------------
    
    # Memo Code
    # ------------------------------------------
    if (dp[index][target] != -1):
        return dp[index][target]
    # ------------------------------------------

    # Recursion Code
    # ------------------------------------------
    else:
        take = 0
        not_take = f(index-1,target,arr,dp)
        if (target - arr[index] >= 0):
            take = f(index-1,target-arr[index],arr,dp)
        dp[index][target] = take + not_take
        return dp[index][target]
    # ------------------------------------------


def targetSum(arr: List[int], target: int) -> int:
    total_sum = sum(arr)
    diff = target
    S2 = total_sum - diff
    if (
        (S2) >= 0
        and
        ((S2 % 2) == 0)
    ):
        required_sum = int((S2) / 2)
        index = len(arr) - 1
        dp = [[-1] * (required_sum + 1) for _ in range(len(arr) +1 )]
        return f(index, required_sum, arr,dp)
    else:
        return 0


test = int(input())
while (test):
    test = test - 1
    num, target = list(map(int, input().strip().split(' ')))
    arr = list(map(int, input().strip().split(' ')))
    print(targetSum(arr, target))
