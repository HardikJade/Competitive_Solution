from sys import stdin
from os import *
from sys import *
from collections import *
from math import *
import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


def f(i1, i2, s1, s2, dp):
    # Base Case
    # -------------------------------------------
    if (i1 < 0 or i2 < 0):
        return 0
    # -------------------------------------------

    # Memo Code
    # -------------------------------------------
    if dp[i1][i2] != -1:
        return dp[i1][i2]
    # -------------------------------------------

    # Recursive Code
    # -------------------------------------------
    else:
        if s1[i1] == s2[i2]:
            dp[i1][i2] = 1 + f(i1-1, i2-1, s1, s2, dp)
            return dp[i1][i2]
        else:
            dp[i1][i2] = max(f(i1-1, i2, s1, s2, dp), f(i1, i2-1, s1, s2, dp))
            return dp[i1][i2]
    # -------------------------------------------


def f(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    dp = [[-1] * (l2 + 1) for _ in range(l1 + 1)]
    # Base Case:
    # --------------------------
    for i in range(l1 + 1): dp[i][0] = 0
    for i in range(1,l2 + 1): dp[0][i] = 0
    # --------------------------

    # Recursion Code
    # --------------------------
    for i1 in range(1,l1+1):
        for i2 in range(1,l2 + 1):
            if s1[i1-1] == s2[i2-1]: dp[i1][i2] = 1 + dp[i1-1][i2-1]
            else: dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])        
    # --------------------------
    return dp[l1][l2]


def lcs(s, t):
    i1 = len(s)
    i2 = len(t)
    # dp = [[-1] * (i2 + 1) for _ in range(i1+1)]
    # return f(i1 - 1, i2 - 1, s, t, dp)
    return f(s, t)


s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())
print(lcs(s, t))
