"""
Problem   : A Special Sequence
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/special-sequence-1cbd35f9/
Date      : 2026-09-21
Difficulty: Medium
Topics    : Binary Search, Bit Manipulation, Basics of Bit Manipulation, Basic Programming

Approach:
The sequence is built in blocks: block i occupies
    count(i) = i * floor(sqrt(i)) + ceil(i / 2)
consecutive positions, and every position inside that block holds the value i.
Precompute a prefix-sum array of block lengths up to the largest R needed across
all queries. For each query (L, R), binary search (bisect_left) on the prefix
array to find which block index (i.e. value) positions L and R fall into.
The answer is simply (value at R) - (value at L) + 1.

Time Complexity : O(max_R^(2/3) + Q * log(max_R^(2/3)))
    - Building the prefix array up to max_R takes O(max_R^(2/3)) steps,
      since block lengths grow roughly as i^1.5.
    - Each of the Q queries is answered in O(log(number_of_blocks)) via binary search.

Space Complexity: O(max_R^(2/3)) for the prefix array of block boundaries.
"""


# -------------------------------------- Solution ------------------------------------------


import sys
from math import isqrt
from bisect import bisect_left

def main():
    input = sys.stdin.readline
    Q = int(input())
    queries = []
    max_r = 0
    for _ in range(Q):
        L, R = map(int, input().split())
        queries.append((L, R))
        if R > max_r:
            max_r = R
    prefix = [0]
    i = 1
    total = 0
    while total < max_r:
        s = isqrt(i)
        half = (i + 1) // 2
        count = i * s + half
        total += count
        prefix.append(total)
        i += 1
    def value_at_position(p):
        return bisect_left(prefix, p)
    out = []
    for L, R in queries:
        left_value = value_at_position(L)
        right_value = value_at_position(R)
        out.append(str(right_value - left_value + 1))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
