"""
Problem   : Zeros and Ones (K-th Bit)
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/k-th-bit-faae0e0d/
Difficulty: Easy
Topics    : Bit Manipulation, Data Structures, Fenwick Tree (BIT)
Date      : 2026-08-19

Approach:
    - Maintain a Fenwick Tree (BIT) over n positions, where each position
      starts as 1 (bit is "set"). bit[] stores prefix counts of set bits.
    - Type 0 query (turn off bit at idx): standard point update, -1 at
      that index, only if it hasn't already been turned off.
    - Type 1 query (find k-th set bit): binary lifting over the BIT —
      walk down powers of two, greedily extending the index as long as
      the accumulated count stays below k. This locates the smallest
      index whose prefix sum reaches k in O(log n), instead of binary
      searching + querying separately (O(log^2 n)).
    - is_one[] guards against double-decrementing an already-zeroed index.

Complexity:
    Time  : O((n + q) log n)  -> O(n) BIT build, O(log n) per update/query
    Space : O(n)              -> bit[] and is_one[] arrays
"""


# ------------------------- Solution ---------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    q = int(input_data[1])
    bit = [0] * (n + 1)
    def add(idx, val):
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)
    for i in range(1, n + 1):
        bit[i] += 1
        nxt = i + (i & (-i))
        if nxt <= n:
            bit[nxt] += bit[i]
    is_one = [True] * (n + 1)
    max_pow = 1
    while max_pow * 2 <= n:
        max_pow *= 2
    ptr = 2
    out = []
    for _ in range(q):
        op = input_data[ptr]
        val = int(input_data[ptr + 1])
        ptr += 2
        if op == '0':
            if is_one[val]:
                is_one[val] = False
                add(val, -1)
        else:
            k = val
            idx = 0
            curr_sum = 0
            step = max_pow
            while step > 0:
                nxt = idx + step
                if nxt <= n and curr_sum + bit[nxt] < k:
                    idx = nxt
                    curr_sum += bit[nxt]
                step >>= 1
            ans = idx + 1
            if ans <= n:
                out.append(str(ans))
            else:
                out.append("-1")   
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
