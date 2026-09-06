"""
Problem: Masterchef Finals
Platform: CodeChef
Link: https://www.codechef.com/problems/TOP10
Date Solved: 2026-09-06
Difficulty: Cakewalk
Topics: Basic Math, Conditional Statements, Implementation

Approach:
Read T test cases; for each rank X, print "YES" if X <= 10
(i.e., the participant finished in the top 10), else "NO".
Straightforward threshold check, no preprocessing needed.

Time Complexity: O(T) — one constant-time check per test case
Space Complexity: O(1) — no extra storage beyond input variables
"""


# ------------------------- Solution --------------------------------


T = int(input())
for _ in range(T):
    X = int(input())
    if X <= 10:
        print("YES")
    else:
        print("NO")
