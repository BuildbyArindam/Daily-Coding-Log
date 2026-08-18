"""
Problem   : Happy New Year!
Platform  : CodeChef
Link      : https://www.codechef.com/problems/NEWYEAR
Date      : 2026-08-18
Difficulty: School / Easy (basic I/O + arithmetic; unverified official rating —
            CodeChef blocks automated fetches, so confirm on-site if you need the exact number)
Topics    : Basic Math, Implementation, I/O

Approach:
Given the current hour X (0-24) on New Year's Eve, the hours remaining
until midnight (24:00) is simply 24 - X. Read X, print 24 - X.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ------------------------- Solution --------------------------


X = int(input())
hours_left = 24 - X
print(hours_left)
