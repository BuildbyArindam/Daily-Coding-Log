"""
Problem   : Picu Bank
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/picu-bank-09e29493/
Difficulty: Easy
Topics    : Algorithms, Binary Search, Math, Searching
Date      : 2026-10-02

Approach:
    Savings repeat in cycles of (M + 1) months. A cycle adds M*A from the
    regular deposits plus B in the final month, so cycle_money = M*A + B.
    Instead of binary searching on the number of months, solve it in closed form:
      1. If D >= X, the answer is 0.
      2. Let need = X - D. Skip full_cycles = need // cycle_money whole cycles.
      3. For the remainder:
         - 0                 -> no extra months
         - <= M*A            -> ceil(remainder / A) more months, reached before the bonus
         - > M*A             -> the bonus month is needed, so add M + 1 months

Complexity:
    Time  : O(1) per test case, O(T) overall
    Space : O(1)
"""


# ------------------------------------ Solution --------------------------------------------------


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    D, A, M, B, X = map(int, input().split())
    if D >= X:
        print(0)
        continue
    need = X - D
    cycle_money = M * A + B
    cycle_months = M + 1
    full_cycles = need // cycle_money
    remaining = need % cycle_money
    months = full_cycles * cycle_months
    if remaining == 0:
        print(months)
    elif remaining <= M * A:
        months += (remaining + A - 1) // A
        print(months)
    else:
        months += M + 1
        print(months)
