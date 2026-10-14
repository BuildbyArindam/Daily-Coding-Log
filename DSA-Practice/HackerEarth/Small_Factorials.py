"""
Problem   : Small Factorials
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/small-factorials/
Difficulty: Easy
Topics    : Math, Big Integers
Date      : 2026-10-14

Approach:
    For each test case, read N and print N! using math.factorial.
    Python's arbitrary-precision integers handle the large results
    without any manual big-number logic.

Complexity (per test case):
    Time  : O(N) big-integer multiplications, roughly O(N * D) where D is
            the number of digits in N!
    Space : O(D) to store the result
"""


# -------------------------------------------------- Solution -------------------------------------------------------------


import math

T = int(input())
for _ in range(T):
    N = int(input())
    print(math.factorial(N))
