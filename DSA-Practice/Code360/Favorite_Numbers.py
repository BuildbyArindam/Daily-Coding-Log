"""
Problem: Favorite Numbers
Platform: Code360
Link: https://www.naukri.com/code360/problems/favorite-numbers_2460770?kunjiRedirection=true
Difficulty: Medium
Topics: Sliding Window, Two Pointers, Hashing, Frequency Counting
Date Solved: 2026-09-06

Approach:
Count subarrays of `arr` that contain every element of `favArr` with at
least its required multiplicity. Build a frequency map `required` for
favArr. Expand a window with `right`, tracking how many distinct
required values are still under-satisfied (`missing`). Once `missing`
hits 0, every subarray ending anywhere from `right` to n-1 that starts
at the current `left` (or later, up to the point the window breaks)
is valid — so instead of shrinking immediately, add (n - right) for
each valid right, then advance `left` one step at a time, re-adding
to `missing` whenever removing an element drops it below its
requirement, and keep repeating while missing == 0. This effectively
counts, for each left boundary, how many right boundaries make the
window valid, summed via the (n - right) trick.

Time Complexity: O(n) — right advances n times, left advances at most
n times total across the whole run (amortized two-pointer).
Space Complexity: O(k) — where k = number of distinct values in
favArr, for the `required` and `window` maps.
"""


# ----------------------------- Solution ---------------------------------


from typing import *

def favoriteNum(arr: List[int], favArr: List[int]) -> int:
    required = {}
    for x in favArr:
        required[x] = required.get(x, 0) + 1
    n = len(arr)
    k = len(favArr)
    missing = k
    window = {}
    left = 0
    ans = 0
    for right in range(n):
        x = arr[right]
        if x in required:
            cnt = window.get(x, 0)
            if cnt < required[x]:
                missing -= 1
            window[x] = cnt + 1
        while missing == 0:
            ans += n - right
            y = arr[left]
            if y in required:
                cnt = window[y]
                if cnt <= required[y]:
                    missing += 1
                window[y] = cnt - 1
            left += 1
    return ans
