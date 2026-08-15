"""
Problem: Hamster Farm
Link: https://codeforces.com/contest/939/problem/B
Platform: Codeforces
Date Solved: 2026-08-15
Topic: Implementation
Rating: 1000

Approach:
For each box type i with capacity cap_i, hamsters that fit in filled boxes
= N - (N % cap_i). Minimizing (N % cap_i) across all K types maximizes the
number of housed hamsters. Track the type with the smallest remainder and
output that type index (1-indexed) along with N // cap_i (number of boxes
used). Any type achieving the minimum remainder is a valid answer.

Time Complexity:  O(K)  - single pass over box capacities
Space Complexity: O(K)  - storing the capacity list (O(1) extra beyond input)
"""


# --------------------------- Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    K = int(input_data[1])
    box_capacities = [int(x) for x in input_data[2 : 2 + K]]
    best_type = 1
    min_remainder = float("inf")
    best_box_count = 0
    for i in range(K):
        cap = box_capacities[i]
        remainder = N % cap
        boxes = N // cap
        if remainder < min_remainder:
            min_remainder = remainder
            best_type = i + 1
            best_box_count = boxes
    print(f"{best_type} {best_box_count}")

if __name__ == "__main__":
    solve()
