"""
Problem   : Ball Game
Platform  : CodeChef
Link      : https://www.codechef.com/problems/BALL_GAME
Difficulty: 1736
Topics    : Sorting, Monotonic Stack
Date      : 2026-10-09

Approach:
    Sort the balls by (A, B). Then sweep once with a monotonic stack,
    comparing ratios by cross-multiplication (a * B_top < A_top * b)
    so there is no float precision issue. If the incoming ball has a
    smaller A/B ratio than the stack top, the top can never be the
    answer and is popped. The answer is the number of balls left in
    the stack.

Complexity:
    Time : O(N log N) for the sort, plus O(N) amortized for the stack sweep
    Space: O(N)
"""


# -------------------------------------------- Solution --------------------------------------------


import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    balls = sorted(zip(A, B))
    stack = []
    for a, b in balls:
        while stack and a * stack[-1][1] < stack[-1][0] * b:
            stack.pop()
        stack.append((a, b))
    print(len(stack))
