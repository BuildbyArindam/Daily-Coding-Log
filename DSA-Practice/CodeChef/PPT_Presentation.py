"""
Problem   : Presentation (PPT)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/PPT
Date      : 2026-08-21
Difficulty: Beginner (Div 4 / Starter series, ~500-700 rating)
Topics    : Basic Math, Ad-Hoc / Implementation

Approach:
Each slide takes 30 seconds, and the target presentation length is
600 seconds, i.e. exactly 20 slides are required in total.
Given N slides already made, the number of additional slides needed
is simply (20 - N). No edge cases beyond direct arithmetic since N
is guaranteed to be within valid bounds.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# -------------------- Solution -------------------------


N = int(input())
print(20 - N)
