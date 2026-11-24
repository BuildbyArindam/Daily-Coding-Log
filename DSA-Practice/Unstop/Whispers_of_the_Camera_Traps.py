"""
Problem   : Whispers of the Camera Traps
Platform  : Unstop
Link      : https://unstop.com/code/practice/674167
Difficulty: Medium
Topics    : Sliding Window, Queue, Hashing, Heap (Priority Queue), Greedy
Date      : 2026-11-24

Approach
--------
Maintain a sliding window of sightings in two parallel deques (timestamps, species).
- On 'S': append the sighting and increment that species' count in a hash map,
  pushing (-count, species) onto a max-heap (via negated count).
- On 'Q': evict sightings with time <= query_time - span from the left of the
  deque, decrementing counts. Then lazily discard stale heap tops, i.e. entries
  whose stored count no longer matches the live count in the hash map. The
  surviving top is the most frequent species (ties go to the smallest species id),
  or "QUIET" if the window is empty.

Complexity
----------
Time : O(N log N). Each event adds at most one heap entry, and each sighting is
       pushed and popped from the deque at most once. Stale heap entries are
       popped at most once each.
Space: O(N) for the deques, hash map and heap.
"""


# ------------------------------------------------------ Solution ------------------------------------------------------------------


import sys
from heapq import heappush as hp_add, heappop as hp_remove
from collections import deque as Dq

def run():
    raw = sys.stdin.buffer.read().split()
    total_events = int(raw[0])
    span = int(raw[1])
    cursor = 2
    live_times = Dq()
    live_species = Dq()
    tally = {}
    board = []
    replies = []
    def bump(sp, delta):
        newval = tally.get(sp, 0) + delta
        tally[sp] = newval
        if newval > 0:
            hp_add(board, (-newval, sp))
    for _ in range(total_events):
        kind = raw[cursor]
        if kind == b'S':
            moment = int(raw[cursor + 1])
            sp = int(raw[cursor + 2])
            cursor += 3
            live_times.append(moment)
            live_species.append(sp)
            bump(sp, 1)
        else:
            moment = int(raw[cursor + 1])
            cursor += 2
            limit = moment - span
            while live_times and live_times[0] <= limit:
                live_times.popleft()
                bump(live_species.popleft(), -1)
            while board and tally.get(board[0][1], 0) != -board[0][0]:
                hp_remove(board)
            if board:
                top = board[0]
                replies.append("%d %d" % (top[1], -top[0]))
            else:
                replies.append("QUIET")
    sys.stdout.write("\n".join(replies))
    if replies:
        sys.stdout.write("\n")

run()
