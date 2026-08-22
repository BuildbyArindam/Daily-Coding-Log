"""
Problem: Smallest First
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/smallest-first_7084829?kunjiRedirection=true
Date Solved: 2026-08-22
Difficulty: Medium
Topics: Arrays, Monotonic Stack, Next Smaller Element

Approach:
Build a monotonic increasing stack from right to left to find, for each index i,
the index of the next element that is smaller than arr[i] (using >= while popping
so equal elements don't get double-counted, ensuring arr[i] is treated as the
leftmost minimum among ties). For each i, (next_smaller[i] - i) gives the count
of subarrays starting at i where arr[i] is the first and smallest element.
Summing this over all i gives the total answer.

Time Complexity: O(n)  -- each index pushed/popped from stack at most once
Space Complexity: O(n) -- stack + next_smaller array
"""


# ----------------------- Solution ---------------------------


def count(n: int, arr: [int]) -> int:
    next_smaller = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            next_smaller[i] = stack[-1]
        stack.append(i)
    ans = 0
    for i in range(n):
        ans += next_smaller[i] - i
    return ans
