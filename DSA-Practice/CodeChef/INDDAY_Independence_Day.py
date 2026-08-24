"""
Problem   : Independence Day
Platform  : CodeChef
Link      : https://www.codechef.com/problems/INDDAY
Date      : 2026-08-24
Difficulty: Easy (Beginner)
Topics    : Math, Ad-hoc, Conditionals

Approach:
    Read X. If X exceeds 15, no valid answer exists -> print -1.
    Otherwise, print the difference (15 - X), i.e., how many more
    are needed to reach the threshold of 15.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ------------------- Solution --------------------------


X = int(input())
if X > 15:
    print(-1)
else:
    print(15 - X)
