"""
Problem: Parade (CF 35E)
Link: https://codeforces.com/problemset/problem/35/E
Date: 2026-09-03
Difficulty: *2100
Topics: Data Structures (Heap/Priority Queue), Sorting, Sweep Line

Approach:
    Classic "skyline problem" solved via a coordinate sweep line + max-heap.
    Sort buildings by left edge. Sweep through candidate x-coordinates
    (either the next building's start, or the current tallest building's
    end). At each x, pop buildings from the heap that have ended, push
    buildings that start exactly at x, then read the new max height from
    the heap top. Record a vertex whenever the skyline height changes.

Time Complexity:  O(n log n)  -- each building pushed/popped from heap once
Space Complexity: O(n)        -- heap + output vertex list
"""


# ---------------------------- Solution ------------------------------------


import sys
import heapq
import os

def solve(inp, out):
    n = int(inp.readline())
    buildings = []
    for _ in range(n):
        h, l, r = map(int, inp.readline().split())
        buildings.append((l, r, h))
    buildings.sort()
    heap = []
    i = 0
    cur_h = 0
    ans = []
    while i < n or heap:
        if i < n:
            next_l = buildings[i][0]
        else:
            next_l = 10**30
        if heap:
            next_r = heap[0][1]
        else:
            next_r = 10**30
        x = min(next_l, next_r)
        while heap and heap[0][1] <= x:
            heapq.heappop(heap)
        while i < n and buildings[i][0] == x:
            l, r, h = buildings[i]
            heapq.heappush(heap, (-h, r))
            i += 1
        if heap:
            new_h = -heap[0][0]
        else:
            new_h = 0
        if not ans:
            ans.append((x, 0))
            ans.append((x, new_h))
        elif new_h != cur_h:
            ans.append((x, cur_h))
            ans.append((x, new_h))
        cur_h = new_h
    out.write(str(len(ans)) + "\n")
    for x, h in ans:
        out.write(f"{x} {h}\n")

def main():
    if os.path.exists("input.txt"):
        with open("input.txt", "r") as inp:
            with open("output.txt", "w") as out:
                solve(inp, out)
    else:
        solve(sys.stdin, sys.stdout)

if __name__ == "__main__":
    main()
