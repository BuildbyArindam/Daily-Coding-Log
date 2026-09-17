"""
Problem: Minimum Cars Required
Platform: CodeChef (practice - Logical Problems, DIFF800)
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MINCARS
Date: 2026-09-17
Difficulty: 608
Topics: Math, Greedy

Approach:
Each car can carry at most 4 people. To find the minimum number of cars
needed for N people, take the ceiling of N/4. Ceiling division is done
without floating point using (N + 3) // 4.

Time Complexity: O(1) per test case, O(T) overall
Space Complexity: O(1)
"""


# ---------------------------------- Solution ---------------------------------------------


T = int(input())
for _ in range(T):
    N = int(input())
    cars = (N + 3) // 4
    print(cars)
