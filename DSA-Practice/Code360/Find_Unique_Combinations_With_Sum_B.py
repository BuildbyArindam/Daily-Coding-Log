"""
Problem   : Find Unique Combinations with Sum B
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/find-unique-combinations-with-sum-b_1948311
Date      : 2026-08-28
Difficulty: Easy
Topics    : Backtracking, Recursion, Array, Sorting

Approach:
- Sort ARR so duplicates sit next to each other and can be skipped,
  and so early termination (ARR[i] > target) works correctly.
- Backtrack from index `start`, building `current` combination.
- At each level, skip ARR[i] == ARR[i-1] (i > start) to avoid duplicate
  combinations, since each array element can be used at most once.
- If target == 0, record a copy of current combination.
- Break early once ARR[i] > target (array is sorted, so no point continuing).

Time Complexity : O(2^n) worst case for combination generation,
                   dominated by branching factor; each valid combo
                   copy costs O(k) where k is combo length.
Space Complexity: O(n) for recursion stack + O(n) for `current`,
                   excluding the output list itself.
"""


# -------------------------- Solution ------------------------------


def combSum(ARR, B):
    ARR.sort()
    ans = []
    def backtrack(start, target, current):
        if target == 0:
            ans.append(current[:])
            return
        for i in range(start, len(ARR)):
            if ARR[i] > target:
                break
            current.append(ARR[i])
            backtrack(i, target - ARR[i], current)
            current.pop()
    backtrack(0, B, [])
    ans.sort(reverse=True)
    return ans
