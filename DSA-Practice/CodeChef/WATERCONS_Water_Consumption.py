"""
Problem: Water Consumption
Platform: CodeChef
Link: https://www.codechef.com/problems/WATERCONS
Date Solved: 2026-09-06
Difficulty: Cakewalk (~254)
Topics: Basic Math, Conditional Statements, Implementation

Approach:
Chef's doctor advised drinking at least 2000 ml of water a day.
For each test case, read the amount X (in ml) Chef drank and
compare it against the 2000 ml threshold. Print "YES" if X >= 2000,
else "NO".

Time Complexity: O(T) — one comparison per test case
Space Complexity: O(1) — no extra storage beyond input variables
"""


# ------------------------ Solution --------------------------------


T = int(input())
for _ in range(T):
    X = int(input())
    if X >= 2000:
        print("YES")
    else:
        print("NO")
