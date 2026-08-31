"""
Problem   : Ninja and the Nested Ranges II
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/ninja-and-the-nested-ranges-ii_1467998
Difficulty: Hard
Date      : 2026-08-31
Topics: Fenwick Tree / BIT, Coordinate Compression, Offline Query Processing, Sorting by Intervals, Interval Containment Counting

Approach:
    - Sort intervals by (left ascending, right descending) so that when
      processing left-to-right, any interval containing the current one
      has already been "opened" but not yet closed in a way that breaks
      containment counting.
    - Coordinate-compress the right endpoints for BIT indexing.
    - Pass 1 (forward through sorted order): for each interval, count how
      many previously processed intervals have a right endpoint >= this
      one's right endpoint -> gives "contained_by" count (how many ranges
      strictly contain this one).
    - Pass 2 (reverse through sorted order): count how many later-processed
      intervals have right endpoint <= this one's -> gives "contains" count
      (how many ranges this one strictly contains).

Time complexity : O(n log n)   -- sorting + BIT updates/queries
Space complexity: O(n)         -- BIT array, rank map, output arrays
"""


# ---------------------------- Solution --------------------------------


from os import *
from sys import *
from collections import *
from math import *

def nestedRangesCount(ranges, n):
    arr = [(ranges[i][0], ranges[i][1], i) for i in range(n)]
    arr.sort(key=lambda x: (x[0], -x[1]))
    rights = sorted(set(b for _, b, _ in arr))
    rank = {b: i + 1 for i, b in enumerate(rights)}
    m = len(rights)
    def update(bit, idx, value):
        while idx <= m:
            bit[idx] += value
            idx += idx & -idx
    def query(bit, idx):
        total = 0
        while idx > 0:
            total += bit[idx]
            idx -= idx & -idx
        return total
    contains = [0] * n
    contained_by = [0] * n
    bit = [0] * (m + 1)
    processed = 0
    for a, b, idx in arr:
        r = rank[b]
        not_containing = query(bit, r - 1)
        contained_by[idx] = processed - not_containing
        update(bit, r, 1)
        processed += 1
    bit = [0] * (m + 1)
    for a, b, idx in reversed(arr):
        r = rank[b]
        contains[idx] = query(bit, r)
        update(bit, r, 1)
    return [contains, contained_by]
