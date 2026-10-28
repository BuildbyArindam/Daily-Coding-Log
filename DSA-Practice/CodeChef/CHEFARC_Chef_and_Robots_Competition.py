"""
Platform   : CodeChef
Problem    : Chef and Robots Competition (CHEFARC)
Link       : https://www.codechef.com/problems/CHEFARC
Difficulty : 2018
Topics     : BFS, Implementation, Graph Algos, Traversals
Date       : 2026-10-28

Approach:
    Two robots start at opposite top corners of a grid and each jumps to any
    non-blocked cell within Manhattan distance k per move. We need the minimum
    time at which both can stand on the same cell.
    1. Run a multi-jump BFS from the robot's start cell. All cells in the
       Manhattan diamond of radius k around the current cell are reachable in
       one move.
    2. To avoid rescanning visited cells, each row keeps a "next unvisited
       cell" pointer array with path compression (DSU-style). Visited and
       blocked cells point to the next column, so each cell is claimed once.
    3. The second robot's start is at the top-right corner, so mirror the grid
       horizontally and reuse the same BFS.
    4. Answer = min over all cells of max(distA, distB), or -1 if no cell is
       reachable by both.

Complexity:
    Time  : O(R * C * min(R, 2k + 1) * alpha) per test, since each popped cell
            scans up to 2k + 1 rows, and every cell is visited at most once.
    Space : O(R * C) for the distance arrays and pointer tables.
"""


# ---------------------------------------------- Solution ------------------------------------------------------------


import sys

def jump(ptr, c):
    top = c
    while ptr[top] != top:
        top = ptr[top]
    while ptr[c] != top:
        ptr[c], c = top, ptr[c]
    return top

def spread(board, R, C, rng):
    ptrs = [[(c + 1 if board[r][c] else c) for c in range(C)] + [C]
            for r in range(R)]
    res = [-1] * (R * C)
    ptrs[0][0] = 1
    res[0] = 0
    todo = [(0, 0)]
    idx = 0
    while idx < len(todo):
        x, y = todo[idx]
        idx += 1
        nd = res[x * C + y] + 1
        top_row = x - rng if x - rng > 0 else 0
        bot_row = x + rng if x + rng < R - 1 else R - 1
        for r in range(top_row, bot_row + 1):
            span = rng - abs(r - x)
            left = y - span if y - span > 0 else 0
            right = y + span if y + span < C - 1 else C - 1
            p = ptrs[r]
            c = jump(p, left)
            while c <= right:
                res[r * C + c] = nd
                p[c] = c + 1
                todo.append((r, c))
                c = jump(p, c + 1)
    return res

def main():
    tok = sys.stdin.read().split()
    pos = 0
    tests = int(tok[pos]); pos += 1
    out = []
    for _ in range(tests):
        R, C, ka, kb = (int(v) for v in tok[pos:pos + 4])
        pos += 4
        board = []
        for _r in range(R):
            board.append([int(v) for v in tok[pos:pos + C]])
            pos += C
        mirrored = [row[::-1] for row in board]
        da = spread(board, R, C, ka)
        db = spread(mirrored, R, C, kb)
        best = -1
        for r in range(R):
            for c in range(C):
                x = da[r * C + c]
                y = db[r * C + (C - 1 - c)]
                if x < 0 or y < 0:
                    continue
                m = x if x > y else y
                if best < 0 or m < best:
                    best = m
        out.append(str(best))
    print("\n".join(out))

main()
