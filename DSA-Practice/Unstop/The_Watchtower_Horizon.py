# Problem: The Watchtower Horizon
# Platform: Unstop
# Link: https://unstop.com/code/practice/659207
# Date: 2026-09-02
# Difficulty: Medium
# Topics: Array, Monotonic Stack, Next Greater Element, Stack
#
# Approach:
#   For each tower, find the horizontal distance to the nearest taller
#   (strictly greater) tower to its right — the "watchtower horizon".
#   If none exists, the horizon extends to the end of the array.
#   Traverse right-to-left maintaining a monotonic decreasing stack of
#   indices; pop indices whose height <= current height (they can't be
#   anyone's "next greater"), then the stack top (if any) is the answer.
#
# Time Complexity:  O(n) — each index is pushed and popped at most once
# Space Complexity: O(n) — stack + answer array


# ------------------------ Solution --------------------------


n = int(input())
heights = list(map(int, input().split()))
ans = [0] * n
stack = []  
for i in range(n - 1, -1, -1):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1] - i
    else:
        ans[i] = n - 1 - i
    stack.append(i)
print(*ans)
