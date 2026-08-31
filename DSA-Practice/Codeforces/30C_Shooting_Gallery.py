"""
Problem   : Shooting Gallery
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/30/C
Difficulty: *1800
Topics    : DP, Probabilities
Date      : 2026-08-31

Approach:
    Sort targets by appearance time t. dp[i] = max expected score of a
    valid shooting sequence ending at target i, where dp[i] = p_i +
    max(dp[j]) over all j appearing strictly before i such that the
    sight can physically travel from j's position to i's position in
    the available time (dx^2 + dy^2 <= dt^2, since sight speed = 1).
    Answer = max(dp[i]) over all i (or 0 if no targets shot).

Complexity:
    Time : O(n^2)  — for each target, scan all earlier targets.
    Space: O(n)    — dp array plus sorted target list.
"""


# --------------------------- Solution -----------------------------------


import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    targets = []
    for _ in range(n):
        x, y, t, p = input().split()
        targets.append((int(t), int(x), int(y), float(p)))
    targets.sort()
    dp = [0.0] * n
    answer = 0.0
    for i in range(n):
        ti, xi, yi, pi = targets[i]
        dp[i] = pi
        for j in range(i):
            tj, xj, yj, _ = targets[j]
            if tj >= ti:
                continue
            dt = ti - tj
            dx = xi - xj
            dy = yi - yj
            if dx * dx + dy * dy <= dt * dt:
                dp[i] = max(dp[i], dp[j] + pi)
        answer = max(answer, dp[i])
    print(f"{answer:.10f}")

if __name__ == "__main__":
    solve()
