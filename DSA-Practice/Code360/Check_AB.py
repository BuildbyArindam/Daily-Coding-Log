"""
Problem   : Check AB
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/check-ab_624396?kunjiRedirection=true
Difficulty: Easy
Topics    : Recursion, String, Pattern Matching

Date      : 2026-08-28

Approach:
Starting from index 0, the string must begin with 'a'. Recursively check each
position i:
  - if i reaches the end, the string is valid.
  - if s[i] != 'a', invalid.
  - if s[i] == 'a', the next char must either be:
        another 'a'   -> recurse from i+1
        'b' followed by another 'b' -> recurse from i+3 (consume "abb" as a unit)
    otherwise invalid.
This enforces that every 'a' is followed by either another 'a' or a "bb" pair.

Time Complexity : O(n) — each index is visited once across the recursion.
Space Complexity: O(n) — recursion call stack depth (worst case one call per
                  character); increased recursion limit to 2000 to be safe.
"""


# ---------------------------- Solution --------------------------------


from math import *
from collections import *
from sys import *
from os import *

def checkString(s, i):
    if i == len(s):
        return True
    if s[i] != 'a':
        return False
    if i + 1 == len(s):
        return True
    if s[i + 1] == 'a':
        return checkString(s, i + 1)
    if s[i + 1] == 'b' and i + 2 < len(s) and s[i + 2] == 'b':
        return checkString(s, i + 3)
    return False

def checkABString(s):
    if len(s) == 0 or s[0] != 'a':
        return False
    setrecursionlimit(2000)
    return checkString(s, 0)

s = input().strip()
print("true" if checkABString(s) else "false")
