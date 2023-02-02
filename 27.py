from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**2)
mod = 1000000007


def f(i1, i2, s1, s2, dp):
    # Base Case
    # ---------------------
    if i1 < 0 or i2 < 0:
        return 0
    # ---------------------

    # Memo Code
    # ---------------------
    if dp[i1][i2] != -1:
        return dp[i1][i2]
    # ---------------------

    # Recursion Code
    # ---------------------
    if s1[i1] == s2[i2]:
        dp[i1][i2] = 1 + f(i1-1, i2-1, s1, s2, dp)
        return dp[i1][i2]

    dp[i1][i2] = max(f(i1-1, i2, s1, s2, dp), f(i1, i2-1, s1, s2, dp))
    return dp[i1][i2]
    # ---------------------


def minInsertion(str):
    n = len(str)
    dp = [[-1] * n for _ in range(n)]
    len_of_palindrome = f(n-1, n-1, str, str[::-1], dp)
    return n - len_of_palindrome


test = int(input())
while (test):
    test = test - 1
    str = input().strip()
    print(minInsertion(str))
