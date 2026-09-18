"""
Problem: Scroll-a-palooza
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/scroll-a-palooza-bed5c880/
Date: 2026-09-18
Difficulty: Medium
Topics: Binary Search, Algorithms

Approach:
Compute prefix sums of daily scroll counts, then for each threshold
query w, find the earliest and latest day where |prefix| >= w. Sort
prefix positions by |value| descending and queries by threshold
descending, then sweep with a pointer so each query only admits the
positions that qualify, tracking min/max day index seen so far
(offline two-pointer / binary-search-on-threshold technique).
Values are bit-packed into integers for fast sort/compare.

Time Complexity: O(N log N + M log M) per test case (dominated by sorts)
Space Complexity: O(N + M)
"""


# ------------------------ Solution ----------------------------------


import sys
from array import array

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    output = []
    for _ in range(T):
        N = int(input())
        pos_shift = max(1, N.bit_length())
        pos_mask = (1 << pos_shift) - 1
        positions = []
        prefix = 0
        values = map(int, input().split())
        day = 1
        for x in values:
            prefix += x
            positions.append((abs(prefix) << pos_shift) | day)
            day += 1
        positions.sort(reverse=True)
        M = int(input())
        query_shift = max(1, M.bit_length())
        query_mask = (1 << query_shift) - 1
        queries = []
        for qid in range(M):
            w = int(input())
            queries.append((w << query_shift) | qid)
        queries.sort(reverse=True)
        answers = array('q', [-1]) * M
        ptr = 0
        min_day = N + 1
        max_day = 0
        for encoded_query in queries:
            w = encoded_query >> query_shift
            while ptr < N and (positions[ptr] >> pos_shift) >= w:
                day_index = positions[ptr] & pos_mask
                if day_index < min_day:
                    min_day = day_index
                if day_index > max_day:
                    max_day = day_index

                ptr += 1
            query_id = encoded_query & query_mask
            if max_day == 0:
                answers[query_id] = -1
            else:
                answers[query_id] = (min_day << pos_shift) | max_day
        for ans in answers:
            if ans == -1:
                output.append("-1")
            else:
                first_day = ans >> pos_shift
                last_day = ans & pos_mask
                output.append(f"{first_day} {last_day}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    solve()
