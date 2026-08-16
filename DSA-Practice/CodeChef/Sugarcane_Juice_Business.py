"""
Problem: Sugarcane Juice Business
Platform: CodeChef
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SUGARCANE
Difficulty: Easy
Date Solved: 2026-08-16

Approach:
Each glass of sugarcane juice costs 15 (fixed rate). For each test case,
given n glasses sold, the total earnings is simply n * 15. No loops or
conditionals needed beyond reading input — pure O(1) arithmetic per query.

Time Complexity: O(T) — one multiplication per test case, T = number of test cases
Space Complexity: O(1) — no extra data structures used
"""


# -------------------------- Solution ------------------------


t = int(input())

for _ in range(t):
    n = int(input())
    print(n * 15)
