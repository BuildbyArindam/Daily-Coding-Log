"""
Problem: Unique Subarrays
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/unique-subarrays/
Date: 2026-08-30
Difficulty: Medium
Topics: Data Structures, Implementation, One-dimensional, Sets

Approach:
Two-pointer sliding window. For each right pointer, shrink left past any
previous occurrence of A[right] within the current window so the window
[left, right] always holds distinct values. Every subarray ending at
`right` that starts within [left, right] is automatically unique, so
instead of enumerating them, use a weighted-sum formula: each subarray
[i, right] contributes (right - i + 1) to the running total. Summing
this over i in [left, right] is done in O(1) per step via a
prefix-sum-based closed form (sum_indices), rather than iterating i.

Time Complexity: O(N) per test case
Space Complexity: O(N) for the `seen` hash map
"""


# ------------------------------- Solution -----------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = int(input_data[idx])
        idx += 1
        A = [int(x) for x in input_data[idx : idx + N]]
        idx += N
        total_weight = 0
        current_sum = 0
        left = 0
        seen = {}
        for right in range(N):
            val = A[right]
            if val in seen and seen[val] >= left:
                left = seen[val] + 1
            seen[val] = right
        left = 0
        seen = {}
        total_weight = 0
        current_sum = 0
        for right in range(N):
            val = A[right]
            if val in seen and seen[val] >= left:
                left = seen[val] + 1
            seen[val] = right
def fast_solution():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = int(input_data[idx])
        idx += 1
        A = [int(x) for x in input_data[idx : idx + N]]
        idx += N
        left = 0
        seen = {}
        total_weight = 0
        for right in range(N):
            val = A[right]
            if val in seen and seen[val] >= left:
                left = seen[val] + 1
            seen[val] = right
            count = right - left + 1
            sum_indices = (right * (right + 1) // 2) - ((left - 1) * left // 2 if left > 0 else 0)
            sub_weight = (right + 1) * count - sum_indices
            total_weight += sub_weight
        out.append(str(total_weight))
    print('\n'.join(out))

if __name__ == '__main__':
    fast_solution()
