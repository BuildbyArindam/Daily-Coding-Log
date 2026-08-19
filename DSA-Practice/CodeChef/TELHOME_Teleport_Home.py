"""
Problem   : Teleport Home (TELHOME)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/TELHOME
Date      : 2026-08-19
Difficulty: 400-500 (Beginner)
Topics    : Math, Greedy, Implementation

Approach:
Chef can teleport up to T km for free (one-time use), and walks the
remaining distance at 1 km/hour. Teleporting the full min(D, T) km is
always optimal since it's free, so the minimum time is just the leftover
distance after teleporting: max(0, D - T).

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ------------------------ Solution --------------------------


D, T = map(int, input().split())
print(max(0, D - T))
