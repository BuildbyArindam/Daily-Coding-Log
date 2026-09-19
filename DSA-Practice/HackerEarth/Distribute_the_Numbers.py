"""
Problem: Distribute the Numbers
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/distribute-the-numbers-8122fa09/
Date: 2026-09-19
Difficulty: Hard
Topics: Binary Search, Number Theory (GCD/LCM)

Approach:
Binary search on the answer 'n' (smallest number such that both people
can get their required counts). For a candidate n, use inclusion-exclusion
with multiples of X, Y, and lcm(X, Y) to check feasibility:
    - bunty_available = n - n//X   (numbers NOT divisible by X)
    - bublee_available = n - n//Y  (numbers NOT divisible by Y)
    - usable = n - n//lcm(X, Y)    (numbers divisible by neither)
Feasible if bunty_available >= N1, bublee_available >= N2, and
usable >= N1 + N2. Binary search finds the minimal such n.

Time Complexity: O(log(total_needed)) per test case for the binary search,
                  O(1) per feasibility check → O(T log(N1+N2)) overall
Space Complexity: O(T) for storing answers
"""


# ---------------------------------- Solution ------------------------------------


import sys
from math import gcd

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    ans = []
    for _ in range(T):
        N1, N2, X, Y = map(int, input().split())
        lcm = X // gcd(X, Y) * Y
        total_needed = N1 + N2
        def possible(n):
            bunty_available = n - n // X
            bublee_available = n - n // Y
            usable = n - n // lcm
            return (
                bunty_available >= N1 and
                bublee_available >= N2 and
                usable >= total_needed
            )
        lo = 1
        hi = 2 * total_needed
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        ans.append(str(lo))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
