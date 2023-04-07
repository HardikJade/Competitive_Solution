from os import *
from sys import *
from collections import *
from math import *
from typing import *

import sys
sys.setrecursionlimit(10**7)
mod = 1000000007


def frogJump(n: int, heights: List[int]) -> int:
    pass


test = int(input())
while(test):
    test = test - 1
    n = int(input())
    arr = list(map(int,input().strip().split(' ')))
    print(frogJump(n,arr))
