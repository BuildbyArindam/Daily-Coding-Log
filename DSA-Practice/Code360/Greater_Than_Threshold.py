"""
Problem: Greater Than Threshold
Platform: Code360
Link: https://www.naukri.com/code360/problems/greater-than-threshold_7664836?kunjiRedirection=true
Date solved: 2026-08-25
Difficulty: Hard
Topics: Monotonic Stack, Previous/Next Smaller Element

Approach:
For each index i, find the nearest smaller element to the left (`left[i]`)
and to the right (`right[i]`) using two monotonic increasing stacks.
This gives the widest window around i where arr[i] is the minimum,
with window length = right[i] - left[i] - 1.
If arr[i] * length > threshold for any i, that length is a valid answer
(check greedily — first match works since we just need any valid length,
not necessarily the maximum). Return -1 if no index qualifies.

Time complexity: O(n) — each index pushed/popped from each stack at most once
Space complexity: O(n) — for left[], right[], and the stack
"""


# ------------------------- Solution -----------------------------------


from typing import *

def greaterThanThreshold(arr: List[int], threshold: int) -> int:
    n = len(arr)
    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    right = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    for i in range(n):
        length = right[i] - left[i] - 1
        if arr[i] * length > threshold:
            return length
    return -1
