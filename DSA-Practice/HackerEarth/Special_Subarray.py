"""
Problem   : Special Subarray
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/special-subarray-3-4de176ca/
Date      : 2026-09-19
Difficulty: Medium
Topics    : Binary Search, Bitmasking, Sliding Window

Approach:
    Use a two-pointer sliding window while tracking the cumulative OR
    of the current window. For each right endpoint, shrink the window
    from the left (removing elements via XOR, since each bit is set by
    exactly one element in a "special" window) while the new element
    shares any set bit with the running OR (current_or & A[right] != 0).
    Once the window is valid, every subarray ending at `right` and
    starting anywhere in [left, right] is special, so add
    (right - left + 1) to the answer.

Time complexity : O(N) per test case (each pointer moves forward only;
                   amortized O(1) work per step aside from O(log(max A)))
Space complexity: O(1) extra space
"""


# ---------------------------------- Solution -----------------------------------------


import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    left = 0
    current_or = 0
    ans = 0
    for right in range(N):
        while (current_or & A[right]) != 0:
            current_or ^= A[left]
            left += 1
        current_or |= A[right]
        ans += right - left + 1
    print(ans)
