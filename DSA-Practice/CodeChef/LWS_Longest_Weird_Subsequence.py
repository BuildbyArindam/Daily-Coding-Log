"""
Problem   : Longest Weird Subsequence (LWS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/LWS
Difficulty: 2011
Date      : 2026-10-23
Topics    : Dynamic Programming, Observation, Arrays, 3D+ Arrays, Data Structures

Approach:
    dp[i][j] = longest valid subsequence so far, where i is the last letter on
    the non-decreasing track (0 = none yet) and j is the last letter on the
    non-increasing track (27 = none yet). For each character v there are two
    transitions:
      1. Extend the non-decreasing track: dp[v][j] = max(dp[i][j] + 1) for i <= v
      2. Extend the non-increasing track: dp[i][v] = max(dp[i][j] + 1) for j >= v
    Both are computed before writing, so v is never used twice. NumPy
    slice-max vectorizes each transition over the 27x28 state table.
    Answer = max over the whole table.

Time    : O(N * A^2) where A = 26, with the inner work vectorized in NumPy
Space   : O(A^2)
"""


# ------------------------------------------- Solution ---------------------------------------------------------


import sys
import numpy as np

def weird_len(word):
    BAD = -10**9
    table = np.full((27, 28), BAD, dtype=np.int64)
    table[0, 27] = 0
    for ch in word:
        v = ord(ch) - 96
        up = table[:v + 1, :].max(axis=0) + 1 
        down = table[:, v:].max(axis=1) + 1  
        table[v, :] = np.maximum(table[v, :], up)
        table[:, v] = np.maximum(table[:, v], down)
    return int(table.max())

def main():
    tokens = sys.stdin.read().split()
    cases = int(tokens[0])
    out = [str(weird_len(w)) for w in tokens[1:1 + cases]]
    print("\n".join(out))

main()
