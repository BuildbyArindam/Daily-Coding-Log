"""
Problem: Guilty — to the kitchen!
Link: https://codeforces.com/problemset/problem/42/A
Platform: Codeforces | Difficulty: *1400 | Topic: Greedy, Implementation
Date solved: 2026-09-10

Approach:
For each ingredient i, the max number of servings you could scale to is
b[i]/a[i] (limited by how much of that ingredient you have). The binding
constraint is the smallest such ratio x = min(b[i]/a[i]). Total soup volume
at that scale is total_a * x (sum of ratios per serving * scale factor),
capped by the vessel volume V.

Time complexity: O(n)
Space complexity: O(n)
"""


# ----------------------------- Solution -----------------------------


import sys
input = sys.stdin.readline
n, V = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
total_a = sum(a)
x = min(b[i] / a[i] for i in range(n))
answer = min(V, total_a * x)
print(f"{answer:.10f}")
