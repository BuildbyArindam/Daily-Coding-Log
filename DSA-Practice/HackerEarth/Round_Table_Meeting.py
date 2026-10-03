"""
Problem   : Round Table Meeting
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/the-graphic-game-59c30775/
Difficulty: Easy
Topics    : Algorithms, Binary Search, Searching
Date      : 2026-10-03

Approach:
  - Group the circular seating by university: map each university to its
    sorted list of seat indices.
  - For a query (x, y), iterate over the smaller position list and binary
    search (bisect_left) in the larger one to find the nearest y-seat on
    each side of every x-seat, wrapping around the circle (+N).
  - The minimum circular distance is halved (best // 2) for the answer.
  - If x == y the answer is 0.

Complexity:
  - Preprocessing: O(N) time, O(N) space.
  - Per query: O(m * log M) time, where m = min(cnt[x], cnt[y]) and
    M = max(cnt[x], cnt[y]); O(1) extra space.
  - Overall: O(N + Q * m * log M) time, O(N) space.
"""


# -------------------------------------- Solution -------------------------------------------------


import sys
from bisect import bisect_left
input = sys.stdin.readline
N, Q = map(int, input().split())
A = list(map(int, input().split()))
positions = {}
for i, university in enumerate(A):
    if university not in positions:
        positions[university] = []
    positions[university].append(i)

def get_answer(x, y):
    if x == y:
        return 0
    px = positions[x]
    py = positions[y]
    if len(px) > len(py):
        px, py = py, px
    best = N
    for p in px:
        k = bisect_left(py, p)
        if k < len(py):
            best = min(best, py[k] - p)
        else:
            best = min(best, py[0] + N - p)
        if k > 0:
            best = min(best, p - py[k - 1])
        else:
            best = min(best, p + N - py[-1])
    return best // 2
answer = []
for _ in range(Q):
    x, y = map(int, input().split())
    answer.append(str(get_answer(x, y)))
sys.stdout.write("\n".join(answer))
