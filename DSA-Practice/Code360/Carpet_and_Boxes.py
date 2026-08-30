"""
Problem   : Carpet and Boxes
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/carpet-and-boxes_5228634?kunjiRedirection=true
Date      : 2026-08-30
Difficulty: Medium
Topics    : Sorting, Two Pointers, Sliding Window

Approach:
  Sort the box positions. The optimal carpet covering exactly k boxes must
  cover k *consecutive* positions in the sorted order (any gap-skipping
  window can only be as good or worse). So slide a fixed window of size k
  across the sorted array and track the minimum (position[i+k-1] - position[i] + 1).

Time Complexity : O(n log n)  -- dominated by the sort; the window scan is O(n)
Space Complexity: O(1) extra (in-place sort, ignoring input/output storage)
"""


# ------------------------- Solution ------------------------------


from os import *
from sys import *
from collections import *
from math import *
from builtins import open

def getMinimumLength(position: [int], k: int) -> int:
    position.sort()
    minimum_length = float('inf')
    for i in range(len(position) - k + 1):
        length = position[i + k - 1] - position[i] + 1
        minimum_length = min(minimum_length, length)
    return minimum_length
