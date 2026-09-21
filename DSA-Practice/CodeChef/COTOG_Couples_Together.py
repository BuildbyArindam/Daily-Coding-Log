"""
Problem   : Couples Together
Platform  : CodeChef (DSAMONDAY021)
Link      : https://www.codechef.com/DSAMONDAY021/problems/COTOG
Date      : 2026-09-21
Difficulty: Medium
Topics    : Union-Find (DSU), Graphs, Greedy

Approach:
    Treat each couple as a graph node. For every adjacent seat pair,
    union the couples occupying those two seats. Each resulting
    connected component of size k needs exactly (k - 1) swaps to
    seat every couple together, since a component of k couples forms
    a "cycle" of misplaced pairs resolvable in k-1 adjacent swaps.
    Answer = sum of (component_size - 1) over all DSU components.

Complexity:
    Time  : O(n * alpha(n))  -- n = number of couples, near-linear
    Space : O(n)             -- parent/rank arrays
"""


# ------------------------------------- Solution -------------------------------------------


import sys

def resolve_root(parent, node):
    path = []
    while parent[node] != node:
        path.append(node)
        node = parent[node]
    for p in path:
        parent[p] = node
    return node

def merge_groups(parent, rank, a, b):
    ra, rb = resolve_root(parent, a), resolve_root(parent, b)
    if ra == rb:
        return
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1

def main():
    data = sys.stdin.read().split()
    idx = 0
    n_couples = int(data[idx]); idx += 1
    total_seats = 2 * n_couples
    seating = [int(data[idx + i]) for i in range(total_seats)]
    couple_id = [p // 2 for p in seating]
    parent = list(range(n_couples))
    rank = [0] * n_couples
    for seat in range(0, total_seats, 2):
        left_couple = couple_id[seat]
        right_couple = couple_id[seat + 1]
        merge_groups(parent, rank, left_couple, right_couple)
    group_size = {}
    for c in range(n_couples):
        root = resolve_root(parent, c)
        group_size[root] = group_size.get(root, 0) + 1
    swaps_needed = sum(size - 1 for size in group_size.values())
    print(swaps_needed)

if __name__ == "__main__":
    main()
