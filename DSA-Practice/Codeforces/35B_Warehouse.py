"""
Problem   : Warehouse
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/35/B
Difficulty: *1700
Topic     : Implementation
Date      : 2026-09-01

Approach:
    Simulate the warehouse as an n x m grid. Maintain a dict mapping
    box_id -> (row, col) for O(1) removal lookups.
    On "+1 x y id": scan shelf x rightward from column y for the first
    empty cell; if the shelf has no room from y onward, fall through to
    scanning every subsequent shelf (row x+1..n-1) left-to-right for the
    first empty cell. If nothing is free anywhere, the box is discarded.
    On "-1 id": look up the box's stored position, report it, then clear
    the cell and remove it from the dict.

Complexity:
    Time  : O(k * n * m) worst case — each "+1" query may scan up to the
            entire grid if shelves are nearly full; each "-1" query is O(1).
    Space : O(n * m) for the grid plus O(k) for the position dict.
"""


# ----------------------- Solution ---------------------------------


with open("input.txt", "r") as f:
    n, m, k = map(int, f.readline().split())
    grid = [[None] * m for _ in range(n)]
    pos = {}
    answer = []
    for _ in range(k):
        query = f.readline().split()
        if query[0] == "+1":
            x = int(query[1]) - 1
            y = int(query[2]) - 1
            box_id = query[3]
            placed = False
            for col in range(y, m):
                if grid[x][col] is None:
                    grid[x][col] = box_id
                    pos[box_id] = (x, col)
                    placed = True
                    break
            if not placed:
                for row in range(x + 1, n):
                    for col in range(m):
                        if grid[row][col] is None:
                            grid[row][col] = box_id
                            pos[box_id] = (row, col)
                            placed = True
                            break
                    if placed:
                        break
        else:  
            box_id = query[1]
            if box_id not in pos:
                answer.append("-1 -1")
            else:
                row, col = pos[box_id]
                answer.append(f"{row + 1} {col + 1}")
                grid[row][col] = None
                del pos[box_id]
with open("output.txt", "w") as f:
    f.write("\n".join(answer))
