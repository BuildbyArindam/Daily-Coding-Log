"""
Problem   : Missing Soldiers
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/missing-soldiers-december-easy-easy/
Date      : 2026-10-30
Difficulty: Easy
Topics    : Sorting, Intervals

Approach  : Convert each record into an inclusive interval [left, left + length].
            Sort the intervals by start, then sweep once while tracking the
            rightmost point already counted (covered_upto). For each interval,
            skip it if it is fully covered; otherwise count only the part
            beyond covered_upto and extend covered_upto. This gives the size
            of the union of the intervals without double counting overlaps.

Time      : O(N log N), dominated by sorting; the sweep is O(N)
Space     : O(N) for the stored intervals
"""


# -------------------------------------------- Solution -----------------------------------------------------------


import sys

def solve():
    tokens = sys.stdin.buffer.read().split()
    count = int(tokens[0])
    spans = []
    for k in range(count):
        base = 1 + 3 * k
        left = int(tokens[base])
        length = int(tokens[base + 2])
        spans.append((left, left + length))
    spans.sort()
    blocked = 0
    covered_upto = 0  
    for left, right in spans:
        if right <= covered_upto:
            continue
        begin = left if left > covered_upto else covered_upto + 1
        blocked += right - begin + 1
        covered_upto = right
    print(blocked)

solve()
