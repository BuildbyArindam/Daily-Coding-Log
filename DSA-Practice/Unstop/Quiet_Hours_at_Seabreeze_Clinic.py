"""
Problem   : Quiet Hours at Seabreeze Clinic
Platform  : Unstop
Link      : https://unstop.com/code/practice/672462
Difficulty: Medium
Topics    : Heap (Priority Queue), Hashing, Simulation, Data Structures
Date      : 2026-11-17

Approach:
    Simulate a waiting board that supports arrive, report (raise priority),
    leave, and call (serve the highest priority). Use a max-heap, stored as
    negated values, ordered by (-priority, arrival rank). A dict maps each
    person to their current [priority, rank], which is the source of truth.
    Priority updates and removals are handled by lazy deletion. A report
    pushes a fresh heap entry, and a leave only removes the dict entry.
    On CALL, pop until an entry matches the dict (same priority and rank),
    which skips stale entries. Rank breaks ties by arrival order, and a
    person who re-arrives gets a new rank.

Complexity:
    Time : O(N log N), since each command pushes at most one heap entry and
           each entry is popped at most once.
    Space: O(N) for the heap and the dict.
"""


# ----------------------------------------------- Solution ---------------------------------------------------------------


import sys
from heapq import heappush, heappop

def main():
    raw = sys.stdin.buffer.read().split()
    total = int(raw[0])
    pos = 1
    board = {}
    queue = []
    results = []
    rank = 0
    def next_valid():
        while queue:
            neg, rk, who = heappop(queue)
            info = board.get(who)
            if info is not None and info[0] == -neg and info[1] == rk:
                del board[who]
                return who
        return None
    for _ in range(total):
        cmd = raw[pos]
        pos += 1
        if cmd == b"CALL":
            got = next_valid()
            results.append("NONE" if got is None else str(got))
        elif cmd == b"LEAVE":
            who = int(raw[pos])
            pos += 1
            board.pop(who, None)
        elif cmd == b"REPORT":
            who = int(raw[pos])
            val = int(raw[pos + 1])
            pos += 2
            info = board.get(who)
            if info is not None and val > info[0]:
                info[0] = val
                heappush(queue, (-val, info[1], who))
        else: 
            who = int(raw[pos])
            val = int(raw[pos + 1])
            pos += 2
            board[who] = [val, rank]
            heappush(queue, (-val, rank, who))
            rank += 1
    results.append("Waiting: " + str(len(board)))
    sys.stdout.write("\n".join(results) + "\n")

main()
