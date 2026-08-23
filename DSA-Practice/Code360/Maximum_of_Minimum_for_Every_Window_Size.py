"""
Problem   : Maximum of Minimum for Every Window Size
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/maximum-of-minimum-for-every-window-size_982935?kunjiRedirection=true
Difficulty: Hard
Date      : 2026-08-23
Topics    : Arrays, Monotonic Stack (Previous/Next Smaller Element)

Approach:
For each index i, find the nearest smaller element to the left (left[i])
and to the right (right[i]) using a monotonic increasing stack. The
distance (right[i] - left[i] - 1) gives the largest window size in which
arr[i] is guaranteed to be the minimum. Update ans[window_size] with
arr[i]. Finally, propagate answers from larger window sizes down to
smaller ones, since any answer valid for a bigger window is also valid
for a smaller one (ans[i] = max(ans[i], ans[i+1])).

Time Complexity : O(n)  — each index pushed/popped from stack at most once (x2 passes)
Space Complexity: O(n)  — left[], right[], stack, ans[]
"""


# --------------------------- Solution ------------------------------


from os import *
from sys import *
from collections import *
from math import *
def maxMinWindow(arr, n):
    ans = [float('-inf')] * (n + 1)
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
        window_size = right[i] - left[i] - 1
        ans[window_size] = max(ans[window_size], arr[i])
    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])
    return ans[1:]
