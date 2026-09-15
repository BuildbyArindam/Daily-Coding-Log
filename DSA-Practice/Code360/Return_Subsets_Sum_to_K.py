"""
Problem: Return Subsets Sum to K
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380917
Date: 2026-09-15
Difficulty: Medium
Topics: Recursion, Backtracking, Subsets, Arrays

Approach:
    Standard include/exclude backtracking over the array. At each index,
    branch into two recursive calls — one including arr[index] in the
    running sum/current subset, one excluding it. When index reaches n,
    check if current_sum == k and record a copy of the subset.

Time Complexity: O(2^n) — two branches per index, n levels deep
Space Complexity: O(n) for recursion stack + current list
                   (excluding output storage for the answer list)
"""


# ------------------------------ Solution -------------------------------------


def findSubsetsThatSumToK(arr, n, k):
    # Write your code here.
    ans = []
    current = []
    def backtrack(index, current_sum):
        if index == n:
            if current_sum == k:
                ans.append(current[:])
            return
        current.append(arr[index])
        backtrack(index + 1, current_sum + arr[index])
        current.pop()
        backtrack(index + 1, current_sum)
    backtrack(0, 0)
    return ans
