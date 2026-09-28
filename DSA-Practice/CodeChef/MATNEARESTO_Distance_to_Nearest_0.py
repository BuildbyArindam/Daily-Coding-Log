"""
Platform   : CodeChef
Problem    : Distance to Nearest 0 (MATNEARESTO)
Link       : https://www.codechef.com/DSAMONDAY022/problems/MATNEARESTO
Date       : 2026-09-28
Difficulty : Hard
Topics     : Multi-source BFS, Matrix/Grid

Approach:
    For every cell, find the Manhattan distance to the nearest '0'.
    Instead of running a BFS from each cell, start one BFS from all '0'
    cells at once (distance 0). Each BFS layer expands by one step in the
    four directions, so the first time a cell is reached is its shortest
    distance. The grid is flattened into a 1D list, with divmod recovering
    row and column.

Time  : O(R * C), each cell is visited once
Space : O(R * C), for the result array and BFS layers
"""


# ----------------------------------- Solution --------------------------------------------------------


import sys

def compute_distances(rows, cols, cells):
    total = rows * cols
    UNSEEN = -1
    result = [UNSEEN] * total
    layer = [i for i in range(total) if cells[i] == '0']
    for i in layer:
        result[i] = 0
    depth = 0
    while layer:
        depth += 1
        upcoming = []
        for pos in layer:
            r, c = divmod(pos, cols)
            if r + 1 < rows and result[pos + cols] == UNSEEN:
                result[pos + cols] = depth
                upcoming.append(pos + cols)
            if r > 0 and result[pos - cols] == UNSEEN:
                result[pos - cols] = depth
                upcoming.append(pos - cols)
            if c + 1 < cols and result[pos + 1] == UNSEEN:
                result[pos + 1] = depth
                upcoming.append(pos + 1)
            if c > 0 and result[pos - 1] == UNSEEN:
                result[pos - 1] = depth
                upcoming.append(pos - 1)
        layer = upcoming
    return result

def main():
    tokens = sys.stdin.read().split()
    rows, cols = int(tokens[0]), int(tokens[1])
    cells = tokens[2:2 + rows * cols]
    flat = compute_distances(rows, cols, cells)
    lines = []
    for r in range(rows):
        chunk = flat[r * cols:(r + 1) * cols]
        lines.append(" ".join(map(str, chunk)))
    sys.stdout.write("\n".join(lines) + "\n")

main()
