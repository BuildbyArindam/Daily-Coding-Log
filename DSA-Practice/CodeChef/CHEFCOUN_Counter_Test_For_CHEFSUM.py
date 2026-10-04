"""
Platform   : CodeChef
Problem    : Counter Test For CHEFSUM (CHEFCOUN)
Link       : https://www.codechef.com/problems/CHEFCOUN
Difficulty : 1802
Topics     : Basic Math, Ad-hoc, Constructive, Prefix Sum, Suffix Sum
Date       : 2026-10-04

Approach:
    Constructive. With M = 2^32 - 1, split M evenly across n + 1 slots to get
    q = M // (n + 1) and remainder r = M % (n + 1). Every element is q, except
    the first, which is bumped by r // 2 + 2 so the array is no longer uniform
    and the tie-breaking breaks. This keeps all values and sums
    within the 32-bit bound the problem works with.

Complexity:
    Time  : O(n) per test case, O(sum of n) overall
    Space : O(n) for the constructed array and output buffer
"""


# -------------------------------------- Solution -------------------------------------------------


import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    M = (1 << 32) - 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        q = M // (n + 1)
        r = M % (n + 1)
        first = q + (r // 2) + 2
        arr = [first] + [q] * (n - 1)
        out.append(" ".join(map(str, arr)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
