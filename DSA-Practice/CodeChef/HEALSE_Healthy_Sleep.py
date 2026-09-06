"""
Problem   : Healthy Sleep
Platform  : CodeChef
Link      : https://www.codechef.com/problems/HEALSE
Date      : 2026-09-06
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
    Read hours slept (H) and compare against the ideal value of 8.
    - H < 8  -> "LESS"
    - H == 8 -> "PERFECT"
    - H > 8  -> "MORE"
    A single if-elif-else covers all three cases in constant time.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ---------------------- Solution ------------------------


H = int(input())
if H < 8:
    print("LESS")
elif H == 8:
    print("PERFECT")
else:
    print("MORE")
