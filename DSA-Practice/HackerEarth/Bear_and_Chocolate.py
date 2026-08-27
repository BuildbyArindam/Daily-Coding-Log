"""
Problem: Bear and Chocolate
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/bear-and-chocolate/
Difficulty: Easy
Topics: Approved, Implementation, Open
Date Solved: 2026-08-27

Approach:
Count total cherries ('#') in the N x N grid. If the count is odd, an
equal split is impossible -> "NO". Otherwise compute target = total/2
and check if a running row-wise prefix sum hits target exactly at some
row boundary (a valid horizontal cut), or failing that, a running
column-wise prefix sum hits target at some column boundary (a valid
vertical cut). If either exists, the grid can be split into two equal
halves -> "YES", else "NO".

Time Complexity: O(N^2) per test case (grid scan + row/col prefix sums)
Space Complexity: O(N^2) to store the grid
"""


# ------------------------ Solution ------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        grid = []
        for _ in range(N):
            grid.append(data[idx])
            idx += 1
        total_cherries = sum(row.count('#') for row in grid)
        if total_cherries % 2 != 0:
            out.append("NO")
            continue
        target = total_cherries // 2
        possible = False
        running_sum = 0
        for row in grid:
            running_sum += row.count('#')
            if running_sum == target:
                possible = True
                break
        if not possible:
            running_sum = 0
            for col in range(N):
                running_sum += sum(1 for row in range(N) if grid[row][col] == '#')
                if running_sum == target:
                    possible = True
                    break
        out.append("YES" if possible else "NO")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
