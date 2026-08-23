"""
Problem     : Can You See Me?
Platform    : Code360 (Naukri)
Link        : https://www.naukri.com/code360/problems/can-you-see-me_3952535?kunjiRedirection=true
Date Solved : 2026-08-23
Difficulty  : Medium
Topics      : Stacks, Monotonic Stack, Next Greater Element

Approach:
Maintain a monotonic decreasing stack of heights seen so far.
For each new height:
  - Pop all shorter elements from the stack, each popped person can see
    the current person, so increment the count for each pop.
  - If the stack is non-empty after popping, the person now at the top
    (taller than current) can also see the current person -> +1.
  - If that top element is equal in height to current, pop it too
    (only one of two equal-height people blocks the view further back).
  - Push the current height onto the stack.
This effectively counts, for each person, how many people behind them
are visible before their view is blocked by someone taller or equal.

Time Complexity  : O(n) -- each element is pushed and popped at most once
Space Complexity : O(n) -- for the stack
"""


# -------------------------- Solution ------------------------------


from typing import *

def countPairs(n: int, arr: List[int]) -> int:
    stack = []
    ans = 0
    for height in arr:
        while stack and stack[-1] < height:
            stack.pop()
            ans += 1
        if stack:
            ans += 1
        if stack and stack[-1] == height:
            stack.pop()
        stack.append(height)
    return ans
