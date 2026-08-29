"""
Problem: Pepper and Contiguous Even Subarray
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/pepper-and-contiguous-even-subarray-9f3adf65/
Date: 2026-08-29
Difficulty: Easy
Topics: Arrays, Basic Programming, Data Structures, One-dimensional

Approach:
Single pass, tracking the length of the current run of consecutive
even numbers. On an odd number, reset the running length to 0.
Track the max run length seen so far. If no even element exists,
output -1.

Time Complexity:  O(n) per test case
Space Complexity: O(n) for storing the array (O(1) extra beyond input)
"""


# ---------------------------- Solution ----------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = [int(x) for x in data[idx : idx + n]]
        idx += n
        max_len = 0
        current_len = 0
        for num in arr:
            if num % 2 == 0:
                current_len += 1
                if current_len > max_len:
                    max_len = current_len
            else:
                current_len = 0
        if max_len > 0:
            print(max_len)
        else:
            print(-1)

if __name__ == '__main__':
    solve()
