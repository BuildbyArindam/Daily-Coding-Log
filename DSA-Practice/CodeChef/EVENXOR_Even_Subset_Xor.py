"""
Problem : Even Subset Xor (EVENXOR)
Link    : https://www.codechef.com/problems/EVENXOR
Platform: CodeChef
Date    : 2026-09-29
Topics  : bitwise-xor, simple

Approach:
  Popcount parity is linear under XOR: parity(a ^ b) = parity(a) ^ parity(b).
  So the set of numbers with even popcount is closed under XOR, and the XOR
  of any subset of them also has even popcount. Precompute the first 1000
  such numbers once (the loop stops after ~2000 iterations, since about half
  of all integers have even popcount), then answer each test case by
  printing the first N of them.

Complexity:
  Precompute: O(1) (bounded, ~2000 iterations)
  Per test  : O(N) to print
  Space     : O(1000) for the precomputed list

Note: int.bit_count() requires Python 3.10+.
"""


# ---------------------------------- Solution ------------------------------------------


import sys
input = sys.stdin.readline
special = []
for x in range(1 << 20):
    if x.bit_count() % 2 == 0:
        special.append(x)
        if len(special) == 1000:
            break
T = int(input())
for _ in range(T):
    N = int(input())
    print(*special[:N])
