"""
Problem   : Largest Rectangle in a Histogram
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/largest-rectangle-in-a-histogram_1058184
Difficulty: Hard
Topics    : Stack, Monotonic Stack, Arrays
Date      : 2026-08-22

Approach:
Maintain a monotonically increasing stack of indices (by height).
When a shorter bar is found, pop taller bars and compute the area they
could span - width is bounded on the right by the current index and on
the left by the new stack top (or 0 if the stack is empty). After the
main pass, flush any remaining bars in the stack, treating the end of
the array as the right boundary.

Time complexity : O(n) - each index is pushed and popped at most once
Space complexity: O(n) - stack can hold up to n indices
"""


# ----------------------- Solution ---------------------------


def largestRectangle(arr):
    stack = []
    max_area = 0
    for i, height in enumerate(arr):
        while stack and arr[stack[-1]] > height:
            h = arr[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)
    n = len(arr)
    while stack:
        h = arr[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * width)
    return max_area
