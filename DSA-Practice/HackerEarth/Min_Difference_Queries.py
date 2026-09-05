"""
Problem   : Min Difference Queries
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/min-difference-queries-f5b9c199/
Difficulty: Medium
Topics    : Advanced Data Structures, Segment Trees, Offline Queries, Bitset Tricks

Date solved: 2026-09-05

Approach:
    For each query (l, r), we need the minimum pairwise difference between
    frequencies of distinct values in a[l..r] restricted to at most k(len)
    distinct values (k(len) is the largest k with k*(k+1)/2 <= len, since
    that many distinct values each needing a different frequency is the
    only way frequencies can stay pairwise-distinct). If the number of
    distinct values with count > 0 in the range exceeds k(len), or any two
    share a frequency, the answer is 0. If there's only one distinct value,
    the answer is -1. Otherwise, the answer is the minimum gap between
    sorted frequencies.

    Key idea: only look at "chunk starts" — positions where a run of the
    same value begins (previous occurrence, if any, lies in an earlier
    64-block). We precompute, per 64-element block, a prefix-OR bitset of
    all chunk-start positions up to and including that block, capped at
    `need = kmax + 64` candidates. For a query range, candidates are
    binary-searched out of the relevant block's candidate list, split into
    "before l" (need bisect-range-count against occurrence lists) and
    "inside [l, r]" (frequency read directly via rank/occ). Queries are
    answered offline with input given as a running XOR-style stream
    (l, r derived from previous answer, per problem's interactive/encoded
    format), input read via sys.stdin for speed.

Time complexity : O((n + q) * (need + log n)) ~= O((n+q) * sqrt(n) ) amortized,
                   since kmax = O(sqrt(n)) and need = kmax + 64.
Space complexity : O(n) for occ/rank/candidates plus O(n/64) bitset buckets.
"""


# -------------------------- Solution --------------------------------


import sys
from bisect import bisect_left, bisect_right

def solve():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    q = next(data)
    value_id = {}
    a = [0] * n
    occ = []
    rank = [0] * n
    for i in range(n):
        v = next(data)
        x = value_id.get(v)
        if x is None:
            x = len(occ)
            value_id[v] = x
            occ.append([])
        a[i] = x
        rank[i] = len(occ[x])
        occ[x].append(i)
    kmax = 0
    while (kmax + 1) * (kmax + 2) // 2 <= n:
        kmax += 1
    k_by_len = [0] * (n + 1)
    k = 0
    for length in range(1, n + 1):
        while (k + 1) * (k + 2) // 2 <= length:
            k += 1
        k_by_len[length] = k
    B = 64
    need = kmax + B
    num_blocks = (n + B - 1) // B
    num_bytes = (n + 7) // 8
    buckets = [bytearray(num_bytes) for _ in range(num_blocks)]
    first_bits = bytearray(num_bytes)
    last_pos = [-1] * len(occ)
    for i, x in enumerate(a):
        p = last_pos[x]
        if p < 0:
            first_bits[i >> 3] |= 1 << (i & 7)
        else:
            b = p >> 6
            buckets[b][i >> 3] |= 1 << (i & 7)
        last_pos[x] = i
    pref = [0] * (num_blocks + 1)
    cur = int.from_bytes(first_bits, "little")
    pref[0] = cur
    for b in range(num_blocks):
        cur |= int.from_bytes(buckets[b], "little")
        pref[b + 1] = cur
    candidates = []
    for b in range(num_blocks):
        start = b * B
        bits = pref[b] >> start
        arr = []
        while bits and len(arr) < need:
            low = bits & -bits
            pos = low.bit_length() - 1
            arr.append(start + pos)
            bits -= low
        candidates.append(arr)
    del buckets
    del first_bits
    del last_pos
    del pref
    mark = [0] * (n + 1)
    out = []
    last = 0
    for query_id in range(1, q + 1):
        u = next(data)
        v = next(data)
        l = (u + last) % n
        r = (v + last) % n
        if l > r:
            l, r = r, l
        length = r - l + 1
        allowed = k_by_len[length]
        block = l >> 6
        cand = candidates[block]
        left_idx = bisect_left(cand, l)
        right_idx = bisect_right(cand, r)
        frequencies = []
        distinct = 0
        for j in range(left_idx):
            p = cand[j]
            x = a[p]
            positions = occ[x]
            cnt = (
                bisect_right(positions, r)
                - bisect_left(positions, l)
            )
            if cnt == 0:
                continue
            distinct += 1
            if distinct > allowed:
                last = 0
                out.append("0")
                break
            if mark[cnt] == query_id:
                last = 0
                out.append("0")
                break
            mark[cnt] = query_id
            frequencies.append(cnt)
        else:
            for j in range(left_idx, right_idx):
                p = cand[j]
                x = a[p]
                cnt = bisect_right(occ[x], r) - rank[p]
                distinct += 1
                if distinct > allowed:
                    last = 0
                    out.append("0")
                    break
                if mark[cnt] == query_id:
                    last = 0
                    out.append("0")
                    break
                mark[cnt] = query_id
                frequencies.append(cnt)
            else:
                if distinct == 1:
                    last = -1
                    out.append("-1")
                else:
                    frequencies.sort()
                    ans = n
                    for i in range(1, len(frequencies)):
                        d = frequencies[i] - frequencies[i - 1]
                        if d < ans:
                            ans = d
                            if ans == 1:
                                break
                    last = ans
                    out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
