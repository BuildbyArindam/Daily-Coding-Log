"""
Problem: Infinite Arrays
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/infinity-array-715a233b/
Difficulty: Easy
Date Solved: 2026-08-23

Approach:
Build a prefix-sum array over one cycle of N elements. Since the array
repeats infinitely, the prefix sum up to any index x can be decomposed
into (full_cycles * total_sum_of_one_cycle) + (prefix_sum_of_remainder).
Each range query [l, r] is answered as get_prefix_sum(r) - get_prefix_sum(l-1),
mod 1e9+7.

Time Complexity: O(N + Q) per test case
Space Complexity: O(N) per test case
"""


# --------------------------- Solution -------------------------------


import sys

def solve():
    def token_generator():
        for line in sys.stdin:
            for token in line.split():
                yield token
    tokens = token_generator()
    MOD = 10**9 + 7
    try:
        first_token = next(tokens)
    except StopIteration:
        return
    T = int(first_token)
    for _ in range(T):
        N = int(next(tokens))
        pref = [0] * (N + 1)
        for i in range(1, N + 1):
            pref[i] = pref[i - 1] + int(next(tokens))
        total_sum = pref[N]
        Q = int(next(tokens))
        L = [int(next(tokens)) for _ in range(Q)]
        def get_prefix_sum(x):
            if x <= 0:
                return 0
            full_cycles = x // N
            remainder = x % N
            return full_cycles * total_sum + pref[remainder]
        ans = []
        for i in range(Q):
            r = int(next(tokens))
            l = L[i]
            res = (get_prefix_sum(r) - get_prefix_sum(l - 1)) % MOD
            ans.append(str(res))
        print(" ".join(ans))

if __name__ == "__main__":
    solve()
