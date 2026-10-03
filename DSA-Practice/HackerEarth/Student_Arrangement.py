"""
Problem   : Student Arrangement
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/student-arrangement-6/
Date      : 2026-10-03
Difficulty: Easy
Topics    : Basic programming, Binary search, Searching (solved with Union-Find)

Approach:
    Each student wants a preferred row. If that row is full, they take the
    next row with a free seat (wrapping around), otherwise they go unseated.
    A student counts toward the answer if they don't get their preferred row.
    Union-Find tracks the next non-full row:
      - The array is doubled (size 2M + 1) so wrap-around becomes a plain
        "move right" step, and index 2M acts as a sentinel for "no seat".
      - When a row reaches K students, both its copies (row, row + M) are
        linked to the next row, so later lookups skip it.
      - Path halving in find() keeps lookups near O(1).
    Once all M*K seats are taken, every remaining student is counted directly.

Time  : O(N * alpha(M)), roughly O(N)
Space : O(M)
"""


# --------------------------------------- Solution ----------------------------------------------------


import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
parent = list(range(2 * M + 1))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
occupied = [0] * M
answer = 0
seated = 0
for preferred in A:
    if seated == M * K:
        answer += 1
        continue
    p = preferred - 1 
    pos = find(p)
    if pos >= 2 * M:
        answer += 1
        continue
    row = pos % M
    if row != p:
        answer += 1
    occupied[row] += 1
    seated += 1
    if occupied[row] == K:
        parent[row] = find(row + 1)
        parent[row + M] = find(row + M + 1)
print(answer)
