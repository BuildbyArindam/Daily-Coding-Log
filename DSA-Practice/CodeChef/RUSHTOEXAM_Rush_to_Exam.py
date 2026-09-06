"""
Problem   : Rush to Exam (RUSHTOEXAM)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/RUSHTOEXAM
Date      : 2026-09-06
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
    Given N (units covered per unit time), M (total distance),
    A (time available), check if N*A can cover M or more.
    Simple threshold comparison — no loop needed.

Complexity:
    Time  : O(1)
    Space : O(1)
"""


# ------------------------- Solution ------------------------


N, M, A = map(int, input().split())
if N * A >= M:
    print("Yes")
else:
    print("No")
