"""
Problem   : Wave Sort
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/wave-sort_594?kunjiRedirection=true
Date      : 2026-08-30
Difficulty: Medium
Topics    : Arrays, Greedy, Sorting Simulation (Zigzag pattern)

Approach:
Single left-to-right pass. Maintain the wave property arr[0] >= arr[1] <= arr[2] >= arr[3]...
by comparing each element only with its immediate right neighbor:
  - At even index i: arr[i] should be >= arr[i+1] -> swap if smaller
  - At odd index i : arr[i] should be <= arr[i+1] -> swap if larger
Since each comparison only looks one step ahead and swaps are local,
one linear pass is enough to fix the whole array into wave form.

Time Complexity : O(n)  -- single pass, constant work per index
Space Complexity: O(1)  -- in-place swaps, no extra array
"""


# ------------------------- Solution ---------------------------------


from math import *
from collections import *
from sys import *
from os import *

n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 1):
    if i % 2 == 0:
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    else:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
print(*arr)
