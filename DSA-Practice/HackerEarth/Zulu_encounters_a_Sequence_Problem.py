"""
Problem: Zulu Encounters a Sequence Problem
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/zulu-encounters-a-sequence-problem/
Difficulty: Easy
Topics: Arrays, Data Structures, Implementation, One-dimensional
Date: 2026-08-29

Approach:
For each index i, find the farthest point of the nearest "break" in
monotonicity on both sides — i.e., the last index to the left (and first
index to the right) where the increasing/decreasing run relative to i
breaks. Precompute these boundaries with two prefix passes:
  L_inc[i], L_dec[i] -> leftmost index reachable via a non-decreasing /
                         non-increasing run ending at i
  R_inc[i], R_dec[i] -> rightmost index reachable via a non-decreasing /
                         non-increasing run starting at i
For each i, the maximum |A[i] - A[j]| achievable using only elements
within its monotonic run (left or right) is compared against the running
answer. Take the max over all i.

Time Complexity:  O(N) per test case (single pass for L arrays, single
                   pass for R arrays, single pass for the answer)
Space Complexity: O(N) per test case (four auxiliary arrays)
"""


# ---------------------------------- Solution ---------------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    test_cases = int(data[0])
    idx = 1
    out = []
    for _ in range(test_cases):
        N = int(data[idx])
        A = [int(x) for x in data[idx + 1 : idx + 1 + N]]
        idx += 1 + N
        if N <= 1:
            out.append(0)
            continue
        L_inc = [0] * N
        L_dec = [0] * N
        for i in range(N):
            if i == 0:
                L_inc[i] = 0
                L_dec[i] = 0
            else:
                L_inc[i] = L_inc[i - 1] if A[i - 1] <= A[i] else i
                L_dec[i] = L_dec[i - 1] if A[i - 1] >= A[i] else i
        R_inc = [0] * N
        R_dec = [0] * N
        for i in range(N - 1, -1, -1):
            if i == N - 1:
                R_inc[i] = N - 1
                R_dec[i] = N - 1
            else:
                R_inc[i] = R_inc[i + 1] if A[i] <= A[i + 1] else i
                R_dec[i] = R_dec[i + 1] if A[i] >= A[i + 1] else i
        max_points = 0
        for i in range(N):
            l1 = L_inc[i]
            l2 = L_dec[i]
            r1 = R_inc[i]
            r2 = R_dec[i]
            points_l = max(abs(A[i] - A[l1]), abs(A[i] - A[l2]))
            points_r = max(abs(A[i] - A[r1]), abs(A[i] - A[r2]))
            curr_points = max(points_l, points_r)
            if curr_points > max_points:
                max_points = curr_points
        out.append(max_points)
    print('\n'.join(map(str, out)))

if __name__ == '__main__':
    solve()
