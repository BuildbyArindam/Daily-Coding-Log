"""
Problem   : Minimal Usage (MNUSE)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MNUSE
Difficulty: 2018
Topics    : Math, Casework, Constructive
Date      : 2026-10-28

Approach:
    Try each possible count `used` from 0..K in increasing order. For a given
    `used`, the remaining `rest = K - used` items must make up the leftover
    target. Whether that is achievable is decided in O(1) by chk(), which
    handles the cases by closed-form casework: no forbidden value, forbidden
    value at the top of the range, a single item, size == 3 (parity), and the
    two boundary cases where the target is one step from an extreme.
    The first feasible `used` is the minimum, so we stop there. If none is
    feasible, the answer defaults to K.

Complexity:
    Time : O(K) per test case (O(1) per check), O(sum of K) overall
    Space: O(1) extra, plus O(T) for the output buffer
"""


# ------------------------------------------ Solution ---------------------------------------------------------


import sys

def chk(cnt, tgt, size, hole):
    if cnt == 0:
        return tgt == 0
    if size == 1:
        return False
    peak = size - 1
    if hole == 0:
        return cnt <= tgt <= cnt * peak
    if hole == peak:
        return 0 <= tgt <= cnt * (size - 2)
    if tgt < 0 or tgt > cnt * peak:
        return False
    if cnt == 1:
        return tgt != hole
    if size == 3:
        return tgt % 2 == 0
    if hole == 1 and tgt == 1:
        return False
    if hole == size - 2 and cnt * peak - tgt == 1:
        return False
    return True

def run():
    tokens = sys.stdin.buffer.read().split()
    cases = int(tokens[0])
    out = []
    ptr = 1
    for _ in range(cases):
        M = int(tokens[ptr + 3])
        S = int(tokens[ptr + 2])
        K = int(tokens[ptr + 1])
        N = int(tokens[ptr])
        ptr += 4
        gap = M - 1
        best = K
        for used in range(K + 1):
            rest = K - used
            if chk(rest, S - used * M - rest, N, gap):
                best = used
                break
        out.append(best)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

run()
