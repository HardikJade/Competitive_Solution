from os import *
from sys import *
from collections import *
from math import *
import sys
from typing import List
sys.setrecursionlimit(10**7)

mod = 1000000007

INF = 99999999999999999999999999999999


def f(index, target, arr, dp):
    # Base Case
    # -------------
    if (index < 0):
        if (target % arr[0] == 0):
            return int(target/arr[0])
        else:
            return INF
    # -------------
    if (dp[index][target] != None):
        return dp[index][target]
    
    else:
        take = INF
        not_take = f(index-1, target, arr, dp)
        if target - arr[index] >= 0:
            take = 1 + f(index, target-arr[index], arr, dp)
        dp[index][target] = min(take, not_take)
        return dp[index][target]


def minimumElements(num: List[int], x: int) -> int:
    dp = [[None] * (x + 1) for _ in range(len(num))]
    ans = f(len(num) - 1, x, num, dp)
    if ans >= INF:
        return -1
    else:
        return ans


test = int(input())
while (test):
    test = test - 1
    n, target = list(map(int, stdin.readline().strip().split(" ")))
    arr = list(map(int, stdin.readline().strip().split(" ")))
    print(minimumElements(arr, target))
