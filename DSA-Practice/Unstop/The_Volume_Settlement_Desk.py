"""
Problem   : The Volume Settlement Desk
Platform  : Unstop 
Link      : https://unstop.com/code/practice/664310
Date      : 2026-10-19
Difficulty: Medium
Topics    : Hashing, Heap / Priority Queue, Sorting, Relative Ordering

Approach  :
    Keep a running total per ticker in a hash map. Every BUY updates the
    ticker's total and pushes (-total, ticker_id) onto a max-heap (a min-heap
    with negated totals, so ties go to the smaller ticker_id).
    On a SETTLE, lazily discard stale heap entries whose stored total no
    longer matches the map. The top valid entry is the ticker with the
    highest volume. Output it, then reset its total to 0.

Complexity:
    Time  : O(N log N), since each BUY pushes once and each entry is popped at most once
    Space : O(N), for the hash map and the heap, which holds at most one entry per BUY
"""


# ----------------------------------------------- Solution --------------------------------------------------------------


import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    idx = 1
    totals = {}
    max_heap = []
    result = []
    for _ in range(n):
        event = data[idx]
        idx += 1
        if event == b'BUY':
            ticker_id = int(data[idx])
            units = int(data[idx + 1])
            idx += 2
            totals[ticker_id] = totals.get(ticker_id, 0) + units
            heapq.heappush(
                max_heap,
                (-totals[ticker_id], ticker_id)
            )
        else:  
            while max_heap:
                neg_total, ticker_id = max_heap[0]
                if totals.get(ticker_id, 0) == -neg_total:
                    break
                heapq.heappop(max_heap)
            neg_total, ticker_id = heapq.heappop(max_heap)
            total = -neg_total
            result.append(f"{ticker_id} {total}")
            totals[ticker_id] = 0
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
