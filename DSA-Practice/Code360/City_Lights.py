"""
Problem     : City Lights
Platform    : Code360 (Naukri)
Link        : https://www.naukri.com/code360/problems/city-lights_5558693?kunjiRedirection=true
Difficulty  : Hard
Date solved : 2026-08-29

Approach:
For each light at position x with radius r, the light illuminates the wall
segment where the circle intersects the horizontal line at distance b — i.e.
the chord [2x - d, 2x + d] where d = sqrt(4r^2 - b^2) (lights with 2r < b
never reach the wall and are skipped; coordinates are doubled to avoid
fractions). Sort these intervals by left endpoint, then greedily apply the
classic "minimum intervals to cover a segment" sweep: repeatedly extend
coverage to the farthest reachable right endpoint among all intervals whose
left endpoint lies within the currently covered range. If no interval
extends the frontier, the wall can't be fully lit -> return -1.

Time complexity  : O(n log n)  — dominated by sorting the intervals
Space complexity : O(n)        — storage for the intervals list
"""


# ------------------------ Solution -------------------------------


from os import *
from sys import *
from collections import *
from math import *
from typing import *

import builtins
open = builtins.open

def cityLights(l: int, b: int, n: int, pos: List[int], r: List[int]) -> int:
    intervals = []
    for x, radius in zip(pos, r):
        if 2 * radius < b:
            continue
        d = sqrt(4 * radius * radius - b * b)
        left = 2 * x - d
        right = 2 * x + d
        intervals.append((left, right))
    if not intervals:
        return -1
    intervals.sort()
    target = 2 * l
    current = 0.0
    i = 0
    count = 0
    m = len(intervals)
    while current < target:
        farthest = current
        while i < m and intervals[i][0] <= current + 1e-12:
            if intervals[i][1] > farthest:
                farthest = intervals[i][1]
            i += 1
        if farthest <= current + 1e-12:
            return -1
        current = farthest
        count += 1
    return count
