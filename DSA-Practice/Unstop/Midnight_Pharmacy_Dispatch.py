"""
Problem   : Midnight Pharmacy Dispatch
Platform  : Unstop
Link      : https://unstop.com/code/practice/673666
Date      : 2026-11-22
Difficulty: Medium
Topics    : Heap (Priority Queue), Hashing, Simulation

Approach:
    Keep one max-heap per ward (urgency stored negated, rid as tiebreaker)
    plus a hash map `live_level` of each request's current urgency.
    NEW pushes a request, CHANGE pushes a fresh entry with the new urgency,
    and cancel just removes the request from `live_level`.
    Nothing is deleted from a heap directly (lazy deletion): on SERVE, pop
    entries until one matches `live_level`, which skips stale or cancelled
    ones. A served request is removed from `live_level`, so any duplicate
    entries for it are discarded later.

Complexity:
    Time : O(N log N), since each operation pushes at most one entry and
           every entry is popped at most once.
    Space: O(N) for the heaps and hash maps.
"""


# ----------------------------------------- Solution --------------------------------------------------------


import sys
from heapq import heappush as hp_push, heappop as hp_pop

def night_shift():
    tokens = sys.stdin.buffer.read().split()
    total = int(tokens[0])
    pos = 1
    live_level = {}    
    home_ward = {}     
    ward_heaps = {}   
    log = []
    for _ in range(total):
        kind = tokens[pos]
        if kind == b'SERVE':
            w = int(tokens[pos + 1])
            pos += 2
            h = ward_heaps.get(w)
            answer = "NONE"
            while h:
                neg_u, rid = h[0]
                hp_pop(h)
                if live_level.get(rid) == -neg_u:
                    del live_level[rid]
                    answer = "%d %d" % (rid, -neg_u)
                    break
            log.append(answer)
        elif kind == b'NEW':
            rid = int(tokens[pos + 1])
            w = int(tokens[pos + 2])
            u = int(tokens[pos + 3])
            pos += 4
            home_ward[rid] = w
            live_level[rid] = u
            if w not in ward_heaps:
                ward_heaps[w] = []
            hp_push(ward_heaps[w], (-u, rid))
        elif kind == b'CHANGE':
            rid = int(tokens[pos + 1])
            u = int(tokens[pos + 2])
            pos += 3
            live_level[rid] = u
            hp_push(ward_heaps[home_ward[rid]], (-u, rid))
        else: 
            rid = int(tokens[pos + 1])
            pos += 2
            live_level.pop(rid, None)

    sys.stdout.write("\n".join(log) + ("\n" if log else ""))

night_shift()
