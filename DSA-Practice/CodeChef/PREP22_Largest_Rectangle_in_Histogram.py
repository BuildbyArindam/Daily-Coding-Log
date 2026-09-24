"""
Platform   : CodeChef
Problem    : Largest Rectangle in Histogram (PREP22)
Link       : https://www.codechef.com/problems/PREP22
Difficulty : 1700
Topics     : Stack, Monotonic Stack, Array
Date       : 2026-09-24

Approach:
    Keep a stack of indices whose bar heights are in increasing order.
    When the current bar is shorter than the bar on top of the stack, pop it
    and treat it as the smallest bar of a rectangle. Its right boundary is the
    current index i, and its left boundary is the new stack top (or the start
    of the array if the stack is empty). Append a sentinel height 0 at the end
    (i == N) to flush all remaining bars.

Time Complexity  : O(N) per test case (each index is pushed and popped once)
Space Complexity : O(N) for the stack
"""


# ------------------------------------ Solution --------------------------------------------


def largestRectangleArea(N: int, A: list[int]) -> int:
    stack = []
    max_area = 0
    for i in range(N + 1):
        curr_height = A[i] if i < N else 0
        while stack and A[stack[-1]] > curr_height:
            height = A[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(largestRectangleArea(N, A))
