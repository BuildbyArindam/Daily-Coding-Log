"""
Problem   : Snake and Ladder Problem
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/snake-and-ladder-problem4816/1
Difficulty: Hard
Topics    : BFS, Graph, Dynamic Programming
Date      : 2026-08-18

Approach:
    Model the board (1..n*n) as a graph where each cell has edges to the
    cells reachable by a dice roll (1-6). Snakes and ladders are modeled
    as "jump" shortcuts: landing on a snake/ladder cell immediately
    teleports to its destination. Since every edge has equal weight
    (1 dice throw), the minimum number of throws to reach cell n*n is
    just the shortest path in this unweighted graph — solved with BFS.
    The first time we pop the destination cell N, the recorded throw
    count is the answer.

Time complexity : O(n^2)   — each of the n*n cells is visited once,
                              with 6 constant-time edge checks each.
Space complexity: O(n^2)   — for the jump table, visited array, and queue.
"""


# ------------------------- Solution -------------------------


from collections import deque

class Solution:
    def minThrows(self, n, lad, sn):
        # code here
        N = n * n
        jump = list(range(N + 1))
        for i in range(0, len(lad), 2):
            jump[lad[i]] = lad[i + 1]
        for i in range(0, len(sn), 2):
            jump[sn[i]] = sn[i + 1]
        q = deque([(1, 0)])
        visited = [False] * (N + 1)
        visited[1] = True
        while q:
            cell, throws = q.popleft()
            for dice in range(1, 7):
                nxt = cell + dice
                if nxt > N:
                    break
                nxt = jump[nxt]
                if nxt == N:
                    return throws + 1
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, throws + 1))
        return -1
