"""
Problem   : Dose Ledger for Ward Requests
Platform  : Unstop
Link      : https://unstop.com/code/practice/671760
Difficulty: Medium
Topics    : Heap (Priority Queue), Hashing, Simulation, Greedy, Lazy Deletion
Date      : 2026-11-16

Approach:
    Keep a min-heap of (expiry, batch_id) so the earliest-expiring batch is
    always issued first (greedy / FEFO). A hash map {batch_id: qty} holds the
    live quantity of each batch.
      - Receive: store qty in the map and push (expiry, id) onto the heap.
      - Recall : set qty to 0 in the map. The heap entry is removed lazily
                 later, so there is no O(n) heap deletion.
      - Issue  : first pop all batches with expiry < today and add their
                 remaining qty to the wasted total. Then drain from the heap
                 top until the request is met or the heap is empty.
                 Recalled batches (qty 0) are dropped for free during this.
      - Output : per-issue "issued shortfall" lines, then "wasted <total>".

Complexity:
    Time : O(Q log Q), since each batch is pushed and popped at most once.
    Space: O(Q) for the heap and the map.
"""


# --------------------------------------- Solution ---------------------------------------------------------------


import sys
from heapq import heappush as push_, heappop as pop_

class ColdStore:
    def __init__(self):
        self.stock = {}    
        self.order = []     
        self.lost = 0

    def receive(self, bid, expiry, qty):
        self.stock[bid] = qty
        push_(self.order, (expiry, bid))

    def recall(self, bid):
        if bid in self.stock:
            self.stock[bid] = 0

    def discard_expired(self, today):
        o, s = self.order, self.stock
        while o and o[0][0] < today:
            _, bid = pop_(o)
            self.lost += s.pop(bid, 0)

    def issue(self, today, want):
        self.discard_expired(today)
        o, s = self.order, self.stock
        left = want
        while left and o:
            bid = o[0][1]
            have = s[bid]
            if have <= left:
                left -= have
                s.pop(bid)
                pop_(o)
            else:
                s[bid] = have - left
                left = 0
        return want - left, left

def main():
    data = sys.stdin.read().split()
    q = int(data[0])
    pos = 1
    store = ColdStore()
    out = []
    for _ in range(q):
        t = data[pos]
        if t == 'R':
            store.receive(int(data[pos + 1]), int(data[pos + 2]), int(data[pos + 3]))
            pos += 4
        elif t == 'I':
            a, b = store.issue(int(data[pos + 1]), int(data[pos + 2]))
            out.append("%d %d" % (a, b))
            pos += 3
        else:
            store.recall(int(data[pos + 1]))
            pos += 2
    out.append("wasted %d" % store.lost)
    print("\n".join(out))

main()
