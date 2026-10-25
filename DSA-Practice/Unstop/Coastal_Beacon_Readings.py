"""
Problem   : Coastal Beacon Readings
Platform  : Unstop
Link      : http://unstop.com/code/practice/667802
Difficulty: Medium
Topics    : Heap (Priority Queue), Hashing, Simulation, Lazy Deletion, Custom Comparator
Date      : 2026-10-25

Approach:
    Keep a max-heap of readings, stored as (-temp, station, expiry_time, stamp),
    so the hottest reading is on top and ties go to the lexicographically
    smallest station name. A dict maps each station to the stamp of its latest
    reading. A reading is stale if its stamp is no longer the station's latest
    or if it has expired (expiry <= query time). Stale entries are not removed
    on update. They are discarded lazily, only when they reach the top of the
    heap during a query.

Complexity:
    Time : O(N log N). Each reading is pushed once and popped at most once.
    Space: O(N) for the heap and the station dict.
"""


# ------------------------------------------------ Solution ------------------------------------------------------------------


import sys
import heapq

def run():
    stream = sys.stdin.buffer.read().split(b"\n")
    n_str, w_str = stream[0].split()
    total = int(n_str)
    span = int(w_str)
    pile = [] 
    newest = {}    
    answers = []
    stamp = 0
    for idx in range(1, total + 1):
        parts = stream[idx].split()
        if parts[0] == b"R":
            moment = int(parts[1])
            station = parts[2].decode()
            temp = int(parts[3])
            stamp += 1
            newest[station] = stamp
            heapq.heappush(pile, (-temp, station, moment + span, stamp))
        else:
            moment = int(parts[1])
            while pile:
                neg, station, deadline, sid = pile[0]
                if newest.get(station) != sid or deadline <= moment:
                    heapq.heappop(pile)
                else:
                    break
            if pile:
                answers.append("%s %d" % (pile[0][1], -pile[0][0]))
            else:
                answers.append("NONE")
    sys.stdout.write("\n".join(answers) + "\n")

run()
