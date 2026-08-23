"""
Problem: Not in Range
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/not-in-range-44d19403/
Date Solved: 2026-08-23
Difficulty: Easy
Topics: Arrays, Data Structures, One-dimensional, Partial Sum, Prefix Sum, Segment Trees

Approach:
Use a difference array over the value domain [1, MAX_VAL] to mark how many
input ranges [l, r] cover each point (diff[l] += 1, diff[r+1] -= 1). Sweep
left to right accumulating active_ranges; any point where active_ranges == 0
lies outside every given range, so add it to the answer.

Time Complexity: O(N + MAX_VAL)   -- N range updates + one sweep over MAX_VAL
Space Complexity: O(MAX_VAL)      -- fixed-size difference array
"""


# ------------------------ Solution --------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    MAX_VAL = 1000000
    diff = [0] * (MAX_VAL + 2)
    idx = 1
    for _ in range(n):
        l = int(input_data[idx])
        r = int(input_data[idx + 1])
        idx += 2
        diff[l] += 1
        diff[r + 1] -= 1
    total_sum = 0
    active_ranges = 0
    for i in range(1, MAX_VAL + 1):
        active_ranges += diff[i]
        if active_ranges == 0:
            total_sum += i
    print(total_sum)

if __name__ == "__main__":
    solve()
