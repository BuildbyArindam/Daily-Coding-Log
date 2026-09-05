"""
Problem   : Advitiya (ADVITIYA1)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ADVITIYA1
Date      : 2026-09-05
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Range Checking

Approach:
    Read integer N and check whether it falls within the inclusive
    range [16, 18]. Print "ADVITIYA" if true, otherwise print
    "WAITING FOR ADVITIYA".

Time Complexity : O(1)  - single comparison, no loops
Space Complexity: O(1)  - constant extra space
"""


# ------------------------ Solution ---------------------------------


N = int(input())
if 16 <= N <= 18:
    print("ADVITIYA")
else:
    print("WAITING FOR ADVITIYA")
