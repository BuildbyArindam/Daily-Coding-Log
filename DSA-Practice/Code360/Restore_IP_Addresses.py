"""
Problem   : Restore IP Addresses
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380931
Difficulty: Medium
Date      : 2026-09-17
Topics    : Backtracking, Recursion, Strings

Approach:
Backtrack by choosing 1-3 digit segments at each step, pruning branches early via
a remaining-length bound (remaining < parts_left or remaining > 3*parts_left) so
we never explore combinations that can't possibly complete to 4 valid octets.
Each candidate segment is validated for leading zeros and the 0-255 range before
recursing. Valid combinations are collected and sorted at the end.

Time  : O(1) — bounded by at most 3^4 = 81 branches regardless of input size,
        since each of 4 octets can only be 1-3 digits long.
Space : O(1) auxiliary (excluding output) — recursion depth is at most 4.
"""


# ------------------------------ Solution -----------------------------------------


from os import *
from sys import *
from collections import *
from math import *

def generateIPAddress(s):
    ans = []
    n = len(s)
    def backtrack(index, parts):
        if len(parts) == 4:
            if index == n:
                ans.append(".".join(parts))
            return
        remaining = n - index
        parts_left = 4 - len(parts)
        if remaining < parts_left or remaining > 3 * parts_left:
            return
        for length in range(1, 4):
            if index + length > n:
                break
            part = s[index:index + length]
            if length > 1 and part[0] == '0':
                break
            if int(part) > 255:
                continue
            parts.append(part)
            backtrack(index + length, parts)
            parts.pop()
    backtrack(0, [])
    ans.sort()
    return ans
