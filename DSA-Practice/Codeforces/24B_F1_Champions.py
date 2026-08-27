"""
Problem   : F1 Champions
Link      : https://codeforces.com/problemset/problem/24/B
Platform  : Codeforces
Difficulty: *1500
Topic     : Implementation

Approach:
    For each of the t seasons, read the finishing order of drivers.
    Track two things per driver:
      1. Total championship points, awarded via the fixed points_table
         to the top 10 finishers of each race.
      2. A count of how many times the driver finished in each position
         (0-indexed, positions 0..49), used for tie-breaking.

    Two ranking systems are computed:
      - System 1 (points-based): winner = most total points, ties broken
        by comparing position-count vectors lexicographically (most 1st
        places, then most 2nd places, etc.)
      - System 2 (wins-based): winner = most 1st-place finishes, ties
        broken by total points, then by position-count vector.

Complexity:
    Let N = total number of driver entries across all seasons (sum of n).
    Time : O(N) to read input and accumulate points/position counts,
           plus O(D * 50) for each max() scan where D = number of
           distinct drivers (D <= N), so overall O(N + D).
    Space: O(D * 50) for the position-count table, O(D) for points.
"""


# ------------------------- Solution ------------------------------


from collections import defaultdict
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    points_table = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
    points = defaultdict(int)
    pos_counts = defaultdict(lambda: [0] * 51)
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        for i in range(n):
            driver = data[idx]
            idx += 1
            if i < 10:
                points[driver] += points_table[i]
            pos_counts[driver][i] += 1
    drivers = list(pos_counts.keys())
    def key_system1(driver):
        return (
            points[driver],
            [pos_counts[driver][i] for i in range(50)],
        )
    def key_system2(driver):
        return (
            pos_counts[driver][0], 
            points[driver], 
            [pos_counts[driver][i] for i in range(1, 50)], 
        )
    champion1 = max(drivers, key=key_system1)
    champion2 = max(drivers, key=key_system2)
    print(champion1)
    print(champion2)

if __name__ == "__main__":
    solve()
