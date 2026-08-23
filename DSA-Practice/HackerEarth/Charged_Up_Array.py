"""
Problem: Charged Up Array
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/charged-up-array-f35a5e23/
Difficulty: Easy
Topics: Arrays, Data Structures, One-dimensional
Date Solved: 2026-08-23

Approach:
    For each test case, compute a threshold K_i = 2^(N-1). Sum all
    array elements that are >= K_i, taking the result modulo 1e9+7.
    Since K_i grows exponentially with N, once N >= 60, K_i exceeds
    any value representable/plausible in input constraints, so the
    answer is trivially 0 — we still consume the N tokens for that
    test case to keep the stream aligned, then print 0.

Time Complexity:  O(N) per test case  ->  O(sum of N) overall
Space Complexity: O(1) extra (excluding input buffering)
"""


# ----------------------- Solution ---------------------------


import sys

MOD = 10**9 + 7
def solve():
    def token_generator():
        for line in sys.stdin:
            for token in line.split():
                yield token
    tokens = token_generator()
    try:
        first_token = next(tokens)
    except StopIteration:
        return
    T = int(first_token)
    for _ in range(T):
        N = int(next(tokens))
        if N >= 60:
            for _ in range(N):
                next(tokens)
            print(0)
            continue
        K_i = 1 << (N - 1)
        total_charge = 0
        for _ in range(N):
            x = int(next(tokens))
            if x >= K_i:
                total_charge = (total_charge + x) % MOD
        print(total_charge)

if __name__ == "__main__":
    solve()
