"""
Problem: Blackjack
Platform: CodeChef
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BLACKJACK
Date: 2026-09-19
Difficulty: 681
Topics: Basic Math, Conditional Logic / Simulation

Approach:
Given two cards A and B, the third card C must make the total exactly 21
(the winning Blackjack sum) and be a valid card value (1-10). So compute
C = 21 - A - B, and check if it falls in [1, 10]. If yes, print C;
otherwise print -1.

Time Complexity: O(1) per test case, O(T) overall
Space Complexity: O(1)
"""


# -------------------------------------- Solution --------------------------------------------


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    C = 21 - A - B
    if 1 <= C <= 10:
        print(C)
    else:
        print(-1)
