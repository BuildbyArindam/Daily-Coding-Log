"""
Problem   : Alex and Priority Requests (Anil and Stocks)
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/anil-and-stocks-628d668e/
Date      : 2026-08-21
Difficulty: Medium
Topics    : Heaps, HashMap, Lazy Deletion

Approach:
Maintain a hashmap (t -> price) as the source of truth, plus three heaps
(min-heap on price, max-heap on -price, max-heap on -time) that are only
lazily cleaned. On query type 3/4, pop stale entries off the top of each
heap (entries whose id is missing from the map or whose stored price no
longer matches) until the top entry is valid, then read it.
- Type 1: insert/update (t, p)      -> push onto all three heaps + map
- Type 2: delete t                  -> remove from map only (heaps cleaned lazily)
- Type 3: min & max price           -> lazy-clean min_heap and max_heap, read tops
- Type 4: most recently added price -> lazy-clean time_heap, read top

Complexity:
Time  : O(q log q) overall — each element is pushed O(1) times and popped
        at most once per heap across the whole run, so lazy cleanup is
        amortized O(log q) per operation.
Space : O(q) for the map and the three heaps.
"""


# --------------------------- Solution --------------------------------


import sys
import heapq
input = sys.stdin.readline
q = int(input())
data = {}
min_heap = []
max_heap = []
time_heap = []
ans = []
for _ in range(q):
    query = list(map(int, input().split()))
    typ = query[0]
    if typ == 1:
        t = query[1]
        p = query[2]
        data[t] = p
        heapq.heappush(min_heap, (p, t))
        heapq.heappush(max_heap, (-p, t))
        heapq.heappush(time_heap, (-t, p))
    elif typ == 2:
        t = query[1]
        del data[t]
    elif typ == 3:
        while min_heap:
            p, t = min_heap[0]
            if t in data and data[t] == p:
                break
            heapq.heappop(min_heap)
        min_value = min_heap[0][0]
        while max_heap:
            neg_p, t = max_heap[0]
            p = -neg_p
            if t in data and data[t] == p:
                break
            heapq.heappop(max_heap)
        max_value = -max_heap[0][0]
        ans.append(f"{min_value} {max_value}")
    elif typ == 4:
        while time_heap:
            neg_t, p = time_heap[0]
            t = -neg_t
            if t in data and data[t] == p:
                break
            heapq.heappop(time_heap)
        ans.append(str(time_heap[0][1]))
sys.stdout.write("\n".join(ans))
