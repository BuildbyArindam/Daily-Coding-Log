"""
Problem   : Possible Roll
Platform  : CodeChef
Link      : https://www.codechef.com/problems/POSSROLL
Date      : 2026-10-07
Difficulty: Easy
Topics    : Math, Implementation

Approach:
    Y is reachable only if it is an exact multiple of K, so Y % K == 0.
    The number of steps needed is n = Y // K, and that must not exceed
    the limit X. Print YES if both conditions hold, otherwise NO.

Complexity:
    Time  : O(1)
    Space : O(1)
"""


# ---------------------------------------- Solution ------------------------------------------------


X, K, Y = map(int, input().split())

possible = False

if Y % K == 0:
    n = Y // K
    possible = n <= X

print("YES" if possible else "NO")
