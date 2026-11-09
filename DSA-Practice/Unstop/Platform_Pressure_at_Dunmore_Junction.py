"""
Problem   : Platform Pressure at Dunmore Junction
Platform  : Unstop
Link      : https://unstop.com/code/practice/670819
Difficulty: Medium
Date      : 2026-11-09
Topics    : Sliding Window, Monotonic Queue, Deque, Frequency Counting, Array

Approach:
    Process the events in order, keeping a sliding window of the last `span`
    minutes (an event is evicted once minute <= current_minute - span).
      - `seen` deque holds (minute, platform) in arrival order so expired
        events can be popped from the front.
      - `live` dict counts events per platform, so len(live) is the number
        of distinct active platforms; a platform is dropped when its count
        reaches 0.
      - `tops` is a monotonic decreasing deque of (minute, lateness), so the
        maximum lateness in the window is always tops[0].
    At each event: score = max_lateness_in_window * distinct_platforms.
    Track the best score and its timestamp (strict '>' keeps the earliest
    timestamp on ties).

Complexity:
    Time  : O(N), since each event is pushed and popped at most once per deque
    Space : O(W), where W is the max number of events inside one window (O(N) worst case)
"""


# --------------------------------------------------- Solution ---------------------------------------------------------------


import sys
from collections import deque

def run():
    raw = sys.stdin.read().split()
    total = int(raw[0])
    span = int(raw[1])
    seen = deque()      
    tops = deque() 
    live = {}   
    best_score = -1
    best_label = ""
    idx = 2
    for _ in range(total):
        stamp = raw[idx]
        plat = int(raw[idx + 1])
        late = int(raw[idx + 2])
        idx += 3
        minute = int(stamp[:2]) * 60 + int(stamp[3:5])
        seen.append((minute, plat))
        live[plat] = live.get(plat, 0) + 1
        while tops and tops[-1][1] <= late:
            tops.pop()
        tops.append((minute, late))
        cutoff = minute - span
        while seen and seen[0][0] <= cutoff:
            old = seen.popleft()[1]
            if live[old] == 1:
                del live[old]
            else:
                live[old] -= 1
        while tops and tops[0][0] <= cutoff:
            tops.popleft()
        score = tops[0][1] * len(live)
        if score > best_score:
            best_score = score
            best_label = stamp
    sys.stdout.write("%d %s\n" % (best_score, best_label))

run()
