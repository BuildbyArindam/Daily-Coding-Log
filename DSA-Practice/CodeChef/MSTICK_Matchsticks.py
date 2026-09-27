"""
Problem: Matchsticks
Platform: CodeChef
Link: https://www.codechef.com/problems/MSTICK
Date solved: 2026-09-27
Difficulty: 1714
Topics: Sparse Table, RMQ, Prefix/Suffix Max

Approach:
    For each query [l, r], the stick that finishes last is either:
      1. One of the two ends of the range being lit simultaneously from
         both directions, meeting at (max_burn_time_in_range + min_burn_time_in_range) / 2, or
      2. A stick outside the range whose fire reaches the nearer boundary
         and then burns inward, taking (max_burn_time_outside_range + min_burn_time_in_range).
    min_burn_time_in_range and max_burn_time_in_range are found using a sparse table (RMQ),
    and the max burn time just outside the range on each side is found using
    prefix-max / suffix-max arrays.

Time complexity:  O(n log n) preprocessing (sparse table) + O(1) per query for
                   range-min/range-max lookups -> O(n log n + q)
Space complexity: O(n log n) for the sparse tables
"""


# ------------------------------------- Solution -------------------------------------------


import sys

def solve():
    raw = sys.stdin.buffer.read().split()
    pos = 0
    total_sticks = int(raw[pos]); pos += 1
    burn = [int(x) for x in raw[pos:pos + total_sticks]]; pos += total_sticks
    query_count = int(raw[pos]); pos += 1
    asks = []
    for _ in range(query_count):
        left, right = int(raw[pos]), int(raw[pos + 1])
        pos += 2
        asks.append((left, right))
    n = total_sticks
    NEG_INF = float('-inf')
    pre_max = [NEG_INF] * n
    suf_max = [NEG_INF] * n
    running = NEG_INF
    for idx in range(n):
        running = burn[idx] if burn[idx] > running else running
        pre_max[idx] = running
    running = NEG_INF
    for idx in range(n - 1, -1, -1):
        running = burn[idx] if burn[idx] > running else running
        suf_max[idx] = running
    table_min = [burn[:]]
    table_max = [burn[:]]
    level = 1
    while (1 << level) <= n:
        width = 1 << level
        half = width >> 1
        prev_min = table_min[-1]
        prev_max = table_max[-1]
        cnt = n - width + 1
        table_min.append([prev_min[i] if prev_min[i] < prev_min[i + half] else prev_min[i + half]
                           for i in range(cnt)])
        table_max.append([prev_max[i] if prev_max[i] > prev_max[i + half] else prev_max[i + half]
                           for i in range(cnt)])
        level += 1

    def range_min(l, r):
        span = r - l + 1
        k = span.bit_length() - 1
        a = table_min[k][l]
        b = table_min[k][r - (1 << k) + 1]
        return a if a < b else b

    def range_max(l, r):
        span = r - l + 1
        k = span.bit_length() - 1
        a = table_max[k][l]
        b = table_max[k][r - (1 << k) + 1]
        return a if a > b else b
    out_lines = []
    for l, r in asks:
        knot_time = range_min(l, r) 
        biggest_in_range = range_max(l, r)
        finish_lit = (biggest_in_range + knot_time) / 2.0
        outside_candidates = []
        if l > 0:
            outside_candidates.append(pre_max[l - 1])
        if r < n - 1:
            outside_candidates.append(suf_max[r + 1])
        if outside_candidates:
            biggest_outside = max(outside_candidates)
            finish_unlit = biggest_outside + knot_time
            answer = finish_lit if finish_lit > finish_unlit else finish_unlit
        else:
            answer = finish_lit
        out_lines.append(f"{answer:.1f}")
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    solve()
