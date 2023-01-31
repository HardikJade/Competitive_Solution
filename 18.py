from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


def f(index, capacity, weight, value, dp):
    # Base Case
    # -----------------------
    if (index < 0):
        return 0
    # -----------------------

    # Recursion Code
    # -----------------------
    if (dp[index][capacity] != None):
        return dp[index][capacity]
    # -----------------------

    else:
        take = 0
        not_take = 0 + f(index-1, capacity, weight, value, dp)
        if (capacity - weight[index] >= 0):
            take = value[index] + \
                f(index-1, capacity-weight[index], weight, value, dp)
        dp[index][capacity] = max(take, not_take)
        return dp[index][capacity]


def solveKnapSack(weight, val, W, n):
    dp = [[None] * (W + 1) for _ in range(n)]
    return f(n-1, W, weight, val, dp)


test = int(input())
while (test):
    test = test - 1
    n = int(input())
    weight = list(map(int, stdin.readline().strip().split(" ")))
    value = list(map(int, stdin.readline().strip().split(" ")))
    capacity = int(input())
    print(solveKnapSack(weight, value, capacity, n))
