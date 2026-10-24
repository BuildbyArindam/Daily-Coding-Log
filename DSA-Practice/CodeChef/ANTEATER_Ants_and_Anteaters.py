"""
Problem   : Ants and Anteaters (ANTEATER)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ANTEATER
Difficulty: 2014
Date      : 2026-10-24
Topics    : Simulation, Grid, Hash Map, Counting

Approach:
    Simulate the grid one second at a time. Each ant moves one cell in its
    direction; it is removed if it leaves the grid or steps onto an anteater
    ('#'). After each step, count the surviving ants per cell with a hash map
    and add C(k, 2) = k*(k-1)/2 for every cell holding k ants, which counts
    each pair of ants meeting in the same cell at the same time. Stop when no
    ants remain.

Complexity (per test case, R rows, C columns):
    Time : O(R * C * max(R, C)) - at most R*C ants, and every ant is gone
           after at most max(R, C) steps.
    Space: O(R * C) - ant list plus per-step tally.

Note: the cell key ny * 100 + nx assumes C < 100 (true for the constraints).
"""


# ----------------------------------------- Solution --------------------------------------------------


import sys

def solve_one(rows, cols, board):
    mv = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    live = []
    for y in range(rows):
        line = board[y]
        for x in range(cols):
            ch = line[x]
            if ch in mv:
                live.append((y, x, mv[ch][0], mv[ch][1]))
    answer = 0
    while live:
        tally = {}
        fresh = []
        for y, x, dy, dx in live:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= rows or nx >= cols:
                continue
            if board[ny][nx] == '#':
                continue
            fresh.append((ny, nx, dy, dx))
            key = ny * 100 + nx
            tally[key] = tally.get(key, 0) + 1
        for v in tally.values():
            answer += v * (v - 1) // 2
        live = fresh
    return answer

def main():
    tokens = sys.stdin.read().split()
    cases = int(tokens[0])
    pos = 1
    res = []
    for _ in range(cases):
        r = int(tokens[pos])
        c = int(tokens[pos + 1])
        pos += 2
        board = tokens[pos:pos + r]
        pos += r
        res.append(str(solve_one(r, c, board)))
    sys.stdout.write("\n".join(res) + "\n")

main()
