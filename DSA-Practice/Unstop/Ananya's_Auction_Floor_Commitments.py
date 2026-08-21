"""
Problem   : Weighted Job Scheduling (mislabeled as "LFUCache" — verify problem source)
Link      : https://unstop.com/code/practice/656547
Platform  : Unstop
Contest   : Ananya's Auction Floor Commitments
Date      : 2026-08-21
Difficulty: Medium

Approach:
    Sort jobs by end time. For each job i, use binary search (bisect_right)
    to find the latest job j whose end time <= start time of job i (no overlap).
    DP recurrence: dp[i] = max(dp[i-1], dp[j] + profit[i])
    dp[i-1] -> skip current job, dp[j] + profit -> take current job.

Time complexity : O(N log N)  -- sorting + binary search per job
Space complexity: O(N)        -- dp array + end_times list
"""


# -------------------------- Solution -------------------------------


import sys
from bisect import bisect_right
input = sys.stdin.readline
n = int(input())
jobs = []
for _ in range(n):
    start, end, profit = map(int, input().split())
    jobs.append((start, end, profit))
jobs.sort(key=lambda x: x[1])
dp = [0] * (n + 1)
end_times = [job[1] for job in jobs]
for i in range(1, n + 1):
    start, end, profit = jobs[i - 1]
    j = bisect_right(end_times, start, 0, i - 1)
    dp[i] = max(dp[i - 1], dp[j] + profit)
print(dp[n])
