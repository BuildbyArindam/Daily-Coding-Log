"""
Problem   : Find Numbers Containing 1, 2, and 3
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/find-numbers-containing-1-2-and-3_1214521
Date      : 2026-08-31
Difficulty: Easy
Topics    : Arrays, String Manipulation, Digit Checking

Approach:
    For each number in the array, convert it to a string and check whether
    the digits '1', '2', and '3' all appear in it (order doesn't matter).
    Collect qualifying numbers, sort the result. If none qualify, return [-1].

Time Complexity : O(n * d log d) -> effectively O(n * d), where d = avg digit length
                   (checking membership of 3 chars in a short string is O(d);
                   the sort of results dominates asymptotically at O(n log n))
Space Complexity: O(n) for the result list
"""


# ----------------------------- Solution ----------------------------------


from os import *
from sys import *
from collections import *
from math import *

def containsNumber(n, arr):
    result = []
    for num in arr:
        s = str(num)
        if '1' in s and '2' in s and '3' in s:
            result.append(num)
    result.sort()
    if len(result) == 0:
        return [-1]
    return result
