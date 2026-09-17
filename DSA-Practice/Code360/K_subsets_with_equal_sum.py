"""
Problem   : K Subsets with Equal Sum
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380925
Date      : 2026-09-17
Difficulty: Easy
Topics    : Backtracking, Recursion, Partition Problems

Approach:
- If total sum isn't divisible by k, or the largest element exceeds
  the target (total/k), it's immediately impossible.
- Sort the array in descending order (helps fail fast / find valid
  splits sooner since large elements are placed first).
- Backtrack: build one subset at a time until it hits `target`, then
  move to the next subset (reset current_sum, restart scan from 0).
- Prune: skip already-used elements, skip duplicate values at the
  same recursion depth (avoids redundant identical branches), and
  skip any element that would overshoot the target.
- Base case: when only 1 group is left, the remaining elements must
  sum to target automatically (short-circuit return True).

Time Complexity : O(2^n) worst case (subset-sum-style backtracking,
                   though pruning + sorting makes it much faster in
                   practice); dominated by the recursive search.
Space Complexity: O(n) for the `used` array and recursion stack.
"""


# ------------------------ Solution ---------------------------------------


from os import *
from sys import *
from collections import *
from math import *

def splitArray(arr, k):
    total = sum(arr)
    if total % k != 0:
        return False
    target = total // k
    arr.sort(reverse=True)
    if arr and arr[0] > target:
        return False
    n = len(arr)
    used = [False] * n
    def backtrack(start, groups_left, current_sum):
        if groups_left == 1:
            return True
        if current_sum == target:
            return backtrack(0, groups_left - 1, 0)
        prev = -1
        for i in range(start, n):
            if used[i]:
                continue
            if arr[i] == prev:
                continue
            if current_sum + arr[i] > target:
                continue
            used[i] = True
            if backtrack(i + 1, groups_left, current_sum + arr[i]):
                return True
            used[i] = False
            prev = arr[i]
            if current_sum == 0:
                break
        return False
    return backtrack(0, k, 0)
