"""
Problem   : Longest Common Subsequence Again
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/lcs-again-43ffb20d/
Difficulty: Medium
Topic     : Dynamic Programming

Approach:
    Variant of LCS where up to (k1 + k2) mismatched character pairs can
    still be counted as a "match" by spending a credit from a combined
    budget k_total = min(k1 + k2, min(len(s), len(p))).
    dp[j][k] = length of the best LCS-with-credits using the first i
    characters of s (rolling dimension) and first j characters of p,
    with k credits still available.
    Transition per (i, j, k):
        - if s[i-1] == p[j-1]: dp[j][k] = prev_dp[j-1][k] + 1
        - else: dp[j][k] = max(
              prev_dp[j][k],            # skip char in s
              dp[j-1][k],               # skip char in p
              prev_dp[j-1][k-1] + 1     # spend a credit to force a match
          )
    The i dimension is rolled (prev_dp = snapshot of dp before row i),
    keeping memory independent of n.

Complexity:
    Time  : O(n * m * k_total)   where n = len(s), m = len(p)
    Space : O(m * k_total)       (rolling over i; prev_dp is a same-size copy)

Date solved: 2026-08-20
"""


# ------------------------- Solution ---------------------------


import sys

def LCS (p, s, k1, k2):
    # Write your code here
    n = len(s)
    m = len(p)
    k_total = min(k1 + k2, min(n, m))
    dp = [[0] * (k_total + 1) for _ in range(m + 1)]
    for i in range(1, n + 1):
        prev_dp = [row[:] for row in dp]
        for j in range(1, m + 1):
            for k in range(k_total + 1):
                if s[i - 1] == p[j - 1]:
                    dp[j][k] = prev_dp[j - 1][k] + 1
                else:
                    res = max(prev_dp[j][k], dp[j - 1][k])
                    if k > 0:
                        res = max(res, prev_dp[j - 1][k - 1] + 1)
                    dp[j][k] = res
    return dp[m][k_total]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]
    p = input_data[1]
    k1 = int(input_data[2])
    k2 = int(input_data[3])
    print(LCS(p, s, k1, k2))

if __name__ == "__main__":
    main()
