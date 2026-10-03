"""
Problem   : Canopy Frequency Watch
Platform  : Unstop
Link      : https://unstop.com/code/practice/661528
Difficulty: Medium
Topics    : Hashing, Heap (Priority Queue), String, Frequency Counting
Date      : 2026-10-03

Approach:
    Keep a hash map of name -> current count. On every "S" (sighting) update,
    increment the count and push (-count, name) onto a max-heap (via negated
    counts). Old entries are never removed, so they go stale (lazy deletion).
    On a query, pop up to C entries, discard any whose count no longer matches
    the map, and collect the valid ones. Ties break by name since the heap
    orders on (-count, name). Then push the valid entries back so the heap is
    intact for the next query.

Complexity:
    Time : O(log n) per update; O(C log n) per query, plus amortized O(log n)
           per stale entry discarded (each entry is discarded at most once).
    Space: O(n) for the map and heap.
"""


# ---------------------------------- Solution -------------------------------------------------


import sys
import heapq

def main():
    input = sys.stdin.readline
    n, C = map(int, input().split())
    counts = {}
    heap = []
    for _ in range(n):
        parts = input().split()
        if parts[0] == 'S':
            name = parts[1]
            counts[name] = counts.get(name, 0) + 1
            count = counts[name]
            heapq.heappush(heap, (-count, name))
        else:  
            top = []
            while heap and len(top) < C:
                neg_count, name = heapq.heappop(heap)
                count = -neg_count
                if counts.get(name, 0) != count:
                    continue
                top.append((neg_count, name))
            print(' '.join(name for _, name in top))
            for item in top:
                heapq.heappush(heap, item)

if __name__ == "__main__":
    main()
