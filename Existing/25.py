import sys
from math import *
from collections import *
from os import *
from sys import *
sys.setrecursionlimit(10**7)
mod = 1000000007


def f(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    ans = 0
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
            if s1[i1-1] == s2[i2-1]: 
                result = 1 + dp[i1-1][i2-1]
                ans = max(ans,result)
                dp[i1][i2] = result
            else:
                dp[i1][i2] = 0     
    # --------------------------
    return ans


def lcs(str1, str2):
    return f(str1, str2)


test = int(input())
while (test):
    test = test - 1
    s1, s2 = list(map(str, input().strip().split(' ')))
    print(lcs(s1, s2))
