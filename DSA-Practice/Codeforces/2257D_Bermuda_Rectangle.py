"""
Problem   : D. Bermuda Rectangle
Contest   : Codeforces Round 1117 (Div. 2)
Link      : https://codeforces.com/contest/2257/problem/D
Date      : 2026-08-18
Difficulty: ~1900-2100 (est., Div. 2 D) - verify exact rating on the CF problem page

Approach:
  The area S is fixed, so every valid "Bermuda Rectangle" has integer side
  pair (a, b) with a * b = S. Enumerate all divisors of S in O(sqrt(S)).
  These divisor pairs form a staircase-shaped region F in the (x, y) plane
  (union of all a x b rectangles). For a query rectangle (x, y), the answer
  is the area of F intersected with [0, x] x [0, y].

  Precompute F as a set of horizontal "blocks" (constant-height segments)
  sorted by x-range, plus a prefix-sum array of area accumulated up to each
  block. For each query, binary search for the block boundary where F's
  staircase height drops below x, then use the prefix sums to compute the
  intersection area in O(log(sqrt(S))) per query.

Complexity:
  Preprocessing (per test case): O(sqrt(S)) to find divisors + build blocks
                                   + prefix sums.
  Per query:                      O(log(sqrt(S))) via binary search.
  Overall:                        O(sqrt(S) + Q log(sqrt(S))) per test case.
  Space:                          O(sqrt(S)) for divisor/block/prefix arrays.
"""


# ------------------- Solution ------------------------------


import sys, math
from bisect import bisect_left

def gather_divisors(n):
    root = math.isqrt(n)
    lows = []
    for i in range(1, root + 1):
        if n % i == 0:
            lows.append(i)
    highs = [n // i for i in lows]
    combo = set(lows)
    combo.update(highs)
    return sorted(combo)

def build_blocks(total, div_list):
    starts = [0]
    ends = [0]
    vals = [total]
    if total > 1:
        cap = total - 1
        count = len(div_list)
        stash = []
        pos = count - 2
        while pos >= 0:
            cur = div_list[pos]
            nxt = div_list[pos + 1]
            top = cap // cur
            bottom = cap // nxt + 1
            if bottom <= top:
                stash.append((bottom, top, cur))
            pos -= 1
        for lo, hi, v in stash:
            starts.append(lo)
            ends.append(hi)
            vals.append(v)
    return starts, ends, vals

def make_prefix(starts, ends, vals):
    m = len(vals)
    running = [0] * m
    running[0] = vals[0] * (ends[0] - starts[0] + 1)
    for p in range(1, m):
        running[p] = running[p - 1] + vals[p] * (ends[p] - starts[p] + 1)
    return running

def answer_query(x, y, starts, ends, vals, running, seg_cnt, cap_val):
    left, right = 0, seg_cnt
    while left < right:
        mid = (left + right) >> 1
        if vals[mid] < x:
            right = mid
        else:
            left = mid + 1
    split_j = starts[left] if left < seg_cnt else cap_val
    boundary = split_j if split_j < y else y
    def prefix_sum(n):
        if n <= 0:
            return 0
        tgt = n - 1
        idx = bisect_left(ends, tgt)
        base = running[idx - 1] if idx > 0 else 0
        return base + vals[idx] * (n - starts[idx])
    return x * boundary + prefix_sum(y) - prefix_sum(boundary)

def main():
    raw = sys.stdin.buffer.read().split()
    cursor = 0
    cases = int(raw[cursor]); cursor += 1
    output_lines = []
    for _ in range(cases):
        area = int(raw[cursor]); num_q = int(raw[cursor + 1]); cursor += 2
        divs = gather_divisors(area)
        starts, ends, vals = build_blocks(area, divs)
        running = make_prefix(starts, ends, vals)
        seg_cnt = len(vals)
        for _ in range(num_q):
            qx = int(raw[cursor]); qy = int(raw[cursor + 1]); cursor += 2
            output_lines.append(
                answer_query(qx, qy, starts, ends, vals, running, seg_cnt, area)
            )
    sys.stdout.write('\n'.join(map(str, output_lines)))

if __name__ == "__main__":
    main()
