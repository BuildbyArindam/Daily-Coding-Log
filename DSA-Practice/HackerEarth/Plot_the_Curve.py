"""
Platform   : HackerEarth
Problem    : Plot the Curve
Link       : https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/lets-plot-this-47a575ed/
Difficulty : Easy
Topics     : Data Structures, Hash Tables, Hash Maps
Date       : 2026-09-30

Approach:
    Count ordered pairs (i, j) where a*A[i]^3 + b*A[i]^2 + c*A[i] + d
    is congruent to A[j]^2 (mod m).
    1. Build a hash map of A[j]^2 mod m -> frequency in one pass.
    2. For each A[i], evaluate the cubic mod m with Horner's method
       (keeps intermediate values small) and add the frequency of that
       value from the map.
    3. Print the total modulo 10^9 + 7.

Complexity (per test case):
    Time  : O(N), one pass to build the map, one pass to query it
    Space : O(N) for the hash map
"""


# --------------------------------------- Solution ----------------------------------------------


import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        a, b, c, d, m = map(int, input().split())
        n = int(input())
        A = list(map(int, input().split()))
        square_count = {}
        for x in A:
            r = x % m
            sq = (r * r) % m
            square_count[sq] = square_count.get(sq, 0) + 1
        ans = 0
        for x in A:
            r = x % m
            target = (((a % m) * r + (b % m)) * r + (c % m)) * r + (d % m)
            target %= m
            ans += square_count.get(target, 0)
        print(ans % MOD)

if __name__ == "__main__":
    solve()
