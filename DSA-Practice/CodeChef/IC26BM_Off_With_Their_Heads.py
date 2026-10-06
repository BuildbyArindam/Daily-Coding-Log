"""
Problem   : Off With Their Heads (IC26BM)
Platform  : CodeChef - ICPCOL26POST
Link      : https://www.codechef.com/ICPCOL26POST/problems/IC26BM
Date      : 2026-10-06
Difficulty: Hard
Topics    : Greedy, Strings, Constructive, Casework

Approach  : Input gives counts of the four 2-char pieces 00, 01, 10, 11, and
            the output is the lexicographically smallest string.
            Greedy with casework:
            - Try each available piece as the one placed last (11, 10, 01, 00).
            - Merge the remaining pieces greedily with _mk(): pair 00/01/11
              pieces up to m = min((p00+p01+p11)//2, p11+p01, p00+p01),
              giving a count of zeros, "01" blocks and ones.
            - 10 pieces are folded into the zeros prefix.
            - Build "0"*z + "01"*t + "1"*o + last piece for each candidate
              and keep the lexicographically smallest.

Complexity: Time  O(N) per test, where N is the output length (4 candidates,
                  each built in O(N)).
            Space O(N) for the candidate strings.
"""


# ---------------------------------------- Solution -------------------------------------------------------------


import sys

def _mk(p00, p01, p11):
    m = min((p00 + p01 + p11) // 2, p11 + p01, p00 + p01)
    both00 = min(p00, m)
    both01 = m - both00
    gone11 = min(p11, m)
    gone01 = m - gone11
    zeros = p00 + both00
    ones = (p01 - gone01 - both01) + (p11 - gone11)
    return zeros, both01, ones

def solve(cnt):
    a, b, c, d = cnt
    labels = ("00", "01", "10", "11")
    best = None
    for k in (3, 2, 1, 0):
        if cnt[k] == 0:
            continue
        cur = list(cnt)
        cur[k] -= 1
        z, t, o = _mk(cur[0], cur[1], cur[3])
        z += cur[2]
        cand = "0" * z + "01" * t + "1" * o + labels[k]
        if best is None or cand < best:
            best = cand
    return best

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    pos = 1
    while t:
        t -= 1
        row = (int(data[pos]), int(data[pos + 1]), int(data[pos + 2]), int(data[pos + 3]))
        pos += 4
        out.append(solve(row))
    sys.stdout.write("\n".join(out) + "\n")

main()
