"""
Problem   : Cars at Maximum Speed (CATMS)
Link      : https://www.codechef.com/problems/CATMS
Date      : 2026-08-18
Difficulty: Easy / Cakewalk
Topics    : Arrays, Greedy, Prefix Minimum

Approach:
Cars travel down a single-lane straight segment and cannot overtake.
A car can only move at its max speed if it's strictly slower than every
car ahead of it (otherwise it must slow down to avoid a collision).
This reduces to counting "new minimums" as we scan left to right:
track the lowest speed seen so far; each time a car's speed is
strictly less than that running minimum, it can run free at max
speed, so we count it and update the minimum.

Time Complexity : O(N)  -- single pass over the speed list
Space Complexity: O(1)  -- only a running minimum and counter are stored
"""


# ------------------------- Solution ----------------------------


import sys

def count_free_flowing_cars(speeds):
    if not speeds:
        return 0
    lowest_seen = speeds[0]
    free_count = 1
    for idx in range(1, len(speeds)):
        current = speeds[idx]
        if current < lowest_seen:
            free_count += 1
            lowest_seen = current
    return free_count

def main():
    data = sys.stdin.read().split()
    total_cars = int(data[0])
    speed_list = list(map(int, data[1:1 + total_cars]))
    result = count_free_flowing_cars(speed_list)
    print(result)

if __name__ == "__main__":
    main()
