"""
Problem   : Multiplication (Recursive)
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/multiplication-recursive_624385?kunjiRedirection=true
Date      : 2026-08-28
Difficulty: Easy
Topics    : Recursion, Math

Approach:
    Compute M * N recursively via repeated addition — multiply(M, N) = M + multiply(M, N-1),
    with multiply(M, 0) = 0 as the base case. N recursive calls are made, each adding M once.

Time Complexity : O(N)  — one recursive call per unit decrease in N
Space Complexity: O(N)  — recursion call stack depth of N
"""


# ---------------------------- Solution -------------------------------------


from math import *
from collections import *
from sys import *
from os import *
setrecursionlimit(10000)

def multiply(M, N):
    if N == 0:
        return 0
    return M + multiply(M, N - 1)
M = int(input())
N = int(input())
print(multiply(M, N))
