from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)
mod = 1000000007

def f(current,dp):
    # base case
    # ****************************************************
    if current <= 1:
        return current
    else:
        if dp[current] != -1:
            return dp[current]
        else:
            one_step = f(current - 1,dp)
            two_step = f(current - 2,dp)
            result = one_step + two_step
            dp[current] = result
            return result
    # ****************************************************


def countDistinctWays(nStairs: int) -> int:
    dp = [-1] * (nStairs + 1)
    return(f(nStairs,dp))


test = int(input())
while(test):
    test = test -1
    n = int(input())
    print(countDistinctWays(n))
