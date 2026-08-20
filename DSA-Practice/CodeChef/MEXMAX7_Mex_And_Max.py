"""
Problem   : Mex and Max (MEXMAX7)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MEXMAX7
Date      : 2026-08-20
Topics    : Combinatorics, Counting, Prefix Products, MEX
Difficulty: Medium

Approach:
Count subsequences S where |max(S) - mex(S)| <= 1, i.e. mex(S) is in
{max(S)-1, max(S), max(S)+1}. Fix M = max(S) (the largest chosen element).
For each M, freq[0..M-1] must each contribute >=1 copy (to keep mex >= M
or handle mex == M-1 boundary), while at least one copy of value M is
picked (fixes the max), and elements > M+1 are excluded entirely.
- ans starts with subsequences where max = 1 (mex = 0 case, i.e. only
  1s chosen): 2^cnt[1] - 1.
- pref tracks the running product of (2^cnt[v] - 1) for v = 0..m-1,
  i.e. number of ways to pick >=1 of each required smaller value.
- For each candidate max m: add pref (mex == m case) and, if m+1 <= N,
  add pref * (2^cnt[m+1] - 1) (mex == m+1 case, forcing >=1 copy of m+1
  without it being the max... handled via extra term).
- pref is updated by multiplying in (2^cnt[m] - 1) after processing m.
All counts taken mod 998244353.

Time complexity : O(N) per test case (after O(maxN) pow2 precompute)
Space complexity: O(N) for frequency array
"""


# ------------------------ Solution --------------------------


import sys
MOD = 998244353

def solve():
    input = sys.stdin.readline
    T = int(input())
    pow2 = [1] * 105
    for i in range(1, 105):
        pow2[i] = (pow2[i - 1] * 2) % MOD
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        cnt = [0] * (N + 2)
        for x in A:
            cnt[x] += 1
        ans = 0
        ans = (pow2[cnt[1]] - 1) % MOD
        pref = (pow2[cnt[0]] - 1) % MOD
        for m in range(1, N + 1):
            ans = (ans + pref) % MOD
            if m + 1 <= N:
                extra = (pow2[cnt[m + 1]] - 1) % MOD
                ans = (ans + pref * extra) % MOD
            if m <= N:
                pref = pref * (pow2[cnt[m]] - 1) % MOD
        print(ans)

if __name__ == "__main__":
    solve()
