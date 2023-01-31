from os import *
from sys import *
from collections import *
from math import *


def f(arr):
    size = len(arr)
    dp = [arr[0]]
    # ---------------------------
    for i in range(1, size):
        pick = -99999999999999999999999999
        notPick = 0 + dp[i-1]
        if ((i - 2) == 0):
            pick = arr[0] + arr[i]
        elif ((i-2) < 0):
            pick = 0 + arr[i]
        else:
            pick = dp[i-2] + arr[i]
        dp.append(max(pick, notPick))
    # ---------------------------
    return dp.pop()


def houseRobber(valueInHouse):
    if len(valueInHouse) == 1:
        return valueInHouse[0]
    else:
        without_first = f(valueInHouse[1:])
        without_last = f(valueInHouse[:-1])
        return (max(without_first, without_last))

testCase = int(input())
while (testCase != 0):
    testCase = testCase - 1
    size = int(input())
    arr = list(map(int, input().split(" ")))
    print(houseRobber(arr))