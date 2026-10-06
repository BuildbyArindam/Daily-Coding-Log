"""
Problem   : Rolling Balls
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/rolling-balls-b8923a50/
Date      : 2026-10-06
Difficulty: Medium
Topics    : Algorithms, Binary Search, Searching

Approach  :
  - Balls that collide just swap identities, so the set of positions at time t
    is the same as if every ball passed through the others. We only need the
    p-th smallest position, not which ball is where.
  - Each ball bounces between walls 0 and M = L-1, which is movement on a
    circle of length 2M. After time t, the right-movers (and left-movers) split
    into at most two runs: balls still travelling in their initial direction,
    and balls that have bounced. Within a run, position is a linear function
    (slope +1 or -1) of the sorted starting position.
  - Per query, binary search on the answer x in [0, M]. count_leq(x) uses
    bisect on each run (at most 4) to count balls at position <= x.
    The smallest x with count >= p is the answer (+1 to convert back to
    1-indexed).

Complexity: O(log M * log n) per query, O(q * log M * log n) overall.
            Space O(n) (the runs only store slices/indices of the input arrays).

Assumption: the starting positions are given in sorted order (bisect relies on it).
"""


# ----------------------------------------- Solution ------------------------------------------------


import sys
from bisect import bisect_left, bisect_right

def build_runs(arr, v, t, M):
    if not arr:
        return []
    period = 2 * M
    r = (v * t) % period
    runs = []
    if r < M:
        turn = M - r
        cut = bisect_left(arr, turn)
        if cut > 0:
            runs.append((arr, 0, cut, 1, r))
        if cut < len(arr):
            runs.append((arr, cut, len(arr), -1, period - r))
    else:
        turn = period - r
        cut = bisect_left(arr, turn)
        if cut > 0:
            runs.append((arr, 0, cut, -1, period - r))
        if cut < len(arr):
            runs.append((arr, cut, len(arr), 1, r - period))
    return runs

def solve_query(M, left_moving, right_moving, t, p):
    runs = []
    runs.extend(build_runs(right_moving, 1, t, M))
    runs.extend(build_runs(left_moving, -1, t, M))
    def count_leq(x):
        total = 0
        for arr, lo, hi, slope, c in runs:
            if slope == 1:
                total += bisect_right(arr, x - c, lo, hi) - lo
            else:
                total += hi - bisect_left(arr, c - x, lo, hi)
        return total
    low = 0
    high = M
    while low < high:
        mid = (low + high) // 2
        if count_leq(mid) >= p:
            high = mid
        else:
            low = mid + 1
    return low + 1

def main():
    input = sys.stdin.readline
    L, n, q = map(int, input().split())
    s = list(map(int, input().split()))
    d = list(map(int, input().split()))
    M = L - 1
    left_moving = []
    right_moving = []
    for pos, direction in zip(s, d):
        a = pos - 1
        if direction == 0:
            left_moving.append(a)
        else:
            right_moving.append(a)
    answer = []
    for _ in range(q):
        t, p = map(int, input().split())
        answer.append(str(solve_query(M, left_moving, right_moving, t, p)))
    sys.stdout.write("\n".join(answer))

if __name__ == "__main__":
    main()
