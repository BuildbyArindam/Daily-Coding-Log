"""
Platform  : CodeChef
Problem   : Cyclic Shift (IC26CS)
Link      : https://www.codechef.com/ICPCOL26POST/problems/IC26CS
Date      : 2026-10-06
Difficulty: Medium
Topics    : Array, Implementation 

Approach  : Treat the array as circular and take the absolute difference
            between every pair of adjacent elements (last wraps to first).
            Track the two largest differences in a single pass, counting
            duplicates separately, and output the second largest.
Time      : O(N) per test case
Space     : O(N) for the input list, O(1) extra
"""


# -------------------------------------------- Solution ----------------------------------------------------


import sys

def solve_case(arr):
    m = len(arr)
    hi = -1
    lo = -1
    prev = arr[-1]
    for cur in arr:
        g = cur - prev
        if g < 0:
            g = -g
        if g > hi:
            lo = hi
            hi = g
        elif g > lo:
            lo = g
        prev = cur
    return lo

def main():
    buf = sys.stdin.buffer.read().split()
    ptr = 1
    out = []
    for _ in range(int(buf[0])):
        n = int(buf[ptr])
        ptr += 1
        seg = list(map(int, buf[ptr:ptr + n]))
        ptr += n
        out.append(str(solve_case(seg)))
    sys.stdout.write("\n".join(out) + "\n")

main()
