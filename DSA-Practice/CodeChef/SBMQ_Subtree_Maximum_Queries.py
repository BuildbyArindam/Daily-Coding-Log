"""
Problem   : Subtree Maximum Queries
Platform  : CodeChef
Link      : https://www.codechef.com/DSAMONDAY020/problems/SBMQ
Date      : 2026-09-14
Difficulty: Medium (~1700-1900) 
Topics    : Trees, Euler Tour, Segment Tree

Approach:
  - Build the tree from parent[] using a counting-sort style adjacency
    list (deg[] -> head[] prefix sums -> kid_buf[]), avoiding
    per-node Python lists for speed.
  - Iterative DFS (explicit stack, no recursion) computes entry_time[]
    and exit_time[] for each node -> Euler tour flattening, so that
    the subtree of any node u corresponds to the contiguous range
    [entry_time[u], exit_time[u]] in the flattened array.
  - Build an iterative max-segment-tree over the flattened weights.
  - Query type 1 (update node u's weight to x): point-update at
    entry_time[u], propagate up.
  - Query type 2 (max in subtree of u): range-max over
    [entry_time[u], exit_time[u]] using the standard iterative
    segment-tree range query.

Complexity:
  Time  : O(N log N) preprocessing (tree build + Euler tour + seg tree
          build), O(log N) per update/query, O(Q log N) total.
  Space : O(N) for adjacency/Euler arrays + O(N) (next power of 2)
          for the segment tree.
"""


# -------------------------- Solution ------------------------------------


import sys

def run():
    raw = sys.stdin.buffer.read().split()
    ptr = 0
    total_nodes = int(raw[ptr]); ptr += 1
    ancestor = [0] * (total_nodes + 1)
    for node_id in range(1, total_nodes + 1):
        ancestor[node_id] = int(raw[ptr]); ptr += 1
    weight = [0] * (total_nodes + 1)
    for node_id in range(1, total_nodes + 1):
        weight[node_id] = int(raw[ptr]); ptr += 1
    deg = [0] * (total_nodes + 2)
    for node_id in range(2, total_nodes + 1):
        deg[ancestor[node_id]] += 1
    head = [0] * (total_nodes + 2)
    for i in range(1, total_nodes + 1):
        head[i + 1] = head[i] + deg[i]
    fill_pos = head[:]
    kid_buf = [0] * (total_nodes - 1 if total_nodes > 0 else 0)
    for node_id in range(2, total_nodes + 1):
        p = ancestor[node_id]
        kid_buf[fill_pos[p]] = node_id
        fill_pos[p] += 1
    entry_time = [0] * (total_nodes + 1)
    exit_time = [0] * (total_nodes + 1)
    clock = 0
    stack_nodes = [1]
    stack_cursor = [head[1]]
    entry_time[1] = 0
    clock = 1
    while stack_nodes:
        cur = stack_nodes[-1]
        c = stack_cursor[-1]
        end = head[cur + 1]
        if c < end:
            child = kid_buf[c]
            stack_cursor[-1] = c + 1
            entry_time[child] = clock
            clock += 1
            stack_nodes.append(child)
            stack_cursor.append(head[child])
        else:
            exit_time[cur] = clock - 1
            stack_nodes.pop()
            stack_cursor.pop()
    flat = [0] * total_nodes
    for node_id in range(1, total_nodes + 1):
        flat[entry_time[node_id]] = weight[node_id]
    leaf_count = 1
    while leaf_count < total_nodes:
        leaf_count <<= 1
    NEG = -1
    tree_arr = [NEG] * (2 * leaf_count)
    for i, v in enumerate(flat):
        tree_arr[leaf_count + i] = v
    for i in range(leaf_count - 1, 0, -1):
        left = tree_arr[2 * i]
        right = tree_arr[2 * i + 1]
        tree_arr[i] = left if left > right else right
    op_count = int(raw[ptr]); ptr += 1
    output_lines = []
    T = tree_arr
    LC = leaf_count
    for _ in range(op_count):
        kind = raw[ptr]; ptr += 1
        if kind == b'1':
            u = int(raw[ptr]); ptr += 1
            x = int(raw[ptr]); ptr += 1
            pos = entry_time[u] + LC
            T[pos] = x
            pos >>= 1
            while pos >= 1:
                l = T[2 * pos]
                r = T[2 * pos + 1]
                T[pos] = l if l > r else r
                pos >>= 1
        else:
            u = int(raw[ptr]); ptr += 1
            lo = entry_time[u] + LC
            hi = exit_time[u] + LC + 1
            best = NEG
            while lo < hi:
                if lo & 1:
                    if T[lo] > best:
                        best = T[lo]
                    lo += 1
                if hi & 1:
                    hi -= 1
                    if T[hi] > best:
                        best = T[hi]
                lo >>= 1
                hi >>= 1
            output_lines.append(str(best))
    sys.stdout.write('\n'.join(output_lines) + ('\n' if output_lines else ''))

if __name__ == '__main__':
    run()
