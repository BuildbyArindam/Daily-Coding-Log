"""
Problem   : Benny and Segments
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/benny-and-segments-marcheasy/
Date      : 2026-10-19
Difficulty: Medium
Topics    : Sorting, Two pointer

Approach  : Sort the roads by left endpoint. Try each distinct left endpoint
            as the start of a segment [start, start + L]. Sweep the sorted
            roads, skipping those that begin before `start` or end beyond
            `start + L`, and extend the covered range `current` while roads
            stay contiguous (xl <= current). If `current` reaches
            `start + L` exactly, the answer is "Yes". Stop at the first gap.

Complexity: Time  O(N log N) for sorting + O(N^2) worst case for the
                  start/sweep loops (O(N) per candidate start).
            Space O(N)
"""


# ---------------------------------------------- Solution ------------------------------------------------------------


import sys
data = list(map(int, sys.stdin.buffer.read().split()))
idx = 0
T = data[idx]
idx += 1
for _ in range(T):
    N, L = data[idx], data[idx + 1]
    idx += 2
    roads = []
    for i in range(N):
        xl, xr = data[idx], data[idx + 1]
        idx += 2
        roads.append((xl, xr))
    roads.sort()
    possible = False
    starts = sorted(set(xl for xl, xr in roads))
    for start in starts:
        target = start + L
        current = start
        for xl, xr in roads:
            if xl < start:
                continue
            if xl > current:
                break
            if xr <= target:
                current = max(current, xr)
            if current == target:
                possible = True
                break
        if possible:
            break
    print("Yes" if possible else "No")
