"""
Problem: Flip the Cards
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLIPCARDS
Date: 2026-09-18
Difficulty: 641
Topics: Greedy, Math

Approach:
Given N cards with X currently face-up, we want all cards showing the
same side with the minimum number of flips. Flipping all face-up cards
down costs X flips; flipping all face-down cards up costs (N - X) flips.
The answer is simply the cheaper of the two options: min(X, N - X).

Time Complexity: O(1) per test case, O(T) overall
Space Complexity: O(1)
"""


# -------------------------------- Solution -------------------------------------------


T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    print(min(X, N - X))
