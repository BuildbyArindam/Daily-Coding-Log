"""
Problem   : Minimum Time to Finish Project
Platform  : GeeksforGeeks (Medium)
Link      : https://www.geeksforgeeks.org/problems/project-manager--141631/1
Date      : 2026-10-01
Topics    : Graph, Topological Sort, DP on DAG

Approach  : Model tasks as a DAG (edge u -> v means u must finish before v).
            Run Kahn's algorithm (BFS topological sort) and keep
            earliest[v] = max(earliest[v], earliest[u] + duration[v]).
            The answer is the largest earliest[] value, i.e. the longest
            (critical) path. If not all nodes get processed, there is a
            cycle, so the project can't finish and we return -1.

Time      : O(V + E)
Space     : O(V + E)
"""


---------------------------------------- Solution --------------------------------------


class Solution:
    def minTime(self, duration, dependencies):
        # code here
        n = len(duration)
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in dependencies:
            graph[u].append(v)
            indegree[v] += 1
        earliest = duration[:]
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        processed = 0
        answer = 0
        for u in queue:
            processed += 1
            answer = max(answer, earliest[u])
            for v in graph[u]:
                earliest[v] = max(
                    earliest[v],
                    earliest[u] + duration[v]
                )
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        if processed != n:
            return -1
        return answer
