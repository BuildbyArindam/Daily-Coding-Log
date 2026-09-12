"""
Problem   : Air Conditioner Temperature
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/ACTEMP
Difficulty: 584
Date      : 2026-09-12
Topic     : Conditional Logic, Implementation

Approach:
Given A (temp needed by person 1), B (AC's set temperature), and C (temp
needed by person 2), the AC can satisfy both people only if its temperature
B is high enough to cover the higher of the two requirements. So check
max(A, C) <= B.

Time Complexity : O(T)   -- one constant-time check per test case
Space Complexity: O(1)   -- no extra data structures used
"""


# ---------------------------- Solution ----------------------------------


T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    if max(A, C) <= B:
        print("Yes")
    else:
        print("No")
