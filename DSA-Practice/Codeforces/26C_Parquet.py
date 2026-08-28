"""
Problem: Parquet
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/26/C
Date Solved: 2026-08-28
Difficulty: *2000
Topics: Combinatorics, Constructive Algorithms, Greedy, Implementation

Approach:
Handle odd n/odd m edge cases first by peeling off a leftover row/column and
tiling it with 1x2 planks (fail if not enough 'a' planks available for the
odd row, or 'b' planks for the odd column). What remains is an even x even
grid split into 2x2 blocks. Greedily fill each block: prefer a 2x2 plank (c),
then two vertical 1x2 planks (a), then two horizontal 1x2 planks (b) - check
total capacity (c + a//2 + b//2) against block count up front to fail fast.
Finally, build an adjacency graph between plank IDs based on shared cell
borders and greedily color it (graph coloring / "welsh-powell"-style
first-fit) so adjacent planks never share a letter.

Time Complexity: O(n*m) - grid construction, plank adjacency, and greedy
                  coloring are all linear in the number of cells/planks.
Space Complexity: O(n*m) - grid, plank graph, and color arrays.
"""


# ---------------------------------- Solution -------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    n, m, a, b, c = map(int, input().split())
    if n % 2 == 1 and m % 2 == 1:
        print("IMPOSSIBLE")
        return
    grid = [[-1] * m for _ in range(n)]
    plank_count = 0
    def add_plank(cells):
        nonlocal plank_count
        pid = plank_count
        plank_count += 1
        for r, col in cells:
            grid[r][col] = pid
    rows = n
    cols = m
    if n % 2 == 1:
        need = m // 2
        if a < need:
            print("IMPOSSIBLE")
            return
        for col in range(0, m, 2):
            add_plank([(n - 1, col), (n - 1, col + 1)])
        a -= need
        n -= 1
    if m % 2 == 1:
        need = n // 2
        if b < need:
            print("IMPOSSIBLE")
            return
        for row in range(0, n, 2):
            add_plank([(row, m - 1), (row + 1, m - 1)])
        b -= need
        m -= 1
    blocks = (n // 2) * (m // 2)
    capacity = c + a // 2 + b // 2
    if capacity < blocks:
        print("IMPOSSIBLE")
        return
    for r in range(0, n, 2):
        for col in range(0, m, 2):
            if c > 0:
                add_plank([
                    (r, col),
                    (r, col + 1),
                    (r + 1, col),
                    (r + 1, col + 1)
                ])
                c -= 1
            elif a >= 2:
                add_plank([(r, col), (r, col + 1)])
                add_plank([(r + 1, col), (r + 1, col + 1)])
                a -= 2
            else:
                add_plank([(r, col), (r + 1, col)])
                add_plank([(r, col + 1), (r + 1, col + 1)])
                b -= 2
    graph = [set() for _ in range(plank_count)]
    for r in range(rows):
        for col in range(cols):
            pid = grid[r][col]
            if r + 1 < rows:
                qid = grid[r + 1][col]
                if pid != qid:
                    graph[pid].add(qid)
                    graph[qid].add(pid)
            if col + 1 < cols:
                qid = grid[r][col + 1]
                if pid != qid:
                    graph[pid].add(qid)
                    graph[qid].add(pid)
    color = [-1] * plank_count
    for pid in range(plank_count):
        used = {color[q] for q in graph[pid] if color[q] != -1}
        col = 0
        while col in used:
            col += 1
        color[pid] = col
    letters = "abcdefghijklmnopqrstuvwxyz"
    answer = [
        "".join(letters[color[grid[r][col]]] for col in range(cols))
        for r in range(rows)
    ]
    print("\n".join(answer))

if __name__ == "__main__":
    solve()
