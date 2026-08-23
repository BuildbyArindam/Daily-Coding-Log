"""
Problem   : Contest Registration Fee
Platform  : CodeChef
Link      : https://www.codechef.com/problems/P1235
Date      : 2026-08-23
Topics    : Implementation, Conditional Statements
Difficulty: Beginner / Easy

Approach:
Read two integers x (available amount) and y (required fee).
If the available amount x is enough to cover the fee y (y <= x),
no extra amount is needed, so print 0. Otherwise, print the fixed
late fee of 100.

Time complexity : O(1)
Space complexity: O(1)
"""


# ----------------------- Solution ---------------------------


x, y = map(int, input().split())
if y <= x:
    print(0)
else:
    print(100)
