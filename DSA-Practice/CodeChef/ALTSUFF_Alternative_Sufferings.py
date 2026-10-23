"""
Problem   : Alternative Sufferings (ALTSUFF)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ALTSUFF
Difficulty: 2011
Date      : 2026-10-23
Topics    : Simulation, Bitmasks, Cycle Detection

Approach:
  Store the W-cell binary string as a single Python integer. One step is:
  a cell becomes 1 only if it was 0 and has at least one 1 neighbour; every
  existing 1 becomes 0. In bit operations:
      neighbours = (x >> 1) | (x << 1)
      next       = neighbours & ~x & mask
  Simulate step by step. Once state[t] == state[t-2], the sequence has
  settled into a period-2 cycle, so the answer at time S is decided by the
  parity of the remaining steps (S - t).

Complexity:
  Time : O(min(S, k) * W / 64) per test, where k is the number of steps
         before the period-2 cycle appears (I'm assuming k is O(W), since
         fronts move one cell per step). Each step is a few big-int ops.
  Space: O(W) for the bitmask and the output string.
"""


# -------------------------------------- Solution ------------------------------------------------------------


import sys

def evolve(width, secs, bits):
    lim = (1 << width) - 1
    now = int(bits, 2)
    prev = None
    t = 0
    while t < secs:
        ngb = (now >> 1) | (now << 1)
        fut = ((ngb | now) ^ now) & lim
        t += 1
        if prev is not None and fut == prev:
            return prev if (secs - t) % 2 == 0 else now
        prev, now = now, fut
    return now

def run():
    data = sys.stdin.read().split()
    cases = int(data[0])
    res = []
    pos = 1
    while cases:
        cases -= 1
        w, s, b = int(data[pos]), int(data[pos + 1]), data[pos + 2]
        pos += 3
        res.append(format(evolve(w, s, b), "0%db" % w))
    sys.stdout.write("\n".join(res) + "\n")

if __name__ == "__main__":
    run()
