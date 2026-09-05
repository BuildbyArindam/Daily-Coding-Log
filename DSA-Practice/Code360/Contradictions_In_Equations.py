"""
Problem: Contradictions In Equations
Platform: Code360
Link: https://www.naukri.com/code360/problems/contradictions-in-equations_7084824?kunjiRedirection=true
Difficulty: Hard
Date: 2026-09-05
Topics: Graph, DFS, Weighted Graph

Approach:
    Build an undirected weighted graph where each equation (a, b, value)
    adds edges a -> b (weight = value) and b -> a (weight = 1/value).
    For each unvisited node, assign it a base weight of 1.0 and run an
    iterative DFS (explicit stack), propagating expected weights to
    neighbors as weight[u] / ratio. If a neighbor is already visited,
    verify the existing weight matches the expected one within a small
    epsilon (1e-9) — a mismatch means the equations are contradictory.

Time Complexity:  O(V + E)  — each node/edge visited once per component
Space Complexity: O(V + E)  — adjacency list + weight map + stack
"""


# -------------------------- Solution --------------------------------


from typing import *

def ContradictionsInEquations(equations : List[List[str]], values : List[float]) -> bool:
    graph = {}
    for (a, b), value in zip(equations, values):
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append((b, value))
        graph[b].append((a, 1.0 / value))
    weight = {}
    for start in graph:
        if start in weight:
            continue
        weight[start] = 1.0
        stack = [start]
        while stack:
            u = stack.pop()
            for v, ratio in graph[u]:
                expected_weight_v = weight[u] / ratio
                if v not in weight:
                    weight[v] = expected_weight_v
                    stack.append(v)
                else:
                    actual_ratio = weight[u] / weight[v]
                    if abs(actual_ratio - ratio) > 1e-9:
                        return True
    return False
