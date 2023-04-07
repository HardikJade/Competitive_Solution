from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


def f(index, target, arr,dp):
    # Base Case
    # -----------------------
    if (target == 0): return 1
    if(index == 0): 
        if (target % arr[0] == 0): return 1
        else: return 0
    # -----------------------

    # Memo Code
    # -----------------------
    if (dp[index][target] != -1):
        return dp[index][target]
    # -----------------------
    
    # Recursion Code
    # -----------------------
    else:
        take = 0
        not_take = f(index-1,target,arr,dp)
        if(target - arr[index] >= 0):
            take = f(index,target-arr[index],arr,dp)
        dp[index][target] = take + not_take
        return dp[index][target]
    # -----------------------


def countWaysToMakeChange(denominations, value):
    n = len(denominations)
    dp = [[-1] * (value + 1) for _ in range(n)]
    return f(n-1, value, denominations, dp)


def takeInput():
    numDenominations = int(input())
    denominations = list(map(int, stdin.readline().strip().split(" ")))
    value = int(input())
    return denominations, numDenominations, value

# main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))
