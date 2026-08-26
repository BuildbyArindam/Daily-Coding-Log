# ============================================================
# Problem   : The Whispering Roots of Devgarh
# Platform  : Unstop
# Link      : https://unstop.com/code/practice/656580
# Difficulty: Medium
# Topics    : Tree, Rerooting DP, Weighted Tree, Subtree Sum, DFS, Distance Contribution
# Date      : 2026-08-26
#
# Approach:
#   1. Root the tree at node 0, build parent/parent_weight/dist via iterative BFS-order DFS.
#   2. Compute subtree_sum[u] (sum of values in u's subtree) via a reverse pass over visit order.
#   3. Compute root_resonance = sum(value[i] * dist(root, i)) directly for the root.
#   4. Reroot: when moving root from p to child u across edge weight w, every node in u's
#      subtree gets w closer and every node outside gets w farther, so:
#        ans[u] = ans[p] + w * (total_value - 2 * subtree_sum[u])
#      This is the classic rerooting-DP trick for distance-weighted subtree contributions.
#
# Time complexity : O(N)  — one DFS to build order/subtree sums, one pass to reroot
# Space complexity: O(N)  — adjacency list, parent/dist/subtree_sum arrays, iterative stack
# ============================================================


# --------------------------------- Solution --------------------------------------------


# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
input = sys.stdin.readline
n = int(input())
value = list(map(int, input().split()))
if n == 1:
    print(0)
    sys.exit()
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))
parent = [-1] * n
parent_weight = [0] * n
dist = [0] * n
order = [0]
parent[0] = -2  
for u in order:
    for v, w in graph[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        parent_weight[v] = w
        dist[v] = dist[u] + w
        order.append(v)
total_value = sum(value)
subtree_sum = value[:]
for u in reversed(order[1:]):
    subtree_sum[parent[u]] += subtree_sum[u]
root_resonance = sum(value[i] * dist[i] for i in range(n))
ans = [0] * n
ans[0] = root_resonance
for u in order[1:]:
    p = parent[u]
    w = parent_weight[u]
    ans[u] = ans[p] + w * (total_value - 2 * subtree_sum[u])

print(*ans)
