"""
Problem   : Digit sum (Interesting Number)
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/interesting-number-2-752e7fa2/
Difficulty: Easy
Topics    : Sorting, Greedy, Merge sort
Date      : 2026-10-23

Approach:
    Split the 2N digits into a left half and a right half and compare their sums.
    To close the gap with the fewest changes, only modify digits that help:
    lower a digit in the heavier half (gain = digit, set to 0), or raise a digit
    in the lighter half (gain = 9 - digit, set to 9). Compute the best possible
    gain for every position, sort the gains in descending order, and take the
    largest ones until the cumulative gain covers the gap. The number taken is
    the minimum number of changes.

Complexity:
    Time  : O(N log N), from sorting the 2N gains (O(N) possible with
            counting sort, since each gain is in 0..9)
    Space : O(N)
"""


# -------------------------------------------- Solution ------------------------------------------------------------


def solve(N, S):
    digits = [int(c) for c in S]
    first = sum(digits[:N])
    second = sum(digits[N:])
    gap = abs(first - second)
    if gap == 0:
        return 0
    gains = []
    for i in range(N):
        if first > second:
            gains.append(digits[i])
            gains.append(9 - digits[N + i])
        else:
            gains.append(9 - digits[i])
            gains.append(digits[N + i])
    gains.sort(reverse=True)
    reduced = 0
    for moves, gain in enumerate(gains, start=1):
        reduced += gain
        if reduced >= gap:
            return moves
    return len(gains)

T = int(input())

for _ in range(T):
    N = int(input())
    S = input().strip()

    out_ = solve(N, S)
    print(out_)
