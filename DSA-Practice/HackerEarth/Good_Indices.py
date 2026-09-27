"""
Problem   : Good Indices
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/good-indices-c7058c9b/
Date      : 2026-09-27
Difficulty: Medium
Topics    : Stacks, Queues, Monotonic Stack

Approach:
    For each index i, find the nearest strictly-smaller element to its left (L[i])
    and right (R[i]) using two monotonic increasing stacks (classic "previous/next
    smaller element" pattern). An index is only "good" if both a smaller element
    exists on the left AND on the right. The answer for a good index is the count
    of elements strictly between L[i] and R[i], excluding i itself:
        (i - L[i] - 1) + (R[i] - i - 1)
    Indices with no smaller element on either side get -1.

Time Complexity : O(N) per test case (two linear passes with monotonic stacks)
Space Complexity: O(N) for L, R, and the stack
"""


# ---------------------------------------- Solution --------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        L = [-1] * N
        stack = []
        for i in range(N):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if stack:
                L[i] = stack[-1]
            stack.append(i)
        R = [-1] * N
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            if stack:
                R[i] = stack[-1]
            stack.append(i)
        ans = [-1] * N
        for i in range(N):
            if L[i] != -1 and R[i] != -1:
                ans[i] = (i - L[i] - 1) + (R[i] - i - 1)
        print(*ans)

if __name__ == "__main__":
    solve()
