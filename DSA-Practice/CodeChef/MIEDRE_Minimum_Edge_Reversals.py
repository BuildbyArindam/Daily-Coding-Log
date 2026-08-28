"""
Problem   : Minimum Edge Reversals
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MIEDRE
Date      : 2026-08-28

Approach  :
    Build a graph where each original directed edge (u -> v) has cost 0,
    and its reverse (v -> u) has cost 1 (representing "must flip this edge").
    Run 0-1 BFS from node 1 to find the minimum total reversal cost to reach
    node N. 0-1 BFS uses a deque: cost-0 edges push to the front, cost-1
    edges push to the back, giving Dijkstra-like correctness in O(N + M).

Time Complexity  : O(N + M)   -- each edge processed once, deque ops O(1)
Space Complexity : O(N + M)   -- adjacency list + distance array
"""


# ------------------------- Solution ---------------------------


from collections import deque
import sys

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append((v, 0))
        graph[v].append((u, 1))
    INF = 10**18
    dist = [INF] * (N + 1)
    dist[1] = 0
    dq = deque([1])
    while dq:
        u = dq.popleft()
        for v, cost in graph[u]:
            new_dist = dist[u] + cost
            if new_dist < dist[v]:
                dist[v] = new_dist
                if cost == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    print(-1 if dist[N] == INF else dist[N])

if __name__ == "__main__":
    solve()
