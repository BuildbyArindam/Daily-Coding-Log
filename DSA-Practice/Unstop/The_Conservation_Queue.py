"""
Problem   : The Conservation Queue
Platform  : Unstop
Link      : https://unstop.com/code/practice/662451
Difficulty: Medium
Topics    : Heap (Priority Queue), Hashing, Simulation, Lazy Deletion
Date      : 2026-10-11

Approach:
    Keep a max-heap (negated urgency) of arriving artifacts, plus a dict
    mapping artifact_id -> current urgency for those still waiting.
    - ARRIVE  : record in dict and push (-urgency, id) onto the heap.
    - WITHDRAW: delete from dict only (lazy deletion, no heap removal).
    - RESTORE : pop stale heap tops (id missing from dict, or urgency
                mismatch) until a valid entry is found, output its id and
                remove it from dict. If the heap empties, output IDLE.
    Ties on urgency are broken by smaller artifact id via the tuple order.

Complexity:
    Time : O(M log M), each entry is pushed and popped at most once.
    Space: O(M) for the heap and the dict.
"""


# --------------------------------------------- Solution --------------------------------------------------------


import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    M = int(next(iterator))
    pq = []
    waiting_artifacts = {}
    output = []
    for _ in range(M):
        op = next(iterator)
        if op == "ARRIVE":
            artifact_id = int(next(iterator))
            urgency = int(next(iterator))
            waiting_artifacts[artifact_id] = urgency
            heapq.heappush(pq, (-urgency, artifact_id))
        elif op == "WITHDRAW":
            artifact_id = int(next(iterator))
            if artifact_id in waiting_artifacts:
                del waiting_artifacts[artifact_id]
        elif op == "RESTORE":
            while pq:
                neg_urgency, artifact_id = pq[0]
                urgency = -neg_urgency
                if artifact_id in waiting_artifacts and waiting_artifacts[artifact_id] == urgency:
                    break
                heapq.heappop(pq)
            if not pq:
                output.append("IDLE")
            else:
                _, restored_id = heapq.heappop(pq)
                output.append(str(restored_id))
                del waiting_artifacts[restored_id]
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()
