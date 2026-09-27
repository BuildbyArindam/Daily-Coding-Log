"""
Problem: Walking Path
Platform: CodeChef (ICPC Regional Training Camp, ICPCTR08)
Link: https://www.codechef.com/practice/course/icpc/ICPCTR08/problems/KAN13B
Date Solved: 2026-09-27
Difficulty: Hard
Topics: Graphs, Dijkstra, Shortest Path

Approach:
    Model the grid as a directed graph where each cell is a node and each
    pair of adjacent cells (horizontal/vertical) forms two directed edges,
    one per direction. Edge weight ("hardness") is asymmetric: climbing
    uphill costs more than going downhill, computed from the height
    difference via edge_hardness(). Build the graph as a sparse CSR matrix
    and run Dijkstra's algorithm from each distinct query source to get
    shortest "hardness" paths to arbitrary destinations.

Time Complexity:  O(Q_src * (E log V)) where V = rows*cols, E ~ 4V,
                   Q_src = number of distinct source cells across queries
                   (scipy's dijkstra runs one multi-target search per source).
Space Complexity:  O(V + E) for the sparse graph, plus O(Q_src * V) for the
                   returned distance matrix.
"""


# -------------------------------------------- Solution --------------------------------------------------


import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

def edge_hardness(height_from, height_to):
    delta = height_from - height_to
    root_term = np.sqrt(1.0 + delta * delta)
    if height_from > height_to:
        return 0.5 + 0.5 * root_term
    return -0.5 + 1.5 * root_term

def build_sparse_graph(rows, cols, elevation):
    total_nodes = rows * cols
    src_idx = []
    dst_idx = []
    weights = []
    def nid(r, c):
        return r * cols + c
    for r in range(rows):
        for c in range(cols):
            h_here = elevation[r][c]
            if c + 1 < cols:
                h_next = elevation[r][c + 1]
                a, b = nid(r, c), nid(r, c + 1)
                src_idx.append(a); dst_idx.append(b); weights.append(edge_hardness(h_here, h_next))
                src_idx.append(b); dst_idx.append(a); weights.append(edge_hardness(h_next, h_here))
            if r + 1 < rows:
                h_next = elevation[r + 1][c]
                a, b = nid(r, c), nid(r + 1, c)
                src_idx.append(a); dst_idx.append(b); weights.append(edge_hardness(h_here, h_next))
                src_idx.append(b); dst_idx.append(a); weights.append(edge_hardness(h_next, h_here))
    weights = np.array(weights, dtype=np.float64)
    src_idx = np.array(src_idx, dtype=np.int32)
    dst_idx = np.array(dst_idx, dtype=np.int32)
    graph = csr_matrix((weights, (src_idx, dst_idx)), shape=(total_nodes, total_nodes))
    return graph

def solve_one_case(rows, cols, elevation, queries):
    graph = build_sparse_graph(rows, cols, elevation)
    def nid(r, c):
        return r * cols + c
    source_nodes = []
    for (si, sj, _, _) in queries:
        source_nodes.append(nid(si - 1, sj - 1))
    unique_sources = sorted(set(source_nodes))
    source_pos = {node: pos for pos, node in enumerate(unique_sources)}
    dist_matrix = dijkstra(
        csgraph=graph,
        directed=True,
        indices=unique_sources,
        return_predecessors=False,
    )
    answers = []
    for (si, sj, ei, ej) in queries:
        src = nid(si - 1, sj - 1)
        dst = nid(ei - 1, ej - 1)
        row = source_pos[src]
        answers.append(dist_matrix[row, dst])
    return answers

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0

    def next_token():
        nonlocal pos
        tok = data[pos]
        pos += 1
        return tok

    def next_int():
        return int(next_token())

    def next_float():
        return float(next_token())
    test_count = next_int()
    output_chunks = []
    for case_number in range(1, test_count + 1):
        rows = next_int()
        cols = next_int()
        elevation = []
        for _ in range(rows):
            elevation.append([next_float() for _ in range(cols)])
        query_count = next_int()
        queries = []
        for _ in range(query_count):
            si = next_int(); sj = next_int(); ei = next_int(); ej = next_int()
            queries.append((si, sj, ei, ej))
        results = solve_one_case(rows, cols, elevation, queries)
        output_chunks.append("Case {}:".format(case_number))
        for value in results:
            output_chunks.append("{:.6f}".format(value))
    sys.stdout.write("\n".join(output_chunks) + "\n")

if __name__ == "__main__":
    main()
