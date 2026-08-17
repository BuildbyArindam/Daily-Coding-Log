"""
Problem: Plus Plus
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/plus-plus-60bcac48/
Difficulty: Easy
Topic: Basic Programming, Implementation, Array/Grid Handling
Date Solved: 2026-08-17

Approach:
- For every interior cell (r, c) with 1 <= r <= n-2, 1 <= c <= m-2, form a
  "plus" shape: the cell itself plus its 4 orthogonal neighbors.
- Store each plus as (set of its 5 coordinates, list of its 5 values).
- Check every pair of pluses; if their coordinate sets are disjoint
  (no shared cell), compute the element-wise dot product of their value
  lists and track the maximum.

Time Complexity: O(P^2) where P = (n-2) * (m-2) is the number of valid
  pluses -> each pair comparison is O(1) for the disjoint check (5-element
  sets) and O(5) for the dot product, so effectively O(P^2).
Space Complexity: O(P) to store all plus coordinate sets and value lists.
"""


# -------------------- Solution --------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    grid = []
    idx = 2
    for _ in range(n):
        grid.append([int(x) for x in input_data[idx:idx+m]])
        idx += m
    pluses = []
    for r in range(1, n - 1):
        for c in range(1, m - 1):
            coords = {
                (r, c),
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1)
            }
            vals = [
                grid[r][c],
                grid[r - 1][c],
                grid[r + 1][c],
                grid[r][c - 1],
                grid[r][c + 1]
            ]
            pluses.append((coords, vals))
    max_sum = 0
    num_pluses = len(pluses)
    for i in range(num_pluses):
        coords1, vals1 = pluses[i]
        for j in range(i + 1, num_pluses):
            coords2, vals2 = pluses[j]
            if coords1.isdisjoint(coords2):
                current_sum = sum(vals1[k] * vals2[k] for k in range(5))
                if current_sum > max_sum:
                    max_sum = current_sum   
    print(max_sum)

if __name__ == '__main__':
    solve()
