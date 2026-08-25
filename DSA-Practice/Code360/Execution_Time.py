"""
Problem: Execution Time
Platform: Code360
Link: https://www.naukri.com/code360/problems/day-26-execution-time_799892?kunjiRedirection=true
Difficulty: Medium
Date: 2026-08-25
Topics: Stack, Simulation

Approach:
Simulate function calls using a stack of function IDs. On a "start" event,
credit any currently-running function (top of stack) with the elapsed time
since the last checkpoint, then push the new function and reset the
checkpoint. On an "end" event, credit the top function up to and including
the current timestamp, pop it, and advance the checkpoint to curr_time + 1
(since the end timestamp is inclusive).

Time Complexity: O(L) — each log processed once
Space Complexity: O(N) — stack + answer array, N = number of functions
"""


# --------------------------- Solution ------------------------------


from os import *
from sys import *
from collections import *
from math import *
from sys import stdin

def exclusiveTime(logs, n, l):
    stack = []
    ans = [0] * n
    prev_time = 0
    for i in range(l):
        func_id = logs[0][i]
        event = logs[1][i]
        curr_time = logs[2][i]
        if event == 1:  
            if stack:
                ans[stack[-1]] += curr_time - prev_time
            stack.append(func_id)
            prev_time = curr_time
        else:  
            ans[stack[-1]] += curr_time - prev_time + 1
            stack.pop()
            prev_time = curr_time + 1
    return ans

t = int(input().strip())

for i in range(t):
    n,l = list(map(int, stdin.readline().strip().split(" ")))
    logs = []
    id = list(map(int, stdin.readline().strip().split(" ")))
    start_end = list(map(int, stdin.readline().strip().split(" ")))
    timestamp = list(map(int, stdin.readline().strip().split(" ")))
    logs.append(id)
    logs.append(start_end)
    logs.append(timestamp)
    ans = exclusiveTime(logs, n, l)
    for ele in ans:
        print(ele, end =" ")
    print()
