"""
Problem   : Curio Packing (IC26CB)
Platform  : CodeChef - ICPCOL26POST
Link      : https://www.codechef.com/ICPCOL26POST/problems/IC26CB
Date      : 2026-10-06
Difficulty: Medium 
Topics    : DP, State Compression, NumPy

Approach:
    Feasibility check by DP over the pattern string. Each item is a glass 'G'
    (width 1) or another curio (width 2). The DP table is indexed by remaining
    capacity 0..k, plus a sentinel state k+1 for a fresh/unbounded container.
    For each character, the table is rebuilt from two transitions: shifting
    the state by the item's width, and carrying the sentinel state into a new
    container. A cell holds -1 if unreachable. The answer is YES if any state
    remains reachable after the last character. NumPy vectorises the
    per-character transition over all k+2 states.

Complexity (per test case, n = len(pattern)):
    Time : O(n * k)
    Space: O(k)
"""


# ----------------------------------------- Solution ------------------------------------------------


import sys
import numpy as np

def feasible(k, pattern):
    top = k + 1
    table = np.full(k + 2, -1, dtype=np.int64)
    table[top] = top
    for ch in pattern:
        glass = (ch == 'G')
        w = 1 if glass else 2
        fresh = np.full(k + 2, -1, dtype=np.int64)
        if w <= k:
            fresh[0:k + 1 - w] = table[w:k + 1]
        carry = table[top]
        if glass:
            if carry > fresh[k]:
                fresh[k] = carry
        else:
            if carry > fresh[top]:
                fresh[top] = carry
        after_inf = k if glass else top
        moved = np.where(table == top, after_inf, table - w)
        moved[table < w] = -1
        fresh = np.maximum(fresh, moved)
        table = fresh
    return bool(table.max() >= 0)

def main():
    tokens = sys.stdin.read().split()
    cases = int(tokens[0])
    answers = []
    pos = 1
    for _ in range(cases):
        n = int(tokens[pos])
        k = int(tokens[pos + 1])
        pattern = tokens[pos + 2]
        pos += 3
        answers.append("YES" if feasible(k, pattern) else "NO")
    sys.stdout.write("\n".join(answers) + "\n")

main()
