"""
Problem: Is Valid Stack Permutation?
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/is-valid-stack-permutation_2042004?kunjiRedirection=true
Difficulty: Hard
Date Solved: 2026-08-22

Approach:
Simulate the push sequence ('first') onto an actual stack. After every push,
greedily pop from the stack as long as the top matches the next expected
value in the pop sequence ('other'). If we can consume all of 'other' by
the end, the pop order is a valid stack permutation of the push order.

Time Complexity: O(n)  -> each element is pushed once and popped at most once
Space Complexity: O(n) -> auxiliary stack in the worst case
"""


# ---------------------- Solution ---------------------------


def validStackPermutation(first, other):
    stack = []
    j = 0
    for value in first:
        stack.append(value)
        while stack and j < len(other) and stack[-1] == other[j]:
            stack.pop()
            j += 1
    return j == len(other)
