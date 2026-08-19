"""
Problem: Seated Together (SAMESIT)
Link: https://www.codechef.com/problems/SAMESIT
Date Solved: 2026-08-19
Platform: CodeChef (Starter 242, Div 4)
Difficulty: Easy
Topics: Math, Implementation, Modular Arithmetic

Approach:
A bus has 20 rows of 5 seats each (seats 1-5 in row 1, 6-10 in row 2, etc.).
Chef sits at seat X, Chefina at seat X+1. They can talk only if they're in
the same row. Seats X and X+1 are in different rows exactly when X is the
last seat of a row, i.e., X % 5 == 0. Otherwise they're always adjacent
within the same row.

Time Complexity: O(1) — single modulo check
Space Complexity: O(1) — no extra storage
"""


# --------------------- Solution --------------------------------


X = int(input())
print("NO" if X % 5 == 0 else "YES")
