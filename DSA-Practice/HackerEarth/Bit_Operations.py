"""
Problem   : Bit Operations
Platform  : HackerEarth (CodeMonk)
Link      : https://www.hackerearth.com/practice/codemonk/7/1504747/
Difficulty: Easy
Topics    : Bit Manipulation, Segment-free Range Updates
Date      : 2026-09-11

Approach:
    Instead of storing the array directly, maintain 18 separate bitmasks
    (bits[0..17]), one per bit-position. bits[k] is an integer whose bit i
    is set iff a[i] has bit k set. This lets a range update (AND/OR/XOR
    with x on [l, r]) be applied to each of the 18 masks using a single
    range_mask = bits (l..r) set, touching only the bit positions present
    in x. Range sum and range XOR queries are answered by popcounting
    (bits[k] & range_mask) for each k and combining with the right shift.

Complexity (n = array size, q = queries, B = 18 fixed bit-width):
    Time : O(B) per query for the bit-position loop, but each bitwise
           op / popcount on an n-bit integer costs O(n/64) machine words,
           so overall O(B * q * n / 64) ~ effectively O(q) for the
           intended constraints.
    Space: O(B * n / 64) words to store the 18 range bitmasks.
"""


# --------------------------- Solution -------------------------------------


import sys
input = sys.stdin.buffer.readline
name = input()
n, q = map(int, name.split())
BITS = 18
ALL = (1 << BITS) - 1
bits = [0] * BITS
P = [1 << i for i in range(BITS)]
out = []
append = out.append
for _ in range(q):
    data = list(map(int, input().split()))
    typ = data[0]
    l = data[1] - 1
    r = data[2] - 1
    range_mask = (1 << (r + 1)) - (1 << l)
    if typ == 1:
        x = data[3]
        while x:
            b = x & -x
            k = b.bit_length() - 1
            bits[k] |= range_mask
            x -= b
    elif typ == 2:
        x = data[3]
        x = ALL ^ x
        while x:
            b = x & -x
            k = b.bit_length() - 1
            bits[k] &= ~range_mask
            x -= b
    elif typ == 3:
        x = data[3]
        while x:
            b = x & -x
            k = b.bit_length() - 1
            bits[k] ^= range_mask
            x -= b
    elif typ == 4:
        s = 0
        s += (bits[0]  & range_mask).bit_count()
        s += (bits[1]  & range_mask).bit_count() << 1
        s += (bits[2]  & range_mask).bit_count() << 2
        s += (bits[3]  & range_mask).bit_count() << 3
        s += (bits[4]  & range_mask).bit_count() << 4
        s += (bits[5]  & range_mask).bit_count() << 5
        s += (bits[6]  & range_mask).bit_count() << 6
        s += (bits[7]  & range_mask).bit_count() << 7
        s += (bits[8]  & range_mask).bit_count() << 8
        s += (bits[9]  & range_mask).bit_count() << 9
        s += (bits[10] & range_mask).bit_count() << 10
        s += (bits[11] & range_mask).bit_count() << 11
        s += (bits[12] & range_mask).bit_count() << 12
        s += (bits[13] & range_mask).bit_count() << 13
        s += (bits[14] & range_mask).bit_count() << 14
        s += (bits[15] & range_mask).bit_count() << 15
        s += (bits[16] & range_mask).bit_count() << 16
        s += (bits[17] & range_mask).bit_count() << 17
        append(str(s))
    else:
        ans = 0
        if (bits[0]  & range_mask).bit_count() & 1:
            ans |= 1
        if (bits[1]  & range_mask).bit_count() & 1:
            ans |= 2
        if (bits[2]  & range_mask).bit_count() & 1:
            ans |= 4
        if (bits[3]  & range_mask).bit_count() & 1:
            ans |= 8
        if (bits[4]  & range_mask).bit_count() & 1:
            ans |= 16
        if (bits[5]  & range_mask).bit_count() & 1:
            ans |= 32
        if (bits[6]  & range_mask).bit_count() & 1:
            ans |= 64
        if (bits[7]  & range_mask).bit_count() & 1:
            ans |= 128
        if (bits[8]  & range_mask).bit_count() & 1:
            ans |= 256
        if (bits[9]  & range_mask).bit_count() & 1:
            ans |= 512
        if (bits[10] & range_mask).bit_count() & 1:
            ans |= 1024
        if (bits[11] & range_mask).bit_count() & 1:
            ans |= 2048
        if (bits[12] & range_mask).bit_count() & 1:
            ans |= 4096
        if (bits[13] & range_mask).bit_count() & 1:
            ans |= 8192
        if (bits[14] & range_mask).bit_count() & 1:
            ans |= 16384
        if (bits[15] & range_mask).bit_count() & 1:
            ans |= 32768
        if (bits[16] & range_mask).bit_count() & 1:
            ans |= 65536
        if (bits[17] & range_mask).bit_count() & 1:
            ans |= 131072
        append(str(ans))

sys.stdout.write('\n'.join(out))
