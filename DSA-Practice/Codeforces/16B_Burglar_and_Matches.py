"""
Problem: Burglar and Matches
Link: https://codeforces.com/problemset/problem/16/B
Platform: Codeforces
Difficulty: *900
Topics: Greedy, Implementation, Sortings
Date Solved: 2026-08-22

Approach:
    Each match container gives (a_i boxes, b_i matches/box). The burglar can
    carry at most n boxes total, and wants max total matches. Since containers
    are interchangeable at the box level, always take boxes from the
    container with the highest matches-per-box first (greedy exchange
    argument: swapping a lower-yield box for a higher-yield one from an
    unfilled higher container never decreases the total).
    Sort containers by b_i descending, then greedily fill the n-box capacity
    starting from the richest container.

Time Complexity:  O(m log m)  — dominated by sorting m containers
Space Complexity: O(m)        — storing the container list
"""


# ------------------------ Solution -----------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    containers = []
    idx = 2
    for _ in range(m):
        a_i = int(data[idx])
        b_i = int(data[idx + 1])
        containers.append((a_i, b_i))
        idx += 2
    containers.sort(key=lambda x: x[1], reverse=True)
    total_matches = 0
    remaining_capacity = n
    for boxes, matches_per_box in containers:
        if remaining_capacity == 0:
            break
        take = min(remaining_capacity, boxes)
        total_matches += take * matches_per_box
        remaining_capacity -= take
    print(total_matches)

if __name__ == "__main__":
    solve()
