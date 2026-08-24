"""
Problem   : Sum of the Minimum Values in Subarrays
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/sum-of-the-minimum-values-in-subarrays_1473824
Date      : 2026-08-24
Difficulty: Easy
Topics    : Monotonic Stack, Arrays, Contribution Technique

Approach:
For each element arr[i], find how many subarrays have arr[i] as their minimum.
This equals (distance to previous strictly smaller element) * (distance to next
smaller-or-equal element). Use two monotonic increasing stacks — one pass left
to right for `left[i]` (nearest strictly smaller on the left), one pass right
to left for `right[i]` (nearest smaller-or-equal on the right) — to avoid
double-counting equal elements. Each element's contribution is
arr[i] * left[i] * right[i], summed mod 1e9+7.

Time Complexity : O(n)  — each index pushed/popped from the stack at most once
Space Complexity: O(n)  — left[], right[], and the stack
"""


# ------------------------ Solution --------------------------


from os import *
from sys import *
from collections import *
from math import *

def sumOfSubarrayMins(arr, n):
    MOD = 10**9 + 7
    left = [0] * n
    right = [0] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = i - stack[-1]
        else:
            left[i] = i + 1
        stack.append(i)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1] - i
        else:
            right[i] = n - i
        stack.append(i)
    ans = 0
    for i in range(n):
        contribution = arr[i] * left[i] * right[i]
        ans = (ans + contribution) % MOD
    return ans
