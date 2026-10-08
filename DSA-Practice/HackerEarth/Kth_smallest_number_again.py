"""
Problem   : Kth Smallest Number Again
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/kth-smallest-number-again-2/
Difficulty: Medium
Topics    : Binary Search, Sorting
Date      : 2026-10-08

Approach:
    1. Sort the given ranges and merge overlapping/adjacent ones, so the
       result is a list of disjoint, ordered intervals.
    2. Build a prefix-sum array of interval sizes (cumulative count of
       numbers covered up to each interval).
    3. For each query K, binary search (bisect_left) the prefix array to find
       the interval containing the Kth smallest number, then compute it as
       start + (K - numbers_before_interval) - 1.
    4. If K is outside [1, total], the answer is -1.

Complexity (per test case, N ranges, Q queries):
    Time  : O(N log N + Q log N)  -> sorting + one binary search per query
    Space : O(N)                  -> merged ranges + prefix array
"""


# ----------------------------------- Solution ------------------------------------------------------


import sys
from bisect import bisect_left

def merge_ranges(ranges):
    ranges.sort()
    merged = []
    for a, b in ranges:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)
    return merged

def main():
    input = sys.stdin.buffer.readline
    T = int(input())
    for _ in range(T):
        N, Q = map(int, input().split())
        ranges = []
        for _ in range(N):
            A, B = map(int, input().split())
            ranges.append((A, B))
        merged = merge_ranges(ranges)
        prefix = []
        total = 0
        for a, b in merged:
            total += b - a + 1
            prefix.append(total)
        answers = []
        for _ in range(Q):
            K = int(input())
            if K < 1 or K > total:
                answers.append("-1")
                continue
            idx = bisect_left(prefix, K)
            previous = 0 if idx == 0 else prefix[idx - 1]
            a, b = merged[idx]
            answer = a + (K - previous) - 1
            answers.append(str(answer))
        sys.stdout.write("\n".join(answers) + "\n")

if __name__ == "__main__":
    main()
