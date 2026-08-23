"""
Problem   : Endless Play (SKONG)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SKONG
Date      : 2026-08-23
Difficulty: Cakewalk
Topics    : Math, Implementation

Approach:
Game started at midnight on Sept 4. Given it's now H hours past
midnight on Sept X, the number of full elapsed days is (X - 4),
contributing (X - 4) * 24 hours, plus the H hours into the current day.
Total hours played = (X - 4) * 24 + H.

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""


# --------------------- Solution ------------------------


x, h = map(int, input().split())
total_hours = (x - 4) * 24 + h
print(total_hours)
