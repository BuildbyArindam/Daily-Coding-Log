"""
Problem   : Jumpy Humpy
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/jumpy-humpy-5e0231d6/
Difficulty: Easy
Topics    : Data Structures, Dynamic Programming, Stacks
Date      : 2026-09-28

Approach:
    Traverse right to left with a monotonic stack of indices, popping every
    height <= the current one. The stack top is then the nearest strictly
    greater element to the right. Define dp[i] = heights[i] XOR dp[next greater],
    or just heights[i] if none exists. The answer is the maximum dp[i].

Complexity:
    Time : O(n), since each index is pushed and popped at most once
    Space: O(n) for the dp array and the stack
"""


# ------------------------------------ Solution ------------------------------------------


n = int(input())
heights = list(map(int, input().split()))
dp = [0] * n
stack = []
answer = 0
for i in range(n - 1, -1, -1):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    if stack:
        j = stack[-1]
        dp[i] = heights[i] ^ dp[j]
    else:
        dp[i] = heights[i]
    answer = max(answer, dp[i])
    stack.append(i)
print(answer)
