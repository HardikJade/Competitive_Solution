from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


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


def canYouMake(s: str, p: str) -> int:
    n = len(s)
    m = len(p)
    dp = [[-1] * m for _ in range(n)]
    len_of_sub = f(n-1, m-1, s, p, dp)
    return (n + m - (2*len_of_sub))


test = int(input())
while (test):
    test = test - 1
    s, p = list(map(str, input().strip().split(' ')))
    print(canYouMake(s, p))
