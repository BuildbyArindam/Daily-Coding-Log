"""
Problem   : Calm Stretches at Orsel Ridge
Platform  : Unstop
Link      : https://unstop.com/code/practice/670820
Difficulty: Hard
Topics    : Sliding Window, Monotonic Queue, Two Pointers, Prefix Sum, Binary Search
Date      : 2026-11-10

Approach:
  A "calm" subarray has max - min <= tol. For queries [l, r], count all calm
  subarrays inside the range and find the longest one.
  1. Monotonic deques (max and min) with two pointers give starts[i], the
     earliest start such that vals[starts[i]..i] is calm. starts[] is
     non-decreasing.
  2. span[i] = i - starts[i] + 1 is the longest calm subarray ending at i.
     Prefix sums of span[] give range counts.
  3. Per query, binary search for the first index `cut` in [l, r] with
     starts[cut] >= l.
       - Indices l..cut-1 have their start clipped to l, so they contribute
         1 + 2 + ... + m (m = cut - l) subarrays, with longest length m.
       - Indices cut..r use span[] unclipped: count via prefix sums, longest
         via a sparse table (O(1) range max).

Complexity:
  Time : O(n log n + q log n)  (sparse table build + one bisect per query)
  Space: O(n log n)            (sparse table)
"""


# ----------------------------------------------- Solution --------------------------------------------------------------


import sys
from bisect import bisect_left

def build_sparse(arr):
    size = len(arr)
    table = [arr[:]]
    j = 1
    while (1 << j) <= size:
        prev = table[-1]
        half = 1 << (j - 1)
        table.append([a if a > b else b for a, b in zip(prev, prev[half:])])
        j += 1
    return table

def earliest_starts(vals, tol):
    hi_q = []
    lo_q = []
    hh = 0
    lh = 0
    begin = 0
    out = []
    for idx, v in enumerate(vals):
        while len(hi_q) > hh and vals[hi_q[-1]] <= v:
            hi_q.pop()
        hi_q.append(idx)
        while len(lo_q) > lh and vals[lo_q[-1]] >= v:
            lo_q.pop()
        lo_q.append(idx)
        while vals[hi_q[hh]] - vals[lo_q[lh]] > tol:
            begin += 1
            if hi_q[hh] < begin:
                hh += 1
            if lo_q[lh] < begin:
                lh += 1
        out.append(begin)
    return out

def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    q = int(tokens[1])
    tol = int(tokens[2])
    vals = [int(x) for x in tokens[3:3 + n]]
    pos = 3 + n
    starts = earliest_starts(vals, tol)
    span = [i - starts[i] + 1 for i in range(n)]
    pref = [0] * (n + 1)
    acc = 0
    for i in range(n):
        acc += span[i]
        pref[i + 1] = acc
    sp = build_sparse(span)
    answers = []
    for t in range(q):
        lo = int(tokens[pos + 2 * t]) - 1
        hi = int(tokens[pos + 2 * t + 1]) - 1
        cut = bisect_left(starts, lo, lo, hi + 1)
        m = cut - lo
        cnt = m * (m + 1) // 2
        best = m
        if cut <= hi:
            cnt += pref[hi + 1] - pref[cut]
            k = (hi - cut + 1).bit_length() - 1
            row = sp[k]
            a = row[cut]
            b = row[hi - (1 << k) + 1]
            if b > a:
                a = b
            if a > best:
                best = a
        answers.append("%d %d" % (cnt, best))
    sys.stdout.write("\n".join(answers) + "\n")

main()
