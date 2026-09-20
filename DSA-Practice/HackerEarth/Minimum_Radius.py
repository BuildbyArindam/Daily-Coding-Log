"""
Problem: Minimum Radius
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/minimum-radius-2-29df5cb3/
Date Solved: 2026-09-20
Difficulty: Medium
Topics: Binary Search, Algorithms

Approach:
Compute squared distance (to avoid floating point) of each point from origin,
then sort points by that squared distance. Greedily accumulate people (A[i])
in increasing order of distance until the cumulative count reaches p. The
answer radius is the ceiling of sqrt of the distance at which the threshold
is met (using integer sqrt with a correction step instead of math.sqrt to
avoid precision errors). If total people < p, answer is -1.

Time Complexity: O(N log N) per test case (dominated by sort)
Space Complexity: O(N)
"""


# ---------------------------------- Solution ---------------------------------------------


import sys
import math

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, p = map(int, input().split())
        X = list(map(int, input().split()))
        Y = list(map(int, input().split()))
        A = list(map(int, input().split()))
        if p == 0:
            print(0)
            continue
        points = []
        total = 0
        for i in range(N):
            d2 = X[i] * X[i] + Y[i] * Y[i]
            points.append((d2, A[i]))
            total += A[i]
        if total < p:
            print(-1)
            continue
        points.sort()
        current = 0
        answer = 0
        i = 0
        while i < N:
            d2 = points[i][0]
            while i < N and points[i][0] == d2:
                current += points[i][1]
                i += 1
            if current >= p:
                answer = math.isqrt(d2)
                if answer * answer < d2:
                    answer += 1
                break
        print(answer)

if __name__ == "__main__":
    solve()
