"""
Problem   : Bath Queue
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/28/C
Difficulty: *2200
Topics    : Combinatorics, DP, Probability
Date      : 2026-08-29

Approach:
    Compute E[max queue length] via E[X] = sum_{t=0}^{max_x-1} P(X > t).
    For a fixed threshold t, P(max_i queue_i <= t) is found by counting,
    over all m^n equally likely room-assignment sequences, the number of
    ways to distribute n students into n rooms such that room i receives
    at most a[i]*t students. This is done with a DP over "students placed
    so far" using the multinomial-style transition
    ndp[s] = sum_k dp[s-k] * C(s, k), where k (0..min(cap_i, s)) is the
    count assigned to room i and C(s, k) picks which of the s students
    go to this room. Summing 1 - P(X <= t) over t gives E[X].

Complexity:
    Time : O(max_x * n * n^2) = O(n^4 / min(a))  (inner double loop over
           s and k for each of n rooms, repeated max_x times)
    Space: O(n^2) for the Pascal's triangle table, O(n) for the DP array
"""


# ------------------------- Solution --------------------------------


import sys
from math import comb

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = m ** n
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = C[i][i] = 1
        for j in range(1, i):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    def probability_leq(t):
        """
        Probability that the maximum queue size is <= t.
        This means room i receives at most a[i] * t students.
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        for ai in a:
            cap = ai * t
            ndp = [0] * (n + 1)
            for s in range(n + 1):
                max_k = min(cap, s)
                for k in range(max_k + 1):
                    ndp[s] += dp[s - k] * C[s][k]
            dp = ndp
        return dp[n] / total
    max_x = (n + min(a) - 1) // min(a)
    expected = 0.0
    for t in range(max_x):
        p_leq = probability_leq(t)
        expected += 1.0 - p_leq
    print("{:.15f}".format(expected))

if __name__ == "__main__":
    solve()
