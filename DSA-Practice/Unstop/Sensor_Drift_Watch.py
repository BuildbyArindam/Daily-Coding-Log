"""
Problem   : Sensor Drift Watch
Platform  : Unstop
Link      : https://unstop.com/code/practice/664312
Difficulty: Medium
Topics    : Fenwick Tree, Hashing, Coordinate Compression, Array
Date      : 2026-10-22

Approach:
  - Coordinate-compress all reading values so they fit a Fenwick Tree (BIT)
    indexed by rank.
  - A hash map stores each sensor's latest reading; the BIT stores how many
    sensors currently hold each value.
  - For each update: remove the sensor's old reading from the BIT. If
    |new - old| > tol, report (sensor, new, count of sensors with a latest
    reading strictly below new). Then insert the new reading.
  - A sensor's first reading is only inserted, never reported.

Complexity:
  Time : O(Q log Q), for sorting/compression plus a BIT update/query per reading
  Space: O(Q), for the compressed values, hash map and BIT
"""


# -------------------------------------------------- Solution -----------------------------------------------------------


import sys
from bisect import bisect_left

class Counter:
    def __init__(self, size):
        self.n = size
        self.t = [0] * (size + 1)

    def bump(self, pos, delta):
        while pos <= self.n:
            self.t[pos] += delta
            pos += pos & (-pos)

    def upto(self, pos):
        acc = 0
        while pos > 0:
            acc += self.t[pos]
            pos -= pos & (-pos)
        return acc

def main():
    raw = sys.stdin.buffer.read().split()
    q, tol = int(raw[0]), int(raw[1])
    ids = raw[2:2 + 2 * q:2]
    vals = list(map(int, raw[3:3 + 2 * q:2]))
    levels = sorted(set(vals))
    rank = lambda v: bisect_left(levels, v) + 1
    tree = Counter(len(levels))
    latest = {}
    out = []
    for k in range(q):
        sid = int(ids[k])
        cur = vals[k]
        prev = latest.get(sid)
        if prev is None:
            tree.bump(rank(cur), 1)
        else:
            tree.bump(rank(prev), -1)
            if abs(cur - prev) > tol:
                out.append("%d %d %d" % (sid, cur, tree.upto(rank(cur) - 1)))
            tree.bump(rank(cur), 1)
        latest[sid] = cur
    sys.stdout.write("\n".join(out) + ("\n" if out else ""))

main()
