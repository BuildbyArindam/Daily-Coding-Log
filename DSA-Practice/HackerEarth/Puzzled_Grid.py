"""
Problem   : Puzzled Grid (HackerEarth)
Link      : https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/puzzled-grid-1/
Date      : 2026-10-15
Difficulty: Hard
Topics    : Kruskal Reconstruction Tree, DSU, Binary Lifting, LCA, Grid Graph

Approach  :
  Treat each cell as a node. The edge between adjacent cells has weight
  max(cell_u, cell_v), so a path's cost is the largest cell value on it.
  Each query asks for the minimum possible path cost between two cells
  (minimax path).
  1. Pack (weight, u, v) into one integer per edge and sort for speed.
  2. Run Kruskal with DSU, but on every merge create a new tree node whose
     value is the edge weight and whose children are the two merged
     components. This builds a Kruskal Reconstruction Tree.
  3. The answer for a query is the value stored at LCA(cell1, cell2).
  4. LCA is done with binary lifting (iterative DFS for depths, so no
     recursion limit issues).

Complexity (N = n*n cells, Q queries):
  Time  : O(N log N) for sorting edges + near-linear DSU
          + O(N log N) to build lifting tables + O(Q log N) for queries
  Space : O(N log N) for the binary lifting tables
          (tree has 2N-1 nodes, packed edges are freed after the build)
"""


# -------------------------------------------------- Solution -----------------------------------------------------


import sys
from array import array
readline = sys.stdin.buffer.readline
n, q = map(int, readline().split())
size = n * n
grid = array('i')
for _ in range(n):
    grid.extend(map(int, readline().split()))
query_a = array('i')
query_b = array('i')
for _ in range(q):
    r1, c1, r2, c2 = map(int, readline().split())
    query_a.append(r1 * n + c1)
    query_b.append(r2 * n + c2)
bits = (size - 1).bit_length()
shift = 2 * bits
mask = (1 << bits) - 1
edges = []
for r in range(n):
    row = r * n
    for c in range(n):
        u = row + c
        if c + 1 < n:
            v = u + 1
            w = max(grid[u], grid[v])
            edges.append((w << shift) | (u << bits) | v)
        if r + 1 < n:
            v = u + n
            w = max(grid[u], grid[v])
            edges.append((w << shift) | (u << bits) | v)
edges.sort()
total = 2 * size - 1
left = array('i', [-1]) * total
right = array('i', [-1]) * total
parent = array('i', [-1]) * total
tree_value = array('i', [0]) * total
for i, value in enumerate(grid):
    tree_value[i] = value
dsu = array('i', range(size))
component_size = array('i', [1]) * size
component_tree = array('i', range(size))
def find(x):
    while dsu[x] != x:
        dsu[x] = dsu[dsu[x]]
        x = dsu[x]
    return x
node_count = size
for packed in edges:
    weight = packed >> shift
    u = (packed >> bits) & mask
    v = packed & mask
    a = find(u)
    b = find(v)
    if a == b:
        continue
    if component_size[a] < component_size[b]:
        a, b = b, a
    node = node_count
    node_count += 1
    left[node] = component_tree[a]
    right[node] = component_tree[b]
    parent[left[node]] = node
    parent[right[node]] = node
    tree_value[node] = weight
    dsu[b] = a
    component_size[a] += component_size[b]
    component_tree[a] = node
    if node_count == total:
        break
root = component_tree[find(0)]
del edges, grid, dsu, component_size, component_tree
depth = array('i', [0]) * total
stack = [root]
while stack:
    node = stack.pop()
    child_depth = depth[node] + 1
    a = left[node]
    if a != -1:
        b = right[node]
        depth[a] = child_depth
        depth[b] = child_depth
        stack.append(a)
        stack.append(b)
ancestors = [parent]
for _ in range(1, total.bit_length()):
    prev = ancestors[-1]
    cur = array('i', [-1]) * total
    for i in range(total):
        p = prev[i]
        if p != -1:
            cur[i] = prev[p]
    ancestors.append(cur)

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    difference = depth[a] - depth[b]
    bit = 0
    while difference:
        if difference & 1:
            a = ancestors[bit][a]
        difference >>= 1
        bit += 1
    if a == b:
        return a
    for level in range(len(ancestors) - 1, -1, -1):
        pa = ancestors[level][a]
        pb = ancestors[level][b]
        if pa != pb:
            a, b = pa, pb
    return parent[a]
answers = []
for a, b in zip(query_a, query_b):
    ancestor = lca(a, b)
    answers.append(str(tree_value[ancestor]))
sys.stdout.write('\n'.join(answers))
