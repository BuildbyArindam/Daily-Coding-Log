"""
Problem   : Little Monk and Flip Operations
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/codemonk/8/1483401/
Date      : 2026-09-23
Difficulty: Medium
Topics    : Trees, Bit Manipulation, DP

Approach:
Root the tree at node `a`. Process each bit (0-29) independently with a
bottom-up (post-order) DP. For a node v, dp[v] starts as the max dp value
among its children. If the parity of that max doesn't match the node's bit
at this position, increment by 1 (a "flip" is needed to align parity).
Summing dp[root] across all 30 bit positions gives the total number of
flip operations needed.

Complexity:
  Time : O(N * B)  where N = number of nodes, B = 30 (bit width)
  Space: O(N)      for the adjacency list, parent/order arrays, and per-bit dp array
"""


# -------------------------------------------- Solution -----------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    N, a = map(int, input().split())
    a -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        graph[x].append(y)
        graph[y].append(x)
    A = list(map(int, input().split()))
    parent = [-1] * N
    parent[a] = a
    order = [a]
    for v in order:
        for u in graph[v]:
            if parent[u] == -1:
                parent[u] = v
                order.append(u)
    answer = 0
    for bit in range(30):
        dp = [0] * N
        for v in reversed(order):
            mx = 0
            for u in graph[v]:
                if parent[u] == v:
                    if dp[u] > mx:
                        mx = dp[u]
            current_bit = (A[v] >> bit) & 1
            if (mx & 1) == current_bit:
                dp[v] = mx
            else:
                dp[v] = mx + 1
        answer += dp[a]
    print(answer)

if __name__ == "__main__":
    solve()
