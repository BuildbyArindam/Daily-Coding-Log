"""
Problem   : Reverse The Groups
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/reverse-the-groups_3929136?kunjiRedirection=true
Difficulty: Medium
Date      : 2026-08-23
Topics    : Arrays, In-place Manipulation, Two Pointers

Approach:
    Walk the array from the back in strides of k, using a pointer i that
    starts at (n - k) and decreases by k each iteration. For each position
    where a full window of size k fits (i >= 0), reverse that k-length
    slice in place. This effectively reverses the array in k-sized blocks,
    processed from the end toward the front. If n is not a multiple of k,
    the leading partial block (size n % k, sitting at index 0) falls
    outside the loop and is left untouched.

Time Complexity : O(n) — each element is touched by exactly one reversal
Space Complexity: O(1) extra — reversal is done via slice assignment
                  in place (ignoring Python's internal slice temporaries)
"""


# -------------------- Solution -------------------------


from os import *
from sys import *
from collections import *
from math import *
from typing import *
import builtins
open = builtins.open
def reverseTheGroups(s: List[int], n: int, k: int) -> List[int]:
    i = n - k
    while i >= 0:
        s[i:i + k] = reversed(s[i:i + k])
        i -= k
    return s
