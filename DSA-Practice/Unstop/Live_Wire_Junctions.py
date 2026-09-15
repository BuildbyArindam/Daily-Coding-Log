"""
Problem   : Live Wire Junctions
Platform  : Unstop
Link      : https://unstop.com/code/practice/659727
Difficulty: Hard
Date      : 2026-09-15
Topics    : Tree, Heavy-Light Decomposition (HLD), Fenwick Tree (BIT), Path Queries, Point Toggle

Approach:
    - Root the tree at node 1; compute parent/depth/subtree-size via iterative
      BFS-order traversal, then pick a heavy child per node (max subtree size)
      to build Heavy-Light Decomposition chains (head[], pos[]).
    - Maintain a Fenwick Tree over the HLD position array, where each node's
      slot holds 1 if it is currently "active" (state[v] == 1) and 0 otherwise.
      Node 1 is excluded/never toggled (root has no state).
    - Query type 1 (toggle v): flip state[v] and add +1/-1 at pos[v] in the BIT.
    - Query type 2 (path sum u..v): walk up chains, jumping u or v to the
      shallower chain head each time, accumulating BIT range sums over each
      chain segment, until u and v share a chain head; add the final
      same-chain segment.

Complexity:
    Build      : O(N) tree traversal + O(N log N) BIT init
    Toggle      : O(log N) per update
    Path query  : O(log^2 N) per query  (O(log N) chain jumps * O(log N) BIT range sum)
    Overall     : O((N + Q) log^2 N) time, O(N) space
"""


# ------------------------------- Solution ---------------------------------------------


import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    def sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res
    def range_sum(self, l, r):
        if l > r:
            return 0
        return self.sum(r) - self.sum(l - 1)

def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    size = [1] * (n + 1)
    heavy = [-1] * (n + 1)
    order = [1]
    parent[1] = 0
    for u in order:
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            order.append(v)
    for u in reversed(order):
        max_size = 0
        for v in graph[u]:
            if parent[v] != u:
                continue
            size[u] += size[v]
            if size[v] > max_size:
                max_size = size[v]
                heavy[u] = v
    head = [0] * (n + 1)
    pos = [0] * (n + 1)
    current_pos = 0
    stack = [(1, 1)]
    while stack:
        start, chain_head = stack.pop()
        u = start
        while u != -1:
            head[u] = chain_head
            current_pos += 1
            pos[u] = current_pos
            for v in graph[u]:
                if parent[v] == u and v != heavy[u]:
                    stack.append((v, v))
            u = heavy[u]
    bit = FenwickTree(n)
    for v in range(2, n + 1):
        bit.add(pos[v], 1)
    state = [0] * (n + 1)
    for v in range(2, n + 1):
        state[v] = 1
    def path_sum(u, v):
        result = 0
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            result += bit.range_sum(pos[head[u]], pos[u])
            u = parent[head[u]]
        if depth[u] > depth[v]:
            u, v = v, u
        result += bit.range_sum(pos[u] + 1, pos[v])
        return result
    q = int(input())
    output = []
    for _ in range(q):
        event = list(map(int, input().split()))
        if event[0] == 1:
            v = event[1]
            if state[v] == 1:
                state[v] = 0
                bit.add(pos[v], -1)
            else:
                state[v] = 1
                bit.add(pos[v], 1)
        else:
            u, v = event[1], event[2]
            output.append(str(path_sum(u, v)))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    solve()
