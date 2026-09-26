"""
Problem   : The Loyalty of the Orcs
Link      : https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/FSSYNC
Platform  : CodeChef | Difficulty: Hard
Date      : 2026-09-26
Topics    : Trees / Tree DP, Probability & Expected Value, Linearity of Expectation, DFS (iterative), Combinatorics

Approach:
- Tree rooted at node 1. Iterative DFS (explicit stack, no recursion) tracks
  `dead_above` = number of "fallen" (dead) ancestors on the root-to-node path.
- By linearity of expectation, each node contributes dead_above / (dead_above + 1)
  to the total answer. This is the classic "expected relative-order / record"
  term that shows up when children order is treated as random — summing it
  over all nodes gives the expected count in O(N).
- Explicit stack avoids Python recursion-depth limits on deep/skewed trees.

Time Complexity  : O(N) per test case — each node & edge visited once.
Space Complexity : O(N) — adjacency list, dead[] array, explicit stack.
"""


# ---------------------------------------- Solution -------------------------------------------------


import sys

def solve_case(n, links, fallen):
    graph = [[] for _ in range(n + 1)]
    for a, b in links:
        graph[a].append(b)
        graph[b].append(a)
    dead = [False] * (n + 1)
    for x in fallen:
        dead[x] = True
    todo = [(1, 0, 0)]
    expected = 0.0
    while todo:
        node, parent, dead_above = todo.pop()
        expected += dead_above / (dead_above + 1.0)
        next_count = dead_above + (1 if dead[node] else 0)
        for nxt in graph[node]:
            if nxt != parent:
                todo.append((nxt, node, next_count))
    return expected

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    test_cases = data[pos]
    pos += 1
    ans = []
    for _ in range(test_cases):
        n = data[pos]
        pos += 1
        edges = []
        for _ in range(n - 1):
            u = data[pos]
            v = data[pos + 1]
            pos += 2
            edges.append((u, v))
        m = data[pos]
        pos += 1
        dead_list = data[pos:pos + m]
        pos += m
        value = solve_case(n, edges, dead_list)
        ans.append(f"{value:.10f}")
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
