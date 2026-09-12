"""
Problem: Speed
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/speed-7/
Date: 2026-09-12
Difficulty: Easy
Topic: Arrays, Implementation

Approach:
    Track the minimum speed seen so far while scanning left to right.
    A car can only overtake cars slower than the ones ahead of it that
    are already "locked in" as the current minimum, so count a car
    whenever its speed is <= the running minimum (i.e., it becomes
    the new slowest-so-far, meaning it can't be overtaken by anyone
    behind it either). The final count is the number of cars that
    never get overtaken.

Time Complexity:  O(N) per test case
Space Complexity: O(N) for storing speeds, O(1) extra
"""


# --------------------------- Solution --------------------------------------


T = int(input())
for _ in range(T):
    N = int(input())
    speeds = list(map(int, input().split()))
    count = 0
    min_speed = float('inf')
    for speed in speeds:
        if speed <= min_speed:
            count += 1
            min_speed = speed
    print(count)
