"""
Problem: Image Smoothing
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/image-smoothing-3/
Difficulty: Easy
Date Solved: 2026-08-22

Approach:
For each pixel (i, j) in the n x n grid, apply a (2m+1) x (2m+1) convolution
filter centered at that pixel. For every filter offset (p, q), check that the
corresponding grid cell (i+p, j+q) lies within bounds; if so, add
grid[i+p][j+q] * filter_mask[p+m][q+m] to the pixel's output value.
Out-of-bounds filter positions are simply skipped (treated as 0 contribution).

Time Complexity: O(n^2 * m^2) - for each of n^2 pixels, we scan a
                  (2m+1) x (2m+1) filter window.
Space Complexity: O(n^2 + m^2) - grid storage plus filter mask storage
                  (output list is O(n^2) as well).
"""


# -------------------------- Solution ------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    idx = 0
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    idx += 2
    filter_size = 2 * m + 1
    filter_mask = []
    for _ in range(filter_size):
        filter_mask.append([int(x) for x in input_data[idx : idx + filter_size]])
        idx += filter_size
    grid = []
    for _ in range(n):
        grid.append([int(x) for x in input_data[idx : idx + n]])
        idx += n
    output = []
    for i in range(n):
        row = []
        for j in range(n):
            pixel_val = 0
            for p in range(-m, m + 1):
                for q in range(-m, m + 1):
                    r, c = i + p, j + q
                    if 0 <= r < n and 0 <= c < n:
                        pixel_val += grid[r][c] * filter_mask[p + m][q + m]
            row.append(str(pixel_val))
        output.append(" ".join(row))
    print("\n".join(output))

if __name__ == "__main__":
    solve()
