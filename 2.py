from os import *
from sys import *
from collections import *
from math import *
from typing import *

import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


def f(current,arr,dp):
    # base case
    if current == 0:
        return 0
    else:
        if dp[current] != -1:
            return dp[current]
        one_step = f(current - 1,arr,dp) + abs(arr[current] - arr[current - 1])
        second_step = mod
        if current - 2 >= 0:
            second_step = f(current - 2,arr,dp) + abs(arr[current] - arr[current - 2])
        result = min(one_step,second_step)
        dp[current] = result
        return result

def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1] * (n + 1)
    return f(n-1,heights,dp)


test = int(input())
while(test):
    test = test - 1
    n = int(input())
    arr = list(map(int,input().strip().split(' ')))
    print(frogJump(n,arr))
