"""
Problem   : Varied Digits (VARDIGS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/VARDIGS
Date      : 2026-08-30
Difficulty: Cakewalk
Topics    : Basic Math, Digit Manipulation, Conditional Statements

Approach:
For a 2-digit number X, compare the tens digit (X // 10)
with the units digit (X % 10). If they differ, the digits
are "varied" -> print "Yes"; otherwise print "No".

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution -----------------------------


X = int(input())
if X // 10 != X % 10:
    print("Yes")
else:
    print("No")
