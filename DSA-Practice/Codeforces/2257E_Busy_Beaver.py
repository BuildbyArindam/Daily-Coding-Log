"""
Problem   : E - Busy Beaver
Platform  : Codeforces
Link      : https://codeforces.com/contest/2257/problem/E
Date      : 2026-08-18
Difficulty: ~2400-2600 (est.) - Div.2 E, unrated as of solve date
Tags      : brute force, divide and conquer, dp, greedy, implementation, sortings

Approach:
  For each building, greedily merge consecutive floors into the shortest
  prefix segments whose cumulative profit is non-negative, tracking each
  segment's "entry threshold" (min running capital needed to clear it
  without going negative mid-segment). This turns each building into a
  short list of (threshold, net_gain, floors_cleared) jumps.

  Push each building's first jump into a min-heap keyed by threshold.
  Repeatedly pop the cheapest-to-afford jump across all buildings, apply
  it (grow wallet, advance progress), and push that building's next jump
  if one exists. Stop once nothing affordable remains in the heap -- this
  maximizes total capital in O((n + total_floors) log n).

  With capital maximized, do one final greedy pass per building (from its
  last reached segment boundary) to see how many additional floors it
  could build with the final wallet, and report the tallest building.

Complexity:
  Time : O(M log n), where M = sum of floors across all buildings
         (segment construction O(M), heap ops O(M log n))
  Space: O(M) for storing costs/profits/jump lists
"""


# ---------------------------- Solution --------------------------------


import sys
import heapq

def solve():
    data = sys.stdin.buffer.read().split()
    nums = list(map(int, data))
    pos = 0
    t = nums[pos]; pos += 1
    out = []
    heappush = heapq.heappush
    heappop = heapq.heappop
    for _ in range(t):
        n = nums[pos]; treasury = nums[pos + 1]; pos += 2
        all_costs = [None] * n
        all_profits = [None] * n
        jump_lists = [None] * n
        heap = []
        for tag in range(n):
            m = nums[pos]; pos += 1
            costs = nums[pos:pos + m]; pos += m
            profits = nums[pos:pos + m]; pos += m
            all_costs[tag] = costs
            all_profits[tag] = profits
            jumps = []
            reset_baseline = 0
            running_delta = 0
            segment_peak = None
            record_high = 0
            j = 0
            while j < m:
                c = costs[j]; p = profits[j]
                req = c - running_delta
                if segment_peak is None or req > segment_peak:
                    segment_peak = req
                running_delta += p - c
                candidate = reset_baseline + running_delta
                if candidate > record_high:
                    record_high = candidate
                    jumps.append((segment_peak, running_delta, j + 1))
                    reset_baseline = record_high
                    running_delta = 0
                    segment_peak = None
                j += 1
            jump_lists[tag] = jumps
            if jumps:
                heappush(heap, (jumps[0][0], tag, 0))
        wallet = treasury
        reached = [0] * n
        while heap:
            need, tag, slot = heap[0]
            if need > wallet:
                break
            heappop(heap)
            lst = jump_lists[tag]
            _need, gain, end = lst[slot]
            wallet += gain
            reached[tag] = end
            nxt = slot + 1
            if nxt < len(lst):
                heappush(heap, (lst[nxt][0], tag, nxt))
        best_h = -1
        best_i = -1
        for tag in range(n):
            costs = all_costs[tag]
            profits = all_profits[tag]
            cash = wallet
            f = reached[tag]
            top = len(costs)
            while f < top and cash >= costs[f]:
                cash += profits[f] - costs[f]
                f += 1
            if f > best_h:
                best_h = f
                best_i = tag + 1
        out.append(f"{best_h} {best_i}")
    sys.stdout.write("\n".join(out) + "\n")

solve()
