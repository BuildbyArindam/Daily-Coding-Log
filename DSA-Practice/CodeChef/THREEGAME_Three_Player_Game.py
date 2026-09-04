"""
Problem   : Three Player Game
Platform  : CodeChef
Link      : https://www.codechef.com/problems/THREEGAME
Date      : 2026-09-04
Difficulty: Easy
Topics    : Math, Greedy, Constructive Algorithms, Case Analysis (Parity)

Approach:
A three-player game holds rounds until one player has a strictly higher
score than both others (a "clear winner"). We're told N rounds have
already passed with no clear winner, and we want the MAXIMUM total
number of rounds that could eventually be held.

Key insight: to delay a clear winner as long as possible after round N,
the best state to be in is two players tied at some score x and the
third at a lower score y, maximizing (x - y). Working through both
parity cases (N even / N odd) and combining them gives the closed form:

    answer = 3 * (N // 2) + 1

Time complexity  : O(1) per test case, O(T) overall
Space complexity : O(1)
"""


# ---------------------------- Solution ------------------------------------


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    ans = 3 * (N // 2) + 1
    print(ans)
