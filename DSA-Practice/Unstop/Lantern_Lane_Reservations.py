"""
Problem   : Lantern Lane Reservations
Platform  : Unstop 
Link      : https://unstop.com/code/practice/671425
Date      : 2026-11-14
Difficulty: Medium
Topics    : Fenwick Tree (BIT), Prefix Sum, Order Statistic Tree

Approach  :
  - Keep a Fenwick tree over the lane where each vacant spot counts as 1.
    Build it in O(N) by pushing each node's value to its parent.
  - Reserve request for spot `val`:
      1. before = number of vacant spots in [1, val-1] (BIT prefix query).
      2. The target is the (before+1)-th vacant spot, i.e. the first vacant
         spot at or after `val`. If before == total vacant, wrap around to
         the 1st vacant spot.
      3. Find the k-th vacant spot with binary lifting on the BIT (order
         statistic), then point-update it by -1.
  - Cancel request: look up the spot held by that earlier request and
    point-update it by +1 to free it.
  - If no vacant spot exists, record 0.

Complexity: Time  O((N + Q) log N)  (O(N) build, O(log N) per request)
            Space O(N + Q)          (BIT + holder/report arrays)
"""


# ------------------------------------------------ Solution ----------------------------------------------------------------


import sys

def run():
    tokens = sys.stdin.read().split()
    lane_len = int(tokens[0])
    req_cnt = int(tokens[1])
    layout = tokens[2]
    stream = tokens[3:3 + req_cnt]
    bit = [0] * (lane_len + 1)
    for idx in range(1, lane_len + 1):
        if layout[idx - 1] == '.':
            bit[idx] += 1
        nxt = idx + (idx & -idx)
        if nxt <= lane_len:
            bit[nxt] += bit[idx]
    top = 1
    while top * 2 <= lane_len:
        top *= 2
    vacant_total = layout.count('.')
    report = []  
    holder = []  
    for tok in stream:
        val = int(tok)
        if val < 0:
            which = -val - 1
            spot = holder[which]
            if spot:
                holder[which] = 0
                vacant_total += 1
                while spot <= lane_len:
                    bit[spot] += 1
                    spot += spot & -spot
            continue
        if vacant_total == 0:
            report.append(0)
            holder.append(0)
            continue
        before = 0
        j = val - 1
        while j > 0:
            before += bit[j]
            j -= j & -j
        need = 1 if before == vacant_total else before + 1
        cur = 0
        step = top
        while step:
            probe = cur + step
            if probe <= lane_len and bit[probe] < need:
                cur = probe
                need -= bit[probe]
            step >>= 1
        chosen = cur + 1
        j = chosen
        while j <= lane_len:
            bit[j] -= 1
            j += j & -j
        vacant_total -= 1
        report.append(chosen)
        holder.append(chosen)
    sys.stdout.write(" ".join(map(str, report)) + "\n")

if __name__ == "__main__":
    run()
