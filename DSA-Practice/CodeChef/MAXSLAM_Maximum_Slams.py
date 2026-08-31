"""
Problem   : Maximum Slams (MAXSLAM)
Link      : https://www.codechef.com/problems/MAXSLAM
Date      : 2026-08-31
Difficulty: Cakewalk
Topics    : Basic Math, Ceiling Division, Implementation

Approach:
Chef has already won X Grand Slams and wants to reach 25.
He needs at least (25 - X) more, and wins 4 per year, so the
answer is the smallest integer k such that 4*k >= 25 - X, i.e.
k = ceil((25 - X) / 4). Implemented via integer-division trick:
(req + 3) // 4 for req = 25 - X.

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""


# ---------------------------- Solution -------------------------------------


X = int(input())
years = (25 - X + 3) // 4
print(years)
