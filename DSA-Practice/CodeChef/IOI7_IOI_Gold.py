"""
Problem   : IOI Gold (IOI7)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/IOI7
Date      : 2026-08-20
Difficulty: Beginner (Div 4 / School level)
Topics    : Basic Programming, Conditional Statements

Approach:
Chef scores N points; a gold medal requires at least G points.
Simply compare N and G — print "Yes" if N >= G, else "No".

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""


# -------------------- Solution -----------------------


N, G = map(int, input().split())
print("Yes" if N >= G else "No")
