"""
Problem: Reverse Stack Using Recursion
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380927
Date: 2026-09-17
Difficulty: Easy
Topics: Recursion, Stack

Approach:
Use recursion to pop all elements off the stack one by one until it's
empty, then use a helper function (insertAtBottom) to insert each
popped element back at the bottom of the stack in the correct order,
using the call stack itself as auxiliary storage instead of an
explicit second stack.

Time Complexity: O(n^2) — each of the n elements is inserted at the
bottom via insertAtBottom, which itself takes O(n) in the worst case.
Space Complexity: O(n) — recursion call stack depth (no extra
data structure used).
"""


# ------------------------------ Solution ---------------------------------------


from typing import List

def reverseStack(stack: List[int]) -> None:
    if len(stack) <= 1:
        return
    top = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack, top)

def insertAtBottom(stack: List[int], value: int) -> None:
    if not stack:
        stack.append(value)
        return
    top = stack.pop()
    insertAtBottom(stack, value)
    stack.append(top)
