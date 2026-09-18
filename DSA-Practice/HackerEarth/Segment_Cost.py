"""
Problem: Segment Cost
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/segment-cost-af31ef0c/
Date Solved: 2026-09-18
Difficulty: Medium
Topics: Binary Search, Sliding Window, Prefix Sum/XOR, Algorithms

Approach:
Find the shortest subarray [l, r] within [x, y] whose "cost" (sum - xor)
is still >= the cost of the full segment [x, y]. Use a sliding window:
expand `right`, then shrink `left` while the window's cost stays >= target,
tracking the smallest valid window (ties broken by smaller left index).

Time Complexity:  O(N) — single pass with two pointers, amortized O(1) per step
Space Complexity: O(1) extra (excluding input storage)
"""


# ------------------------------------ Solution ----------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    total_sum = sum(A[x:y + 1])
    total_xor = 0
    for i in range(x, y + 1):
        total_xor ^= A[i]
    target = total_sum - total_xor
    left = x
    window_sum = 0
    window_xor = 0
    best_l = x
    best_r = y
    best_len = y - x + 1
    for right in range(x, y + 1):
        window_sum += A[right]
        window_xor ^= A[right]
        while left <= right:
            current_cost = window_sum - window_xor
            if current_cost < target:
                break
            current_len = right - left + 1
            if (current_len < best_len or
                    (current_len == best_len and left < best_l)):
                best_len = current_len
                best_l = left
                best_r = right
            window_sum -= A[left]
            window_xor ^= A[left]
            left += 1
    print(best_l + 1, best_r + 1)

if __name__ == "__main__":
    solve()
