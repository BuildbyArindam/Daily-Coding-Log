"""
Problem: Candy in the Box
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/candy-in-the-box-75b63839/
Platform: HackerEarth
Date: 2026-09-10
Difficulty: Easy
Topic: Observation, Linear Search, Math

Approach:
The candy bounces back and forth between position 1 and N, so the
sequence of positions repeats with period (2N - 2). For a given
turn K, reduce K-1 modulo the period to find where in the cycle we
are. If that offset is less than N, the candy is on its way "up"
(position = offset + 1). Otherwise it's on its way "back down"
(position = period - offset + 1).

Time Complexity: O(1) per query, O(T) overall
Space Complexity: O(1)
"""


# --------------------------- Solution -----------------------------------


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    period = 2 * N - 2
    pos = (K - 1) % period
    if pos < N:
        answer = pos + 1
    else:
        answer = period - pos + 1
    print(answer)
