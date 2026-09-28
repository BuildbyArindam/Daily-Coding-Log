"""
Platform    : HackerEarth
Problem     : Largest Number
Link        : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/largest-number-7-eee0b7c3/
Difficulty  : Medium
Topics      : Stacks, Basics of Stacks, Data Structures
Date Solved : 2026-09-28

Approach:
    Greedy with a monotonic (non-increasing) stack. Scan the digits left to
    right; while the top of the stack is smaller than the current digit and
    removals remain (K > 0), pop it, since a bigger digit in an earlier
    position always gives a larger number. Then push the current digit.
    If removals are left after the scan, the stack is already non-increasing,
    so drop the last K digits.

Complexity:
    Time  : O(N) - each digit is pushed and popped at most once
    Space : O(N) - stack holds up to N digits
"""


# ---------------------------------------- Solution -----------------------------------------------


N = input().strip()
K = int(input().strip())
stack = []
for digit in N:
    while K > 0 and stack and stack[-1] < digit:
        stack.pop()
        K -= 1
    stack.append(digit)
if K > 0:
    stack = stack[:-K]
print(''.join(stack))
