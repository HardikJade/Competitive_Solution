from os import *
from sys import *
from collections import *
from math import *


def f(index, capacity, weight, value, dp):
    # Base Case
    # ------------------------
    if capacity == 0:
        return 0
    if index == 0:
        if (capacity >= weight[0]):
            return value[0] * int(capacity/weight[0])
        return 0
    # ------------------------

    # Memo Code
    # ------------------------
    if(dp[index][capacity] != -1):
        return dp[index][capacity]
    # ------------------------

    # Recursion Code
    # ------------------------
    else:
        take = 0
        not_take = f(index-1, capacity, weight, value, dp)
        if capacity - weight[index] >= 0:
            take = value[index] + \
                f(index, capacity-weight[index], weight, value, dp)
        dp[index][capacity] = max(take, not_take)
        return dp[index][capacity]
    # ------------------------


def unboundedKnapsack(n, w, profit, weight):
    dp = [[-1] * (w + 1) for _ in range(n)]
    return f(n-1, w, weight, profit, dp)


test = int(input())
while (test):
    test = test - 1
    num, capacity = list(map(int, input().strip().split(' ')))
    value = list(map(int, input().strip().split(' ')))
    weight = list(map(int, input().strip().split(' ')))
    print(unboundedKnapsack(num, capacity, value, weight))
