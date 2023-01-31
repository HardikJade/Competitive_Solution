from typing import *


def f(index: int, arr: List[List[int]], prev: int, dp: List[List[int]]) -> int:
    # Base Case
    # -----------------------------------
    if (index == 0):
        if prev == 0:
            return max(arr[0][1], arr[0][2])
        elif prev == 1:
            return max(arr[0][0], arr[0][2])
        elif prev == 2:
            return max(arr[0][0], arr[0][1])
        elif prev == 3:
            return max(arr[0][0], arr[0][1], arr[0][2])
    # -----------------------------------
    else:
        # Memoization
        # -----------------------------------
         if dp[index][prev] != -1:
             return dp[index][prev]
        # -----------------------------------

        if prev == 0:
            first = f(index-1, arr, 1, dp) + arr[index][1]
            second = f(index-1, arr, 2, dp) + arr[index][2]
            dp[index][0] = max(first, second)
            print(dp[index][prev])
            return max(first, second)
        elif prev == 1:
            zeroth = f(index-1, arr, 0, dp) + arr[index][0]
            second = f(index-1, arr, 2, dp) + arr[index][2]
            dp[index][1] = max(zeroth, second)
            print(dp[index][prev])
            return max(zeroth, second)
        elif prev == 2:
            zeroth = f(index-1, arr, 0, dp) + arr[index][0]
            first = f(index-1, arr, 1, dp) + arr[index][1]
            dp[index][prev] = max(zeroth, first)
            print(dp[index][prev])
            return max(zeroth, first)
        elif prev == 3:
            zeroth = f(index-1, arr, 0, dp) + arr[index][0]
            first = f(index-1, arr, 1, dp) + arr[index][1]
            second = f(index-1, arr, 2, dp) + arr[index][2]
            dp[index][prev] = max(zeroth, first, second)
            print(dp[index][prev])
            return max(zeroth, first, second)


def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1] * 4 for _ in range(n)]
    return f(n-1, points, 3, dp)


test = int(input())
while (test):
    test = test - 1
    size = int(input())
    arr = []
    for i in range(size):
        temp = input()
        temp = list(map(int, temp.split(' ')))
        arr.append(temp)
    print(ninjaTraining(size, arr))
