"""
Problem   : Vaccine Drive (VACCINE3)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/VACCINE3
Difficulty: 1731
Topics    : Math, Implementation
Date      : 2026-10-08

Approach:
    X holds the group sizes in vaccination order, and G is the 1-indexed
    group that contains Chef. `before` is the number of people vaccinated
    ahead of Chef's group (sum(X[G:])).
      - Best case: Chef is first in their group, so `before + 1` people
        must be done, giving ceil((before + 1) / P) days.
      - Worst case: Chef is last in their group, so `before + X[G-1]`
        people must be done, giving ceil((before + X[G-1]) / P) days.
    P is the number of vaccinations per day, and ceiling division is done
    with integer arithmetic.

Time Complexity : O(N) per test case (one pass to sum the suffix)
Space Complexity: O(N) to store X, O(1) extra
"""


# --------------------------------------- Solution --------------------------------------------------


import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    G, P, *X = map(int, input().split())
    before = sum(X[G:])
    minimum_days = (before + 1 + P - 1) // P
    maximum_days = (before + X[G - 1] + P - 1) // P
    print(minimum_days, maximum_days)
