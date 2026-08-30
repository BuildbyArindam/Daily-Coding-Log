"""
Problem   : Food Balance
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FOODBAL
Date      : 2026-08-30
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
    Compute the absolute difference between food (F) and population (P)
    for both countries. The country with the smaller |F - P| has a better
    food-to-population balance. If both differences are equal, it's a tie.

Time Complexity : O(1)  — constant number of arithmetic operations
Space Complexity: O(1)  — no extra data structures used
"""


# ----------------------- Solution -------------------------------


F1, P1, F2, P2 = map(int, input().split())
diff1 = abs(F1 - P1)
diff2 = abs(F2 - P2)
if diff1 < diff2:
    print("First")
elif diff2 < diff1:
    print("Second")
else:
    print("Both")
