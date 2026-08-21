"""
Problem: The Prime Cells
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/pythagorean-triangles-0158a4c5/
Difficulty: Easy
Topic: Basic Programming, Implementation
Date Solved: 2026-08-21

Approach:
For each cell in an N x N grid, sum the values of its valid orthogonal
neighbors (up/down/left/right, boundary-checked). Count how many of these
neighbor-sums are prime, using trial division up to sqrt(n).

Time Complexity: O(N^2 * sqrt(S)), where S is the max possible neighbor sum
                  (4 neighbors * max cell value) — primality check dominates.
Space Complexity: O(N^2) for storing the grid.
"""


# ---------------------------- Solution ------------------------------


import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    grid = []
    idx = 1
    for _ in range(n):
        grid.append([int(x) for x in data[idx:idx + n]])
        idx += n
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    prime_cell_count = 0
    for r in range(n):
        for c in range(n):
            neighbor_sum = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    neighbor_sum += grid[nr][nc]
            if is_prime(neighbor_sum):
                prime_cell_count += 1
    print(prime_cell_count)

if __name__ == '__main__':
    solve()
