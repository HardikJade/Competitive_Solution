from os import *
from sys import *
from collections import *
from math import *
import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


def f(index, rod_length, arr, dp):
    # Base Case
    # -------------------------
    if rod_length == 0:
        return 0
    if index == 0:
        return rod_length * arr[0]
    # -------------------------

    # Memo Code
    # -------------------------
    if(dp[index][rod_length] != -1):
        return dp[index][rod_length]
    # -------------------------

    # Recursion Code
    # -------------------------
    else:
        take = 0
        not_take = f(index-1, rod_length, arr, dp)
        if rod_length - (index + 1) >= 0:
            take = arr[index] + f(index, rod_length-(index+1), arr, dp)
        dp[index][rod_length] = max(take, not_take)
        return dp[index][rod_length]
    # -------------------------


def cutRod(price, n):
    dp = [[-1] * (n+1) for _ in range(n)]
    return f(n-1, n, price, dp)


def takeInput():
    n = int(input())
    price = list(map(int, input().strip().split(" ")))
    return price, n


t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
