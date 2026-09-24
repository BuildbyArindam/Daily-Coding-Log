"""
Problem   : Two Dimensional OR
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/two-dimensional-or-daa0a7aa/
Date      : 2026-09-24
Difficulty: Medium
Topics    : Multi-dimensional arrays, Bit manipulation, Prefix/Sparse table

Approach:
    Answer many "OR of a submatrix" queries. OR is idempotent, so overlapping
    ranges are safe and a sparse table works along the row axis.
    1. Build a row-wise sparse table per column: col_table[k][c][r] = OR of
       rows r..r+2^k-1 in column c.
    2. Group columns into blocks of B=24 and build the same sparse table on
       block-level ORs, so wide ranges cost far fewer lookups.
    3. Per query, take k = floor(log2(row_count)) and combine two overlapping
       row windows (r1 and r2-2^k+1). Then OR the leading partial columns,
       the full blocks, and the trailing partial columns.

Complexity:
    Preprocessing: O(n * m * log n) time.
    Query        : O(B + m / B) time, with O(1) row combination.
    Space        : O(n * m * log n), stored in compact array('I') buffers.
    (Assumes values fit in 32 bits, since array('I') is unsigned 32-bit.)
"""


# -------------------------------------------- Solution --------------------------------------------------------


import sys
from array import array

def solve():
    data = sys.stdin.buffer.read().split()
    it = iter(map(int, data))
    n = next(it)
    m = next(it)
    B = 24
    num_blocks = (m + B - 1) // B
    total = n * m
    col0 = array('I', [0]) * total
    block0 = array('I', [0]) * (num_blocks * n)
    for r in range(n):
        for c in range(m):
            v = next(it)
            col0[c * n + r] = v
            b = c // B
            block0[b * n + r] |= v
    col_table = [col0]
    half = 1
    while half * 2 <= n:
        length = half * 2
        valid_rows = n - length + 1
        prev = col_table[-1]
        cur = array('I', [0]) * total
        for c in range(m):
            base = c * n
            other = base + half
            for r in range(valid_rows):
                cur[base + r] = prev[base + r] | prev[other + r]
        col_table.append(cur)
        half *= 2
    block_table = [block0]
    half = 1
    while half * 2 <= n:
        length = half * 2
        valid_rows = n - length + 1
        prev = block_table[-1]
        cur = array('I', [0]) * (num_blocks * n)
        for b in range(num_blocks):
            base = b * n
            other = base + half
            for r in range(valid_rows):
                cur[base + r] = prev[base + r] | prev[other + r]
        block_table.append(cur)
        half *= 2
    q = next(it)
    ans = []
    for _ in range(q):
        x1 = next(it)
        y1 = next(it)
        x2 = next(it)
        y2 = next(it)
        r1 = x1 - 1
        r2 = x2 - 1
        c1 = y1 - 1
        c2 = y2 - 1
        row_len = r2 - r1 + 1
        k = row_len.bit_length() - 1
        span = 1 << k
        r2_start = r2 - span + 1
        col_level = col_table[k]
        block_level = block_table[k]
        result = 0
        first_block = (c1 + B - 1) // B
        last_block = (c2 + 1) // B - 1
        if first_block <= last_block:
            left_end = first_block * B
            for c in range(c1, left_end):
                base = c * n
                result |= (
                    col_level[base + r1] |
                    col_level[base + r2_start]
                )
            for b in range(first_block, last_block + 1):
                base = b * n
                result |= (
                    block_level[base + r1] |
                    block_level[base + r2_start]
                )
            right_start = (last_block + 1) * B
            for c in range(right_start, c2 + 1):
                base = c * n
                result |= (
                    col_level[base + r1] |
                    col_level[base + r2_start]
                )
        else:
            for c in range(c1, c2 + 1):
                base = c * n
                result |= (
                    col_level[base + r1] |
                    col_level[base + r2_start]
                )
        ans.append(str(result))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
