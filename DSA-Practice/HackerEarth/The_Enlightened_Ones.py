"""
Problem   : The Enlightened Ones
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/the-enlightened-ones/
Difficulty: Medium
Topics    : Binary Search, Sorting, Greedy
Date      : 2026-10-08

Approach:
    Binary search on the answer (minimum radius). For a given radius, a monk
    covers a segment of length 2 * radius. After sorting positions, greedily
    start a new segment at the first uncovered position and skip everything
    within positions[i] + 2 * radius. If the number of segments needed is <= K,
    the radius is feasible. Feasibility is monotonic in the radius, so search
    the range [0, max - min] for the smallest feasible value.

Complexity:
    Time : O(N log N + N log D), where D = max(positions) - min(positions)
    Space: O(N) for the positions list (sorted in place)
"""


# ---------------------------------------------- Solution ---------------------------------------------------------


N, K = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()

def can_cover(radius):
    monks = 0
    i = 0
    while i < N:
        monks += 1
        cover_until = positions[i] + 2 * radius
        i += 1
        while i < N and positions[i] <= cover_until:
            i += 1
        if monks > K:
            return False
    return True

low = 0
high = positions[-1] - positions[0]
while low < high:
    mid = (low + high) // 2
    if can_cover(mid):
        high = mid
    else:
        low = mid + 1

print(low)
