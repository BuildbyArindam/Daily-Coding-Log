"""
Problem   : Ticket Queue
Platform  : CodeChef
Link      : https://www.codechef.com/DSAMONDAY020/problems/TCTQU
Date      : 2026-09-14
Difficulty: Medium
Topics    : Simulation, Round-Robin Scheduling, Math

Approach:
Single ticket counter serves everyone in round-robin, 1 time unit per person
per round. For the target person needing `needed` units:
  - Each person BEFORE the target in queue overlaps with the target for
    min(their_time, needed) ticks (they either finish early, contributing
    their full time, or they're still going when target finishes).
  - Each person AFTER the target overlaps for min(their_time, needed - 1)
    ticks, since the target is always served one tick ahead of them within
    the same round.
  - Total finish time = needed + sum(overlap_before) + sum(overlap_after).

Time Complexity : O(n)  -- single pass to sum overlaps
Space Complexity: O(1) extra (O(n) for storing input times)
"""


# ----------------------------- Solution --------------------------------------


import sys

def compute_finish_time(service_times, target_idx):
    needed = service_times[target_idx]
    elapsed_before_target = 0
    for pos in range(target_idx):
        elapsed_before_target += min(service_times[pos], needed)
    elapsed_after_target = 0
    for pos in range(target_idx + 1, len(service_times)):
        elapsed_after_target += min(service_times[pos], needed - 1)
    return needed + elapsed_before_target + elapsed_after_target

def main():
    data = sys.stdin.read().split()
    cursor = 0
    total_people = int(data[cursor]); cursor += 1
    target_index = int(data[cursor]); cursor += 1
    times = [int(data[cursor + i]) for i in range(total_people)]
    cursor += total_people
    result = compute_finish_time(times, target_index)
    print(result)

if __name__ == "__main__":
    main()
