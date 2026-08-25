"""
Problem   : Roy's Life Cycle
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/roys-life-cycle-44/
Difficulty: Easy
Topics    : Approved, Data Structures, Implementation
Date      : 2026-08-25

Approach:
For each day's activity string, track the longest run of consecutive 'C'
characters (max_daily_streak). Also concatenate all days in order and track
the longest run of consecutive 'C's across the whole sequence
(max_overall_streak), since a streak can span the boundary between two days.
Single pass over each string using a running counter reset on any non-'C'.

Time complexity : O(N * L)  where N = number of days, L = avg length of each day's string
                  (equivalently O(total characters), since each char is visited twice)
Space complexity: O(total characters) for storing/joining the day strings
"""


# ------------------------- Solution ----------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    days = input_data[1:n+1]
    max_daily_streak = 0
    for day in days:
        current_streak = 0
        for char in day:
            if char == 'C':
                current_streak += 1
                max_daily_streak = max(max_daily_streak, current_streak)
            else:
                current_streak = 0
    all_days = "".join(days)
    max_overall_streak = 0
    current_streak = 0
    for char in all_days:
        if char == 'C':
            current_streak += 1
            max_overall_streak = max(max_overall_streak, current_streak)
        else:
            current_streak = 0
    print(f"{max_daily_streak} {max_overall_streak}")

if __name__ == '__main__':
    solve()
