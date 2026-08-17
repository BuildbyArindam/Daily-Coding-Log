"""
Problem   : Looking for Order
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/8/C
Difficulty: *2000
Topic     : Bitmask DP
Date      : 2026-08-17

Approach:
    dp[mask] = minimum total travel distance to have picked up exactly
    the set of items in `mask`, always starting/ending each trip at home
    (xs, ys). From any state, only extend the DP by including the
    lowest-indexed unset item ("first") either alone or paired with one
    other unset item `j`:
        - alone : home -> first -> home                (2 * d_bag[first])
        - paired: home -> first -> j -> home            (d_bag[first] + d_obj[first][j] + d_bag[j])
    Restricting transitions to always cover `first` guarantees every
    reachable mask is only visited once per useful transition, which
    collapses the naive O(2^n * n^2) subset-pair DP down to O(2^n * n).
    Path is reconstructed by walking `parent[]` back from the full mask
    and reversing the recovered (mask XOR prev_mask) segments.

Complexity:
    Time : O(2^n * n)      -- n <= 8, so this is trivially fast
    Space: O(2^n + n^2)    -- dp/parent arrays + pairwise distance matrix
"""


# ------------------------ Solution --------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    xs, ys = int(data[0]), int(data[1])
    n = int(data[2])
    coords = []
    idx = 3
    for _ in range(n):
        coords.append((int(data[idx]), int(data[idx + 1])))
        idx += 2
    def dist_sq(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    d_bag = [dist_sq((xs, ys), coords[i]) for i in range(n)]
    d_obj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            d_obj[i][j] = dist_sq(coords[i], coords[j])
    INF = float("inf")
    dp = [INF] * (1 << n)
    parent = [-1] * (1 << n)
    dp[0] = 0
    for mask in range(1 << n):
        if dp[mask] == INF:
            continue
        first = -1
        for i in range(n):
            if not (mask & (1 << i)):
                first = i
                break
        if first == -1:
            continue
        next_mask = mask | (1 << first)
        cost = dp[mask] + 2 * d_bag[first]
        if cost < dp[next_mask]:
            dp[next_mask] = cost
            parent[next_mask] = mask
        for j in range(first + 1, n):
            if not (mask & (1 << j)):
                next_mask = mask | (1 << first) | (1 << j)
                cost = dp[mask] + d_bag[first] + d_obj[first][j] + d_bag[j]
                if cost < dp[next_mask]:
                    dp[next_mask] = cost
                    parent[next_mask] = mask
    full_mask = (1 << n) - 1
    print(dp[full_mask])
    curr = full_mask
    path_segments = []
    while curr > 0:
        prev = parent[curr]
        diff = curr ^ prev
        picked = [i + 1 for i in range(n) if diff & (1 << i)]
        path_segments.append(picked)
        curr = prev
    path_segments.reverse()
    path = [0]
    for seg in path_segments:
        path.extend(seg)
        path.append(0)
    print(" ".join(map(str, path)))

if __name__ == "__main__":
    solve()
