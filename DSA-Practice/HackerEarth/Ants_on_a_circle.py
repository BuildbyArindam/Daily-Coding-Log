"""
Problem   : Ants on a circle
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/ants-on-the-circle-928dbbba/
Difficulty: Easy
Topics    : Sorting, Math, Modular Arithmetic
Date      : 2026-10-15

Approach:
    When two ants collide and reverse direction, the set of occupied positions
    is identical to what you'd get if the ants passed through each other,
    since ants are indistinguishable. So each ant is moved independently:
    new_pos = (start - 1 + direction * T) mod N + 1.
    Python's % returns a non-negative result, so negative directions wrap
    correctly. Sort the final positions and print.

Complexity:
    Time  : O(M log M), dominated by sorting the M final positions
    Space : O(M)
"""


# -------------------------------------------- Solution ---------------------------------------------------------


import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    N, M, T = data[:3]
    ants = []
    idx = 3
    for _ in range(M):
        z, y = data[idx], data[idx + 1]
        idx += 2
        pos = ((z - 1 + y * T) % N) + 1
        ants.append(pos)
    ants.sort()
    print(*ants)

if __name__ == "__main__":
    solve()
