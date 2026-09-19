"""
Problem: Cover Line
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/cover-points-37bf8bb9/
Date Solved: 2026-09-19
Difficulty: Medium
Topics: Greedy, Binary Search, Sorting

Approach:
Binary search on the answer (max allowed segment weight). For a given
weight cap, use a greedy interval-covering sweep (like the classic
"minimum number of intervals to cover a line" check) restricted to
segments with weight <= cap, to see if [1, n] can be fully covered.
Binary search over weight values to find the minimum cap that still
allows full coverage.

Time Complexity: O(m log m) for sorting + O(m log(max_weight)) for the
                 binary search (each feasibility check is O(m))
Space Complexity: O(m) for storing segments
"""


# ------------------------------------ Solution --------------------------------------------


import sys

def can_cover(n, segments, max_weight):
    """
    Check whether [1, n] can be completely covered
    using only segments with weight <= max_weight.
    """
    reach = 0
    i = 0
    m = len(segments)
    while reach < n:
        best = reach
        while i < m and segments[i][0] <= reach + 1:
            l, r, w = segments[i]
            if w <= max_weight and r > best:
                best = r
            i += 1
        if best == reach:
            return False
        reach = best
    return True

def main():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    segments = []
    for _ in range(m):
        l, r, w = map(int, input().split())
        segments.append((l, r, w))
    segments.sort(key=lambda x: x[0])
    if not can_cover(n, segments, 10**9):
        print(-1)
        return
    low = 1
    high = max(w for _, _, w in segments)
    while low < high:
        mid = (low + high) // 2
        if can_cover(n, segments, mid):
            high = mid
        else:
            low = mid + 1
    print(low)

if __name__ == "__main__":
    main()
