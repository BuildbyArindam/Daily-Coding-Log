"""
Problem   : Incense Sticks and Fragrance
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/hydrogen-bomb-c4096642/
Difficulty: Easy
Topic     : Mathematics (Geometry / Binary Search)
Date      : 2026-08-16

Approach:
Two incense sticks burn outward simultaneously from (x1,y1) and (x2,y2) at
unit speed. A point (x,y) is "fragranced" only once BOTH sticks' smoke has
reached it, i.e. at time = max(dist_to_stick1, dist_to_stick2). Compute this
arrival time for all N points, sort them, then for each query time t, binary
search (bisect_right) for how many points have arrival time <= t.

Time Complexity : O(N log N + Q log N)
                  - O(N) to compute distances, O(N log N) to sort
                  - O(log N) per query via bisect_right, O(Q log N) total
Space Complexity: O(N) for storing arrival times
"""


# ------------------------ Solution -------------------------


import sys
import math
from bisect import bisect_right

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    x1, y1 = int(input_data[0]), int(input_data[1])
    x2, y2 = int(input_data[2]), int(input_data[3])
    N = int(input_data[4])
    idx = 5
    x_coords = [int(x) for x in input_data[idx: idx + N]]
    idx += N
    y_coords = [int(y) for y in input_data[idx: idx + N]]
    idx += N
    Q = int(input_data[idx])
    idx += 1
    queries = [int(q) for q in input_data[idx: idx + Q]]
    req_times = []
    for i in range(N):
        x, y = x_coords[i], y_coords[i]
        dist1 = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        dist2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
        req_times.append(max(dist1, dist2))
    req_times.sort()
    out = []
    for t in queries:
        ans = bisect_right(req_times, t)
        out.append(str(ans))
    print(" ".join(out))

if __name__ == '__main__':
    solve()
