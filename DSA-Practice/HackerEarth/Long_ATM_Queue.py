"""
Problem: Long ATM Queue
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/long-atm-queue-3/
Difficulty: Easy
Date: 2026-08-30

Approach:
    A new "group" forms in the queue whenever the current person's height
    is strictly less than the previous person's height (i.e., the
    non-decreasing run breaks). Count the number of such breaks + 1
    to get the total number of groups.

Time Complexity: O(N)  — single pass over the heights array
Space Complexity: O(N) — storing the heights list (O(1) extra beyond input)
"""


# ------------------------- Solution -------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    heights = [int(x) for x in input_data[1:N+1]]
    groups = 1
    for i in range(1, N):
        if heights[i] < heights[i - 1]:
            groups += 1
    print(groups)

if __name__ == '__main__':
    solve()
