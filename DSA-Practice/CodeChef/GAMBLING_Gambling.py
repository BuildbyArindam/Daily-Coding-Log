"""
Problem   : Gambling (GAMBLING)
Platform  : CodeChef (Starter 207, Division-based)
Link      : https://www.codechef.com/problems/GAMBLING
Date      : 2026-08-21
Difficulty: Cakewalk
Topics    : Ad-Hoc, Basic Math

Approach:
Standard 6-sided die has opposite faces summing to 7 (1-6, 2-5, 3-4).
Given the visible face value A, the hidden (bottom) face is simply 7 - A.
No simulation or search needed — direct O(1) arithmetic formula.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution -------------------------


A = int(input())
print(7 - A)
