"""
Problem: Don't fear, DravDe is kind
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/28/D
Date: 2026-08-29
Difficulty: *2400
Topics: Binary Search, Data Structures, DP, Hashing

Approach:
Each robot part is defined by (v, c, l, r) where v = value/power,
c = length of straight segment, l/r = radii of left/right hemispheres.
A valid "creature" is a chain of parts where each part's right hemisphere
radius equals the next part's left hemisphere radius, and the total
diameter (l + c + r) is constant across the whole chain.
The first part in a chain must have l == 0, and the last must have r == 0.

We do a DP over parts (in input order) keyed by (total_diameter, join_radius),
where join_radius is the radius that the NEXT part must match on its l side.
dp[(total, radius)] = (best_value_so_far, index_of_part_achieving_it, chain_length)

For each part i:
  - Try starting a new chain here (if l == 0).
  - Try extending the best existing chain ending in a part whose r == this l
    and whose total diameter matches.
  - Store the best result under key (total, l + c) for future parts to extend.
  - If r == 0, this part can end a chain — check if it beats the global best.

Parent pointers reconstruct the actual sequence of part indices.

Time complexity: O(n log n) — n parts, dict lookups are O(1) average,
                  dominated by input parsing / iteration.
Space complexity: O(n) — dp dictionary and parent array sized to n.
"""


# --------------------------------- Solution -------------------------------------


import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    dp = {}
    parent = [0] * (n + 1)
    best_value = 0
    best_last = 0
    pos = 1
    for i in range(1, n + 1):
        v = data[pos]
        c = data[pos + 1]
        l = data[pos + 2]
        r = data[pos + 3]
        pos += 4
        total = l + c + r
        cur_value = -1
        prev_idx = 0
        cur_len = 0
        if l == 0:
            cur_value = v
            cur_len = 1
        prev = dp.get((total, l))
        if prev is not None:
            prev_value, prev_idx_candidate, prev_len = prev
            candidate = prev_value + v
            if candidate > cur_value:
                cur_value = candidate
                prev_idx = prev_idx_candidate
                cur_len = prev_len + 1
        if cur_value >= 0:
            parent[i] = prev_idx
            key = (total, l + c)
            old = dp.get(key)
            if old is None or cur_value > old[0]:
                dp[key] = (cur_value, i, cur_len)
            if r == 0 and cur_value > best_value:
                best_value = cur_value
                best_last = i
    answer = []
    cur = best_last
    while cur != 0:
        answer.append(cur)
        cur = parent[cur]
    answer.reverse()
    print(len(answer))
    print(*answer)

if __name__ == "__main__":
    solve()
