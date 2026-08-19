"""
Problem   : Balloon Splash (BOP1)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/BOP1
Date      : 2026-08-19
Difficulty: Cakewalk
Topics    : Conditional Statements, Basic I/O

Approach:
    Read two integers X and Y (balloon counts for Alice and Bob).
    Directly compare them:
        - X > Y -> Alice wins
        - Y > X -> Bob wins
        - X == Y -> Draw
    No data structures or algorithms needed beyond a simple comparison.

Complexity:
    Time  : O(1) per test case
    Space : O(1)
"""


# ----------------------- Solution ------------------------


X, Y = map(int, input().split())
if X > Y:
    print("Alice")
elif Y > X:
    print("Bob")
else:
    print("Draw")
