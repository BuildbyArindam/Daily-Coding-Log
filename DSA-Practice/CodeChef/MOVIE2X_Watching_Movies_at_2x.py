"""
Problem   : Watching Movies at 2x
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MOVIE2X
Difficulty: 628
Date      : 2026-09-18
Topics    : Basic Math, Greedy, Implementation

Approach:
    Out of X total minutes of footage, Y minutes are watched at 2x speed
    (so they take Y//2 minutes), and the remaining (X - Y) minutes are
    watched at normal speed. Total time is just the sum of the two.

Time Complexity : O(1)  — constant-time arithmetic
Space Complexity: O(1)  — no extra data structures
"""


# -------------------------------- Solution -----------------------------------------


X, Y = map(int, input().split())
time_for_first_Y = Y // 2
time_for_remaining = X - Y
total_time = time_for_first_Y + time_for_remaining
print(total_time)
