"""
Problem: Course Schedule
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/course-schedule_985288?kunjiRedirection=true
Difficulty: Easy
Topics: Graph, Topological Sort
Date Solved: 2026-09-11

Approach:
Model courses and prerequisites as a directed graph (prerequisite -> course).
Use Kahn's Algorithm (BFS-based topological sort): compute in-degree of each
node, push all 0-in-degree nodes into a queue, and repeatedly pop, count, and
decrement in-degrees of neighbors, pushing any that hit 0. If all n courses
get processed (count == n), no cycle exists, so the schedule is completable.
Otherwise a cycle exists and it's impossible.

Time Complexity: O(V + E) -> O(n + len(prerequisites))
Space Complexity: O(V + E) -> adjacency list + indegree array + queue
"""


# -------------------------- Solution -------------------------------


from os import *
from sys import *
from collections import *
from math import *

def canFinish(prerequisites, n, m):
    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for course, prerequisite in prerequisites:
        adj[prerequisite].append(course)
        indegree[course] += 1
    q = deque()
    for course in range(1, n + 1):
        if indegree[course] == 0:
            q.append(course)
    count = 0
    while q:
        course = q.popleft()
        count += 1
        for next_course in adj[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                q.append(next_course)
    if count == n:
        return "Yes"
    else:
        return "No"
