"""
Problem   : Longest Colored Path
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/longest-colored-path--151454/1
Difficulty: Hard
Topics    : Tree, DFS/BFS, Dynamic Programming (Tree DP)
Date      : 2026-09-27

Approach:
Root the tree at node 0 and get an iterative BFS order (avoids recursion-depth
issues on skewed trees). Process nodes in reverse BFS order (leaves -> root)
so every child is finalized before its parent.

For each node track four values:
  - RR[v] / BB[v]: length of the longest downward path ending at v that is
    monochromatic red / blue respectively.
  - F[v] / G[v]  : longest downward path ending at v allowing a color switch,
    used to combine a red segment with a blue segment through v.
At each node, take the best and second-best qualifying child value among its
children (diameter-of-tree technique) to combine two downward chains through
v into a candidate answer path, updating the running global maximum `ans`.

Time Complexity : O(N) - one BFS pass + one reverse pass, O(children) work
                  per node (best/second-best scan), sums to O(N) overall.
Space Complexity: O(N) - adjacency list, parent/order arrays, and the four
                  DP arrays (RR, BB, F, G), each of size N.
"""


# ------------------------------------- Solution ---------------------------------------------------


class Solution:
    def longestPath(self, s, edges):
        # code here
        n = len(s)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1] * n
        parent[0] = -2
        order = [0]
        for v in order:
            for nei in graph[v]:
                if parent[nei] == -1:
                    parent[nei] = v
                    order.append(nei)
        RR = [0] * n
        BB = [0] * n
        F = [0] * n
        G = [0] * n
        ans = 1
        for v in reversed(order):
            children = [u for u in graph[v] if parent[u] == v]
            best_rr = 0
            best_bb = 0
            best_f = 0
            best_g = 0
            for u in children:
                best_rr = max(best_rr, RR[u])
                best_bb = max(best_bb, BB[u])
                best_f = max(best_f, F[u])
                best_g = max(best_g, G[u])
            if s[v] == 'R':
                RR[v] = 1 + best_rr
                G[v] = 1 + best_rr
                F[v] = 1 + best_f
                BB[v] = 0
                first = (-1, -1) 
                second = (-1, -1)
                for u in children:
                    val = F[u]
                    if val > first[0]:
                        second = first
                        first = (val, u)
                    elif val > second[0]:
                        second = (val, u)
                for u in children:
                    other = first if first[1] != u else second
                    if other[1] != -1:
                        ans = max(ans, RR[u] + 1 + other[0])
            else: 
                RR[v] = 0
                BB[v] = 1 + best_bb
                F[v] = 1 + best_bb
                G[v] = 1 + best_g
                first = (-1, -1)   
                second = (-1, -1)
                for u in children:
                    val = BB[u]
                    if val > first[0]:
                        second = first
                        first = (val, u)
                    elif val > second[0]:
                        second = (val, u)
                for u in children:
                    other = first if first[1] != u else second
                    if other[1] != -1:
                        ans = max(ans, G[u] + 1 + other[0])
            ans = max(ans, F[v], G[v], RR[v], BB[v])
        return ans
