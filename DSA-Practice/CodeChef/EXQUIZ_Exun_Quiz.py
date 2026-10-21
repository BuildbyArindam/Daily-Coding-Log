"""
Problem   : Exun Quiz (EXQUIZ)
Platform  : CodeChef, Starters 261 (START261A)
Link      : https://www.codechef.com/START261A/problems/EXQUIZ
Date      : 2026-10-21
Difficulty: Hard
Topics    : Math, Brute Force, Precomputation

Approach  : Each question attempted is either right (+4) or wrong (-1), and
            skipped questions score 0. Since n <= 50 and the score range is
            small, precompute best[n][s], the minimum number of attempted
            questions needed to score exactly s out of n questions.
            Enumerate every (right, wrong) pair with right + wrong <= n and
            record the smallest right + wrong for each score 4*right - wrong.
            Each test case is then a single table lookup (-1 if unreachable).

Time      : O(N^3) precompute with N = 50, then O(1) per test case
Space     : O(N * S) for the table, S = 200
"""


# ------------------------------------------------- Solution ----------------------------------------------------------------


import sys

def build_table(limit_n=50, limit_s=200):
    INF = 10**9
    best = [[INF] * limit_s for _ in range(limit_n + 1)]
    for n in range(limit_n + 1):
        row = best[n]
        for wrong in range(n + 1):
            for right in range(n - wrong + 1):
                pts = 4 * right - wrong
                if 0 <= pts < limit_s:
                    tries = right + wrong
                    if tries < row[pts]:
                        row[pts] = tries
    return best, INF

def main():
    tokens = sys.stdin.read().split()
    best, INF = build_table()
    t = int(tokens[0])
    out = []
    for k in range(t):
        n = int(tokens[1 + 2 * k])
        s = int(tokens[2 + 2 * k])
        v = best[n][s]
        out.append(str(-1 if v == INF else v))
    print("\n".join(out))

main()
