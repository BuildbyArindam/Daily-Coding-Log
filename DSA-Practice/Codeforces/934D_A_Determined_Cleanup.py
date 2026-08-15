"""
Problem   : A Determined Cleanup
Platform  : Codeforces
Link      : https://codeforces.com/contest/934/problem/D
Date      : 2026-08-15
Difficulty: *2000 (Div 1 B / Div 2 D)
Topics    : math, number-base-representation

Approach:
Given p and k, find non-negative integer coefficients c0, c1, ..., cn-1
(each < k) such that f(-k) = p, i.e. p is represented in "base -k".
Standard negative-base conversion: repeatedly take remainder = p % k
(Python's % always returns non-negative, so this is safe even when
p goes negative), append it as a coefficient, then update
p = (p - remainder) // (-k). Loop terminates once p == 0.

Time complexity : O(log_k |p|)  -- each step roughly divides p by k
Space complexity: O(log_k |p|)  -- storing the coefficient list
"""


# --------------------- Solution --------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    p = int(input_data[0])
    k = int(input_data[1])
    coefficients = []
    while p != 0:
        remainder = p % k
        coefficients.append(remainder)
        p = (p - remainder) // (-k)
    print(len(coefficients))
    print(*coefficients)

if __name__ == "__main__":
    solve()
