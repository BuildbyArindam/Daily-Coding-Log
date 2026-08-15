"""
Problem   : Tree Path Guardian
Platform  : Unstop
Link      : https://unstop.com/code/practice/650923
Difficulty: Medium
Topics    : Trees, DFS, Monotonic Stack, Union Find, Sorting
Date      : 2026-08-15

Approach:
    For every node v (tree rooted at node 1), find the nearest ancestor u
    on the root-to-v path such that a[u] > a[v] ("guardian" node).

    A single DFS (iterative, explicit stack to avoid recursion limits)
    maintains a *monotonic stack over the current root-to-node path*
    using a persistent-stack trick (prev[] pointers instead of a real
    stack array):
      - On entering v: pop (via prev[] chain) all nodes with
        a[node] <= a[v] to find the closest strictly-greater ancestor.
        That becomes ans[v]. Push v by setting prev[v] = that ancestor
        and top = v.
      - On exiting v (post-order): restore `top` to what it was before
        entering v, so siblings/other branches see the correct path
        state (this is what makes it "per-path" rather than global).

    Each node is pushed and logically popped at most once overall,
    so total work across the DFS is linear.

Time Complexity : O(n)  -- each node visited once, amortized O(1) stack ops
Space Complexity: O(n)  -- adjacency list, prev[], ans[], explicit DFS stack
"""


# ------------------------- Solution ------------------------------


import sys
input = sys.stdin.readline
n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
a = [0] + list(map(int, input().split()))
ans = [-1] * (n + 1)
prev = [-1] * (n + 1)
top = -1
dfs = [(1, 0, 0, -1)]
while dfs:
    v, parent, state, old_top = dfs.pop()
    if state == 0:
        saved_top = top
        cur = top
        while cur != -1 and a[cur] <= a[v]:
            cur = prev[cur]
        ans[v] = cur
        prev[v] = cur
        top = v
        dfs.append((v, parent, 1, saved_top))
        for u in reversed(adj[v]):
            if u != parent:
                dfs.append((u, v, 0, -1))
    else:
        top = old_top
print(*ans[1:])
