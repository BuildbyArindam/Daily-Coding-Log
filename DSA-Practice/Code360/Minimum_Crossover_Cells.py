"""
Problem: Minimum Crossover Cells
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/minimum-crossover-cells_3114803?kunjiRedirection=true
Difficulty: Medium
Topics: Arrays, Hashing / HashMap, Prefix Sum, Simulation
Date Solved: 2026-09-09

Approach:
Each row encodes a horizontal path as a sequence of column-deltas (row[0] = k,
followed by k-1 step values). Walking each row, we accumulate a running
`position` and, via a hashmap, count how many rows pass through each column
position after some step (a "boundary crossing" point). The row-set that
shares the most common boundary position can be aligned there without any
extra crossing cells, so the answer is n minus that maximum count.

Time Complexity:  O(S)  where S = total number of elements across all rows (sum of k_i)
Space Complexity: O(S)  for the boundary_count hashmap (at most S distinct positions)
"""


# ------------------------- Solution -------------------------------


from os import *
from sys import *
from collections import *
from math import *
from typing import List

def minimmumCrossedCells(n: int, mat: List[List[int]]) -> int:
    boundary_count = defaultdict(int)
    for row in mat:
        k = row[0]    
        position = 0
        for i in range(k - 1):
            position += row[i + 1]
            boundary_count[position] += 1
    max_boundary_rows = max(boundary_count.values(), default=0)
    return n - max_boundary_rows
