"""
Problem: Thief and Warehouses
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/thief-and-warehouses-6ebf4e07/
Date: 2026-08-29
Difficulty: Medium
Topics: Arrays, Data Structures, One-dimensional, Stacks

Approach:
    Classic "largest rectangle in histogram" pattern. Maintain a monotonic
    increasing stack of indices. For each bar (plus a sentinel 0-height bar
    at the end), pop indices whose height exceeds the current height,
    computing the max area for each popped bar using its height and the
    width spanned between the new stack top and current index.

Time Complexity:  O(n) — each index is pushed and popped from the stack at most once
Space Complexity: O(n) — for the stack
"""


# ------------------------ Solution --------------------------------


import sys

def max_sacks(arr, n):
    stack = []
    max_area = 0
    for i in range(n + 1):
        current_h = arr[i] if i < n else 0
        while stack and arr[stack[-1]] > current_h:
            h = arr[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        arr = [int(x) for x in input_data[idx : idx + n]]
        idx += n
        print(max_sacks(arr, n))

if __name__ == '__main__':
    main()
