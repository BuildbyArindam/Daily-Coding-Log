"""
Problem   : Nil Xor
Platform  : CodeChef
Link      : https://www.codechef.com/problems/NILXOR
Difficulty: 2001
Date      : 2026-10-15
Topics    : Bit Manipulation, Digit Counting

Approach:
    Count values m in [0, n) with (m & x) == 0. Scan bits from LSB to MSB.
    Bits where x has a 1 are forbidden in m, so they are skipped. Bits where
    x has a 0 are "free" positions, numbered 0, 1, 2, ... in order. Wherever
    n has a 1 on a free bit, m can take a 0 there and be anything on the free
    bits below it, which adds 2^(free bits below) to the count. This is the
    same as compressing n onto the free bits (a parallel bit extract of n
    with the mask ~x).

Complexity:
    Time : O(31) per test case, O(T * 31) overall
    Space: O(1) per test case, O(T) for buffered output
"""


# ----------------------------------------------------- Solution -----------------------------------------------------------


import sys

def solve_case(n, x):
    total = 0
    free = 0
    for b in range(31):
        xb = (x >> b) & 1
        nb = (n >> b) & 1
        if xb == 0:
            if nb == 1:
                total += 1 << free
            free += 1
    return total

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    pos = 1
    while t:
        n = int(data[pos])
        x = int(data[pos + 1])
        pos += 2
        out.append(solve_case(n, x))
        t -= 1
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
