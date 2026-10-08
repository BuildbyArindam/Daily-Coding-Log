"""
Problem   : Zulu and Games
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/zulu-and-games-0fee9adb/
Difficulty: Medium
Topics    : Algorithms, Dynamic Programming
Date      : 2026-10-08

Approach:
    - Sort levels by L and coordinate-compress the distinct L values.
    - dp[level] = number of valid ways to reach that level
                = (ways from earlier levels still "active" at this L)
                  + (1 if the level can be a starting level).
    - A level with height h becomes active for the L-groups starting at
      the first L > h, and stays active until the L-groups exceed the
      smallest H among those later groups (suffix minimum).
    - These active ranges are applied with add/remove events (a
      difference array), so each level's dp is computed in one sweep.
    - The answer sums dp * (sum of H >= max L) over all levels that can
      finish, taken modulo 1e9+7.

Complexity:
    Time : O(N log N) -> sorting + bisect lookups per level
    Space: O(N)       -> compressed coordinates, suffix mins, event arrays
"""


# ---------------------------------------------- Solution -----------------------------------------------------------


import sys
from bisect import bisect_right
MOD = 1000000007
INF = 10**30
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
H = list(map(int, input().split()))
levels = sorted(zip(L, H))
coords = sorted(set(L))
m = len(coords)
group_id = {x: i for i, x in enumerate(coords)}
group_min_h = [INF] * m
end_sum = [0] * m
min_h_all = min(H)
max_l_all = max(L)
for l, h in levels:
    g = group_id[l]
    if h < group_min_h[g]:
        group_min_h[g] = h
    if h >= max_l_all:
        end_sum[g] = (end_sum[g] + h) % MOD
suffix_min = [INF] * (m + 1)
for g in range(m - 1, -1, -1):
    suffix_min[g] = min(group_min_h[g], suffix_min[g + 1])
add_event = [0] * (m + 1)
remove_event = [0] * (m + 1)
active = 0
answer = 0
p = 0
while p < N:
    current_l = levels[p][0]
    g = group_id[current_l]
    q = p
    while q < N and levels[q][0] == current_l:
        q += 1
    active = (active - remove_event[g] + add_event[g]) % MOD
    start_count = 1 if min_h_all >= current_l else 0
    dp = (active + start_count) % MOD
    answer = (answer + dp * end_sum[g]) % MOD
    for k in range(p, q):
        _, h = levels[k]
        add_idx = bisect_right(coords, h)
        add_event[add_idx] = (add_event[add_idx] + dp) % MOD
        r = suffix_min[add_idx]
        if r != INF:
            remove_idx = bisect_right(coords, r)
            remove_event[remove_idx] = (
                remove_event[remove_idx] + dp
            ) % MOD
    p = q
print(answer % MOD)
