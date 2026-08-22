"""
Problem   : Problem Selection
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/problems/problem-selection_2824965
Difficulty: Easy
Date      : 2026-08-22
Topics    : Arrays, Sorting, Greedy

Approach:
    - Compute group size m = ceil(len(A) / (K + 1)), i.e. the smallest
      possible bucket size when A is split into (K + 1) groups as evenly
      as possible.
    - Sort A.
    - Minimum possible sum of a group of size m = sum of the m smallest
      elements (A[:m] after sorting).
    - Maximum possible sum of a group of size m = sum of the m largest
      elements (A[-m:] after sorting).
    - Return (minimum, maximum).

Time complexity : O(N log N)   -> dominated by the sort
Space complexity: O(1) extra   (O(log N) / O(N) if counting sort's own
                                 internal stack/array, ignoring input list)
"""


# ------------------------ Solution ----------------------------


from sys import *
from collections import *
from math import *
from typing import *

def problemSelection(A: List[int], K: int) -> Tuple[int, int]:
    m = (len(A) + K) // (K + 1)
    A.sort()
    minimum = sum(A[:m])
    maximum = sum(A[-m:])
    return minimum, maximum
