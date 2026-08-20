"""
Problem   : Modify and Subtract (MODSUB)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MODSUB
Date      : 2026-08-20
Topic     : Prefix Sums / Alternating Prefix Sums, Suffix Min (parity split), Greedy
Difficulty: Medium (official difficulty: TBD)

Approach  :
    For array A, the operation "subtract 1 from A_i and A_{i+1}" can reduce
    A to all zeros iff its alternating prefix sum Q_i = A_i - A_{i-1} + ...
    satisfies Q_i >= 0 for all i, and Q_N = 0.

    For each index k we might replace, exactly one value X restores Q_N = 0
    (since each element contributes one term to the alternating sum). Whether
    the resulting array stays valid depends only on:
      - prefix Q_j (j < k) being unchanged and already >= 0 (prefix_ok array)
      - suffix Q_j (j >= k) shifted by +/-d depending on parity of j vs k,
        checked via parity-bucketed suffix minimums (suf_min[parity][i])

    This makes each candidate index checkable in O(1) after O(N) preprocessing.

Time      : O(N) per test case
Space     : O(N) per test case
"""


# -------------------------------- Solution ------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        x = [0] * (N - 1)
        x[0] = A[0]
        for i in range(1, N - 1):
            x[i] = A[i] - x[i - 1]
        prefix_ok = [True] * (N - 1)
        for i in range(1, N - 1):
            prefix_ok[i] = prefix_ok[i - 1] and (x[i] >= 0)
        prefix_ok[0] = (x[0] >= 0)
        INF = 10**30
        suf_min = [[INF] * (N - 1) for _ in range(2)]
        for i in range(N - 2, -1, -1):
            p = i & 1
            suf_min[p][i] = x[i]
            if i + 1 < N - 1:
                suf_min[p][i] = min(suf_min[p][i], suf_min[p][i + 1])
            if i + 1 < N - 1:
                suf_min[p ^ 1][i] = suf_min[p ^ 1][i + 1]
        ans = 0
        for k in range(N - 1):
            if k > 0 and not prefix_ok[k - 1]:
                continue
            parity = (N - 2 - k) & 1
            d = ((-1) if parity else 1) * (A[N - 1] - x[N - 2])
            same_min = suf_min[k & 1][k]
            other_min = suf_min[(k & 1) ^ 1][k]
            if same_min >= -d and other_min >= d:
                ans += 1
        if prefix_ok[N - 2]:
            ans += 1
        print(ans)

if __name__ == "__main__":
    solve()
