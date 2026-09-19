"""
Problem: The Last Levels
Platform: CodeChef
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/LASTLEVELS
Date Solved: 2026-09-19
Difficulty: 679
Topics: Math, Simulation

Approach:
Each level takes Y time. After every 3 levels completed, a break of
Z time is taken — except after the very last level (no break needed
once all levels are done). Number of breaks = (X - 1) // 3.
Total time = (X * Y) + (breaks * Z).

Time Complexity: O(1) per test case, O(T) overall
Space Complexity: O(1)
"""


# ------------------------------- Solution ---------------------------------------------


T = int(input())

for _ in range(T):
    X, Y, Z = map(int, input().split())
    breaks = (X - 1) // 3
    total_time = X * Y + breaks * Z
    print(total_time)
