"""
Platform   : CodeChef
Problem    : OR Tuples (ORTUPLES)
Link       : https://www.codechef.com/problems/ORTUPLES
Difficulty : 1703
Date       : 2026-09-24
Topics     : Bit Manipulation, Combinatorics, Math

Approach:
    Bits are independent, so analyse each bit position of (P, Q, R) separately.
    - Exactly one of the three bits set  -> impossible, so the answer is 0.
      Detected in O(1) via (P ^ Q ^ R) & ~(P & Q & R).
    - All three bits set                 -> 4 valid bit assignments.
    - Any other pattern (0, 0, 0 or two bits set) -> exactly 1 assignment.
    So the answer is 4^k, where k = popcount(P & Q & R), or 0 if impossible.

Time  : O(1) per test case (bit ops on fixed-width ints), O(T) overall
Space : O(1)
"""


# ------------------------------------ Solution ---------------------------------------------


import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    P, Q, R = map(int, input().split())
    exactly_one = (P ^ Q ^ R) & ~(P & Q & R)
    if exactly_one:
        print(0)
    else:
        k = (P & Q & R).bit_count()
        print(4 ** k)
