"""
Problem   : Shelf Life Ledger
Platform  : Unstop
Link      : https://unstop.com/code/practice/667562
Difficulty: Medium
Date      : 2026-10-23
Topics    : Heap (Priority Queue), Hashing, Simulation, Greedy, Lazy Deletion

Approach:
  Process events in chronological order, simulating the shelf.
  - Min-heap of expiry days gives the earliest-expiring stock first (FIFO by expiry).
  - Dict `stock` maps expiry -> remaining quantity; dict `where` maps batch id -> expiry.
  - Before each event, sweep() pops every batch whose expiry < current day and
    adds its quantity to the expired total.
  - R (receive): record the batch and push its expiry onto the heap.
  - D (demand): greedily take from the earliest-expiring batches until the need
    is met or the shelf is empty; fully drained batches are popped.
  - X (recall): zero out the batch's stock instead of removing it from the heap
    (lazy deletion); the empty entry is discarded later when it reaches the top.
  - A final sweep at audit_day settles remaining expirations.

Complexity:
  Time  : O(N log N), since each batch is pushed and popped at most once
          and each event does O(1) amortized heap work beyond that.
  Space : O(N) for the heap and the two dicts.
"""


# --------------------------------------- Solution -------------------------------------------------------------


import sys
from heapq import heappush, heappop

def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    audit_day = int(tokens[1])
    shelf = [] 
    stock = {}
    where = {}   
    lost = 0
    pulled = 0
    answers = []
    def sweep(limit):
        nonlocal lost
        while shelf and shelf[0] < limit:
            e = heappop(shelf)
            lost += stock.pop(e)
    pos = 2
    for _ in range(n):
        day = int(tokens[pos])
        kind = tokens[pos + 1]
        sweep(day)
        if kind == b'R':
            b = int(tokens[pos + 2])
            e = int(tokens[pos + 3])
            q = int(tokens[pos + 4])
            pos += 5
            where[b] = e
            stock[e] = q
            heappush(shelf, e)
        elif kind == b'D':
            need = int(tokens[pos + 2])
            pos += 3
            given = 0
            while need > 0 and shelf:
                e = shelf[0]
                have = stock[e]
                take = have if have < need else need
                given += take
                need -= take
                if take == have:
                    heappop(shelf)
                    del stock[e]
                else:
                    stock[e] = have - take
            answers.append(given)
        else:
            b = int(tokens[pos + 2])
            pos += 3
            e = where.get(b)
            if e is not None and e in stock and stock[e] > 0:
                pulled += stock[e]
                stock[e] = 0 
    sweep(audit_day)
    out = [str(a) for a in answers]
    out.append("EXPIRED %d RECALLED %d" % (lost, pulled))
    sys.stdout.write("\n".join(out) + "\n")

main()
