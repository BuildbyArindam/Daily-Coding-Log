"""
Problem   : The Ward Priority Desk
Platform  : Unstop (Medium)
Link      : https://unstop.com/code/practice/661268
Date      : 2026-09-28
Topics    : Heap (Priority Queue), Hashing, Lazy Deletion, Simulation

Approach:
    Keep a max-heap (negated priority, arrival order) so the highest priority
    is served first and ties go to the earliest arrival. A hash map `pending`
    holds the current (priority, order, version) of each active request.
    UPDATE pushes a new heap entry with a bumped version instead of editing
    the heap, and CANCEL just removes the id from `pending`. On serve, pop
    until an entry matches `pending` (same id and version); stale entries
    are discarded lazily. If the heap empties, print -1.

Time  : O(Q log Q), since each command pushes at most one entry and each entry is popped at most once
Space : O(Q) for the heap and the map
"""


# ---------------------------------- Solution ---------------------------------------------


import sys
import heapq
input = sys.stdin.readline
q = int(input())
heap = []
pending = {}
arrival_order = 0
output = []
for _ in range(q):
    parts = input().split()
    command = parts[0]
    if command == "ADD":
        req_id = int(parts[1])
        priority = int(parts[2])
        arrival_order += 1
        version = 0
        pending[req_id] = (priority, arrival_order, version)
        heapq.heappush(heap, (-priority, arrival_order, req_id, version))
    elif command == "UPDATE":
        req_id = int(parts[1])
        new_priority = int(parts[2])
        if req_id in pending:
            _, order, version = pending[req_id]
            version += 1
            pending[req_id] = (new_priority, order, version)
            heapq.heappush(heap, (-new_priority, order, req_id, version))
    elif command == "CANCEL":
        req_id = int(parts[1])
        pending.pop(req_id, None)
    else:  
        while heap:
            neg_priority, order, req_id, version = heapq.heappop(heap)
            current = pending.get(req_id)
            if current is None:
                continue
            cur_priority, cur_order, cur_version = current
            if cur_version != version:
                continue
            del pending[req_id]
            output.append(str(req_id))
            break
        else:
            output.append("-1")
sys.stdout.write("\n".join(output))
