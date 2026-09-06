"""
Problem: Roy's Life Cycle
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/roys-life-cycle/
Difficulty: Easy
Topics: Approved, Data Structures, Implementation, Open
Date Solved: 2026-09-06

Approach:
For each day's string, track the longest run of consecutive 'C's (coding
streak) within that day, and also maintain a running streak across days
that only resets when a non-'C' character is seen. Track the max of both
as we go.

Time Complexity: O(N * L) — N days, L = length of each day's string
Space Complexity: O(1) extra (excluding input storage)
"""


# ------------------------ Solution ------------------------------------


name = input()
n = int(name)
max_day_streak = 0   
max_total_streak = 0
current_streak = 0
for _ in range(n):
    s = input().strip()
    day_streak = 0
    for ch in s:
        if ch == 'C':
            current_streak += 1
            day_streak += 1
            max_total_streak = max(max_total_streak, current_streak)
            max_day_streak = max(max_day_streak, day_streak)
        else:
            current_streak = 0
            day_streak = 0
print(max_day_streak, max_total_streak)
