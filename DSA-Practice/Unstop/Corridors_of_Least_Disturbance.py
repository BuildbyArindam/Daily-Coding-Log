"""
Problem   : Corridors of Least Disturbance
Platform  : Unstop
Link      : https://unstop.com/code/practice/661277
Difficulty: Hard
Date      : 2026-09-30
Topics    : Graph, MST, Kruskal, DSU, Binary Lifting, LCA, Minimum Bottleneck Path

Approach:
    For each query (a, b), the answer is the minimum possible value of the
    maximum edge weight on any path from a to b (minimum bottleneck path).
    1. Sort edges by weight and run Kruskal with DSU (union by size).
    2. Build a Kruskal Reconstruction Tree: each successful union creates a
       new node whose weight is the edge weight, with the two component
       roots as children. Original vertices are leaves (1..n).
    3. Preprocess binary lifting tables (iterative DFS to avoid recursion).
    4. For a query, if a and b are in different trees the answer is -1;
       if a == b it is 0; otherwise it is weight[LCA(a, b)].

Complexity:
    Time  : O(m log m) for sorting + O(m α(n)) for DSU
            + O(n log n) for lifting tables + O(q log n) for queries
    Space : O(n log n) for the binary lifting table (tree has at most 2n nodes)
"""


# ---------------------------------- Solution --------------------------------------------


def compute_worst_corridor(n, m, corridors, q, queries):
    import sys
    sys.setrecursionlimit(1_000_000)
    corridors.sort(key=lambda x: x[2])
    max_nodes = 2 * n + 5
    parent = list(range(max_nodes))
    size = [1] * max_nodes
    weight = [0] * max_nodes
    tree_root = list(range(max_nodes))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    tree = [[] for _ in range(max_nodes)]
    next_node = n + 1
    for u, v, w in corridors:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            continue
        x = next_node
        next_node += 1
        weight[x] = w
        left_root = tree_root[ru]
        right_root = tree_root[rv]
        tree[x].append(left_root)
        tree[x].append(right_root)
        if size[ru] < size[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        size[ru] += size[rv]
        tree_root[ru] = x
    total_nodes = next_node
    component_root = [0] * (n + 1)
    for v in range(1, n + 1):
        component_root[v] = tree_root[find(v)]
    LOG = max(1, total_nodes.bit_length())
    up = [[0] * total_nodes for _ in range(LOG)]
    depth = [0] * total_nodes
    visited = [False] * total_nodes
    for v in range(1, n + 1):
        root = component_root[v]
        if visited[root]:
            continue
        visited[root] = True
        stack = [(root, 0, 0)]
        while stack:
            node, par, dep = stack.pop()
            up[0][node] = par
            depth[node] = dep
            for child in tree[node]:
                visited[child] = True
                stack.append((child, node, dep + 1))
    for k in range(1, LOG):
        prev = up[k - 1]
        cur = up[k]
        for v in range(total_nodes):
            cur[v] = prev[prev[v]]
    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        diff = depth[a] - depth[b]
        bit = 0
        while diff:
            if diff & 1:
                a = up[bit][a]
            diff >>= 1
            bit += 1
        if a == b:
            return a
        for k in range(LOG - 1, -1, -1):
            if up[k][a] != up[k][b]:
                a = up[k][a]
                b = up[k][b]
        return up[0][a]
    results = [-1] * q
    for i, (a, b) in enumerate(queries):
        if component_root[a] != component_root[b]:
            results[i] = -1
        elif a == b:
            results[i] = 0
        else:
            ancestor = lca(a, b)
            results[i] = weight[ancestor]
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    n, m = int(data[index]), int(data[index + 1])
    index += 2
    corridors = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        corridors.append((u, v, w))
        index += 3
    q = int(data[index])
    index += 1
    queries = []
    for _ in range(q):
        a = int(data[index])
        b = int(data[index + 1])
        queries.append((a, b))
        index += 2
    results = compute_worst_corridor(n, m, corridors, q, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
