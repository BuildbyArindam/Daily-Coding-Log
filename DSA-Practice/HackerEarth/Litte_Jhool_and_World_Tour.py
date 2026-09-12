"""
Problem   : Little Jhool and World Tour
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/litte-jhool-and-world-tour-1/
Difficulty: Hard
Topic     : Data Structures, Arrays, 1-D

Date Solved: 2026-09-12

Approach:
    Treat the N positions as a circular track. Each (X, Y) range is
    "unrolled" onto a doubled line: if X <= Y it's split into two
    copies (X, Y) and (X+N, Y+N); if it wraps (X > Y) it becomes a
    single interval (X, Y+N). This lets circular coverage be checked
    with a linear sweep instead of handling wraparound explicitly.

    After sorting intervals by start, sweep position by position
    (current), pushing the end-points of all intervals starting at
    `current` onto a min-heap. At each position, pop the interval
    with the earliest end — if that end is already before `current`,
    no live interval covers this position, so full coverage fails.
    Early exit if M > N, since you can't cover N points with fewer
    than N interval-starts in the worst case.

Time Complexity : O(M log M) for sorting + O(N log M) for the sweep
                   (each of the ~2N positions does O(log M) heap work)
                   => O((N + M) log M) per test case
Space Complexity: O(M) for the intervals list and heap
"""


# ------------------------- Solution --------------------------------


import sys
import heapq

def possible(N, ranges):
    M = len(ranges)
    if M > N:
        return False
    intervals = []
    for X, Y in ranges:
        if X <= Y:
            intervals.append((X, Y))
            intervals.append((X + N, Y + N))
        else:
            intervals.append((X, Y + N))
    intervals.sort()
    heap = []
    i = 0
    current = 0
    total = len(intervals)
    while True:
        if not heap:
            if i == total:
                break
            current = intervals[i][0]
        while i < total and intervals[i][0] == current:
            end = intervals[i][1]
            heapq.heappush(heap, end)
            i += 1
        earliest_end = heapq.heappop(heap)
        if current > earliest_end:
            return False
        current += 1
    return True

def main():
    input = sys.stdin.readline
    tc = int(input())
    for _ in range(tc):
        N, M = map(int, input().split())
        ranges = []
        for _ in range(M):
            X, Y = map(int, input().split())
            ranges.append((X, Y))
        print("YES" if possible(N, ranges) else "NO")

if __name__ == "__main__":
    main()
