"""
Problem   : A Game of Numbers
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/a-game-of-numbers-1-5d3a8cb3/
Difficulty: Easy
Topics    : Data Structures, Stacks
Date      : 2026-09-28

Approach:
    For each index i, find j = the next index to the right with A[j] > A[i],
    then k = the next index to the right of j with A[k] < A[j]. Answer is A[k],
    or -1 if either j or k doesn't exist.
    Both lookups are precomputed with monotonic stacks:
      - Pass 1 (decreasing stack): next greater index for every element.
      - Pass 2 (increasing stack): next smaller index for every element.
      - Combine: ans[i] = A[next_smaller[next_greater[i]]].

Complexity:
    Time  : O(N), each index is pushed and popped at most once per pass.
    Space : O(N) for the stacks and the helper arrays.
"""


# --------------------------------- Solution ---------------------------------------------


import sys
input = sys.stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
next_greater = [-1] * N
stack = []
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        next_greater[stack.pop()] = i
    stack.append(i)
next_smaller = [-1] * N
stack = []
for i in range(N):
    while stack and A[stack[-1]] > A[i]:
        next_smaller[stack.pop()] = i
    stack.append(i)
ans = [-1] * N
for i in range(N):
    j = next_greater[i]
    if j != -1:
        k = next_smaller[j]

        if k != -1:
            ans[i] = A[k]
print(*ans)
