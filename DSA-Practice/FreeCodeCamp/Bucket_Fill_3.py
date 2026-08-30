"""
Problem: The Last Challenge: Bucket Fill 3
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-10
Date solved: 2026-08-30
Difficulty: Medium-Hard
Topics: BFS/State-Space Search, Connected Components (Flood Fill), Graph Traversal, Matrix/Grid, Simulation

Approach:
    BFS over grid states. Each state is a flattened tuple of the grid's
    colors. At every step, extract all connected color components (regions)
    and their adjacent colors via a per-state component scan. For each
    region, try recoloring it to any adjacent color (or the target color),
    generating a new state. BFS guarantees the first state where the whole
    grid equals target_color is reached in the minimum number of clicks.

Time complexity:  O(S * R * C) where S = number of distinct states visited
                   and R*C = grid size (each state requires a full
                   component scan + transitions).
Space complexity: O(S * R * C) for storing visited states and the queue.
"""


# ----------------------- Solution -----------------------------


from collections import deque

def bucket_fill(grid, target_color):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    start = tuple(cell for row in grid for cell in row)
    if all(color == target_color for color in start):
        return 0
    colors = set(start)
    colors.add(target_color)
    def get_components(state):
        """Return (color, cells, adjacent_colors) for every region."""
        visited = [False] * (rows * cols)
        components = []
        for start_pos in range(rows * cols):
            if visited[start_pos]:
                continue
            color = state[start_pos]
            stack = [start_pos]
            visited[start_pos] = True
            cells = []
            adjacent_colors = set()
            while stack:
                pos = stack.pop()
                cells.append(pos)
                r, c = divmod(pos, cols)
                for nr, nc in (
                    (r - 1, c),
                    (r + 1, c),
                    (r, c - 1),
                    (r, c + 1),
                ):
                    if 0 <= nr < rows and 0 <= nc < cols:
                        next_pos = nr * cols + nc
                        if state[next_pos] == color:
                            if not visited[next_pos]:
                                visited[next_pos] = True
                                stack.append(next_pos)
                        else:
                            adjacent_colors.add(state[next_pos])
            components.append((color, cells, adjacent_colors))
        return components
    queue = deque([(start, 0)])
    visited_states = {start}
    while queue:
        state, clicks = queue.popleft()
        for color, cells, adjacent_colors in get_components(state):
            possible_colors = adjacent_colors | {target_color}
            for new_color in possible_colors:
                if new_color == color:
                    continue
                new_state = list(state)
                for pos in cells:
                    new_state[pos] = new_color
                new_state = tuple(new_state)
                if new_state in visited_states:
                    continue
                next_clicks = clicks + 1
                if all(cell == target_color for cell in new_state):
                    return next_clicks
                visited_states.add(new_state)
                queue.append((new_state, next_clicks))
    return -1
