"""
Problem   : Collar Watch at Silverfen Reserve
Platform  : Unstop
Link      : https://unstop.com/code/practice/670818
Difficulty: Medium
Topics    : Heap (Priority Queue), Simulation, Lazy Deletion
Date      : 2026-11-08

Approach:
    Keep a min-heap of (battery, id) pairs plus a battery[] array that holds
    the true current value for each collar. Updates never edit the heap in
    place: a drain pushes a fresh (new_battery, id) entry, and a removal just
    flags the collar in gone[]. On a query, pop from the top and discard any
    stale entry (collar removed, or its heap value no longer matches
    battery[id]). The first valid entry is the answer; reset that collar to
    100 and push it back. If the heap empties, output NONE.
    Fast input via sys.stdin.buffer and one batched output write.

Complexity:
    Time : O((N + E) log (N + E)). Each event adds at most one heap entry,
           and each entry is pushed and popped at most once.
    Space: O(N + E) for the heap and the battery/gone arrays.
"""


# ----------------------------------------------- Solution ------------------------------------------------------------------


import sys
from heapq import heappush as _hp, heappop as _hq, heapify as _hf

def _run():
    _in = sys.stdin.buffer.read().split()
    _p = 0
    _n = int(_in[0])
    _e = int(_in[1])
    _p = 2
    battery = [0] * (_n + 1)
    gone = bytearray(_n + 1)
    pq = []
    for _i in range(1, _n + 1):
        _v = int(_in[_p])
        _p += 1
        battery[_i] = _v
        pq.append((_v, _i))
    _hf(pq)
    answers = []
    for _ in range(_e):
        _cmd = _in[_p]
        _p += 1
        _c = _cmd[0]
        if _c == 68:  
            _id = int(_in[_p])
            _amt = int(_in[_p + 1])
            _p += 2
            _cur = battery[_id]
            _nw = _cur - _amt
            if _nw < 0:
                _nw = 0
            if _nw != _cur:
                battery[_id] = _nw
                _hp(pq, (_nw, _id))
        elif _c == 82:
            _id = int(_in[_p])
            _p += 1
            gone[_id] = 1
        else:  
            _found = 0
            while pq:
                _lv, _who = pq[0]
                if gone[_who] or battery[_who] != _lv:
                    _hq(pq) 
                    continue
                _hq(pq)
                _found = _who
                break
            if _found:
                battery[_found] = 100
                _hp(pq, (100, _found))
                answers.append(str(_found))
            else:
                answers.append("NONE")
    sys.stdout.write("\n".join(answers))
    if answers:
        sys.stdout.write("\n")

_run()
