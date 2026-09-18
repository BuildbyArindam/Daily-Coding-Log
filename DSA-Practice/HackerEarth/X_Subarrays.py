"""
Problem: X Subarrays
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/x-subarrays-2-6179b2c0/
Date Solved: 2026-09-18
Difficulty: Medium
Topics: Binary Search, Algorithms (two-pointer)

Approach:
    Sort is not needed here (array order matters for subarray sum,
    but the two-pointer works because A[left] + A[right] is monotonic
    as `right` only ever moves left as `left` increases).
    For each `left`, shrink `right` from the end while A[left] + A[right] > X.
    All subarrays [left, right] are valid, so add (right - left + 1) to the count.

Time Complexity:  O(N) per test case — right pointer only moves left, never resets.
Space Complexity: O(1) extra (excluding input storage).
"""


# ----------------------------- Solution --------------------------------------------


import sys
input = sys.stdin.buffer.readline
T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    right = N - 1
    for left in range(N):
        while right >= left and A[left] + A[right] > X:
            right -= 1
        if right < left:
            break
        ans += right - left + 1
    print(ans)
