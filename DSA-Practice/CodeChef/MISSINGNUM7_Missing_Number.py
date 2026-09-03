"""
Problem   : Missing Number
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MISSINGNUM7
Difficulty: Cakewalk
Topics    : Basic Math, Implementation

Date      : 2026-09-03

Approach:
    A jigsaw puzzle has exactly 4 pieces numbered 1-4, so the full sum
    is always 1+2+3+4 = 10. Given S, the sum of the remaining 3 pieces,
    the missing piece is simply 10 - S.

Complexity:
    Time : O(1)
    Space: O(1)
"""


# ------------------------ Solution --------------------------------


S = int(input())
print(10 - S)
