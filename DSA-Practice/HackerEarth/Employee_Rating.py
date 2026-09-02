"""
Problem: Employee Rating
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/employee-rating-8cd8dc10/
Difficulty: Easy
Topic: Real World, Algorithms, Linear Search
Date Solved: 2026-09-02

Approach:
Single left-to-right scan tracking a running streak of days where
workload > 6 hours. Reset the streak to 0 whenever a day's hours
drop to <= 6, and keep a running max of the streak length seen so far.

Time Complexity: O(N) — one pass over the workload array
Space Complexity: O(1) — only two counters used
"""


# ------------------------- Solution -----------------------------


def solve (N, workload):
    # Write your code here
    max_days = 0
    current_days = 0
    for hours in workload:
        if hours > 6:
            current_days += 1
            max_days = max(max_days, current_days)
        else:
            current_days = 0
    return max_days
    pass
N = int(input())
workload = list(map(int, input().split()))
out_ = solve(N, workload)
print (out_)
