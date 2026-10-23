"""
Platform   : CodeChef
Problem    : Chipped Tree (EXUND)
Link       : https://www.codechef.com/problems/EXUND
Difficulty : 2011
Topics     : Basic Math, Cartesian Coordinate System, Geometry, Convex Hull, Observation, Advanced Algorithms, Mathematics, Computational Geometry, Polygons, Algorithms
Date       : 2026-10-23

Approach:
    Root the tree at node 1 and get a BFS order with parent pointers.
    Process nodes in reverse BFS order (children before parents) to compute
    ht[v], the height of v's subtree counted in nodes (a leaf has ht = 1).
    The answer is the number of nodes v with ht[v] <= k.
    BFS is iterative, so there is no recursion-depth problem in Python.

Complexity:
    Time  : O(N) per test case
    Space : O(N)
"""


# ------------------------------------------- Solution ---------------------------------------------------


import sys

def solve_case(tokens, ptr):
    n, k = int(tokens[ptr]), int(tokens[ptr + 1])
    ptr += 2
    nb = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x = int(tokens[ptr]); y = int(tokens[ptr + 1])
        ptr += 2
        nb[x].append(y)
        nb[y].append(x)
    dad = [0] * (n + 1)
    dad[1] = -1
    seq = [1]
    for node in seq:
        pr = dad[node]
        for nx in nb[node]:
            if nx != pr:
                dad[nx] = node
                seq.append(nx)
    ht = [1] * (n + 1)
    i = n - 1
    while i > 0:
        node = seq[i]
        pr = dad[node]
        cand = ht[node] + 1
        if cand > ht[pr]:
            ht[pr] = cand
        i -= 1
    total = 0
    for v in range(1, n + 1):
        if ht[v] <= k:
            total += 1
    return total, ptr

def main():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    ptr = 1
    res = []
    while t:
        ans, ptr = solve_case(tokens, ptr)
        res.append(str(ans))
        t -= 1
    sys.stdout.write("\n".join(res) + "\n")

main()
