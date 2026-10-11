"""
Problem   : Supertables
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/supertables-3/
Difficulty: Medium
Topics    : Binary Search, Math, Sorting
Date      : 2026-10-11

Approach:
    The task is to find the N-th smallest number divisible by A or B.
    Binary search on the answer. For a candidate value x, the count of
    valid numbers <= x follows from inclusion-exclusion:
        count(x) = x//A + x//B - x//lcm(A, B)
    The smallest x with count(x) >= N is the answer. The upper bound is
    min(A, B) * N, since multiples of the smaller number alone already
    give N valid values by then.

Complexity:
    Time : O(T * log(min(A, B) * N)) over T test cases
    Space: O(1) extra per test case (O(T) for stored output)
"""


# ---------------------------------------- Solution --------------------------------------------------------------


import sys
from math import gcd

def solve(A, B, N):
    lcm = (A * B) // gcd(A, B)
    low = 1
    high = min(A, B) * N
    while low < high:
        mid = (low + high) // 2
        count = mid // A + mid // B - mid // lcm
        if count >= N:
            high = mid
        else:
            low = mid + 1
    return low
data = list(map(int, sys.stdin.buffer.read().split()))
T = data[0]
idx = 1
ans = []
for _ in range(T):
    A, B, N = data[idx], data[idx + 1], data[idx + 2]
    idx += 3
    ans.append(str(solve(A, B, N)))
sys.stdout.write("\n".join(ans))
