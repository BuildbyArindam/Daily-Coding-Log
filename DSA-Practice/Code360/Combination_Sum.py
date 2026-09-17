"""
Problem   : Combination Sum
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380933
Difficulty: Easy
Date      : 2026-09-17
Topics    : Backtracking, Recursion, Array

Approach:
    Sort the array first so we can prune early (break instead of continue
    when ARR[i] > target). Standard backtracking: at each step, either
    include the current element (and stay at the same index `i` since
    elements can be reused) or move to the next index. Base case is when
    target hits 0, at which point the current combination is a valid
    answer and gets copied into the result list.

Time complexity : O(2^t) worst case, where t = target / min(ARR)
                   (bounded further by the branching factor of the tree;
                   exact bound is roughly O(N^(T/M + 1)) where N = len(ARR),
                   M = min element)
Space complexity: O(T/M) for recursion depth (call stack),
                   plus O(number of combinations * avg length) for output storage
"""


# -------------------------------- Solution ------------------------------------


from copy import copy

def combSum(ARR, B):
    ARR.sort()
    ans = []
    def backtrack(start, target, current):
        if target == 0:
            ans.append(copy(current))
            return
        for i in range(start, len(ARR)):
            if ARR[i] > target:
                break
            current.append(ARR[i])
            backtrack(i, target - ARR[i], current)
            current.pop()
    backtrack(0, B, [])
    return ans
