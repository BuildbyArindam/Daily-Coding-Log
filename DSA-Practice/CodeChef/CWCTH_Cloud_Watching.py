"""
Problem   : Cloud Watching (CWCTH)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CWCTH
Date      : 2026-08-22

Approach  :
    It rains if B (cloud count) is at least 3 times A (some threshold value).
    Direct comparison — no loops or data structures needed.

Time Complexity  : O(1)
Space Complexity : O(1)
"""


# -------------------------- Solution ----------------------------


A, B = map(int, input().split())
if B >= 3 * A:
    print("Rain")
else:
    print("Dry")
