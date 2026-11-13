"""
Problem   : Cold Room Rotation Ledger
Platform  : Unstop
Link      : https://unstop.com/code/practice/671424
Difficulty: Medium
Topics    : Heap (Priority Queue), Hash Table, Greedy, Lazy Deletion
Date      : 2026-11-13

Approach:
    Greedy: every issue request (I) must consume from the batch with the
    earliest expiry first, so a min-heap keyed on (expiry, batch_id) is used.
    A hash map (batch_id -> remaining count) holds the live quantities, and a
    running `stock` total lets us answer "SHORT" in O(1) before touching the heap.
    Removing a batch (R) just zeroes its count in the map (lazy deletion). The
    stale heap entry is discarded later, when it surfaces at the top with
    count == 0. For each issue, we pop/decrement batches until the request is
    met, tracking the last expiry touched and the number of batches used.

Complexity:
    Time : O((N + E) log (N + E)). Each batch is pushed once and popped at
           most once, and every other operation is O(1).
    Space: O(N + E) for the heap and the hash map.
"""


# ----------------------------------------------- Solution --------------------------------------------------------------


import sys
from heapq import heappush as _push, heappop as _pop

def _solve():
    tok = sys.stdin.buffer.read().split()
    n_init = int(tok[0])
    n_evt = int(tok[1])
    pos = 2
    shelf = {}        
    queue = []         
    stock = 0     
    audit = []
    def stash(bid, exp, cnt):
        nonlocal stock
        shelf[bid] = cnt
        _push(queue, (exp, bid))
        stock += cnt
    for _ in range(n_init):
        stash(int(tok[pos]), int(tok[pos + 1]), int(tok[pos + 2]))
        pos += 3
    for _ in range(n_evt):
        kind = tok[pos]
        if kind == b'I':
            need = int(tok[pos + 1])
            pos += 2
            if need > stock:
                audit.append("SHORT")
                continue
            stock -= need
            used = 0
            last_exp = 0
            while need > 0:
                exp, bid = queue[0]
                have = shelf[bid]
                if have == 0:
                    _pop(queue) 
                    continue
                used += 1
                last_exp = exp
                if have <= need:
                    need -= have
                    shelf[bid] = 0
                    _pop(queue)
                else:
                    shelf[bid] = have - need
                    need = 0
            audit.append("%d %d" % (last_exp, used))
        elif kind == b'A':
            stash(int(tok[pos + 1]), int(tok[pos + 2]), int(tok[pos + 3]))
            pos += 4
        else: 
            bid = int(tok[pos + 1])
            pos += 2
            stock -= shelf[bid]
            shelf[bid] = 0
    sys.stdout.write("\n".join(audit) + "\n")

_solve()
