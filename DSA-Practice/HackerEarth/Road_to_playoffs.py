"""
Problem: Road to Playoffs
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/road-to-playoffs-4e5d8318/
Date Solved: 2026-09-21
Difficulty: Hard
Topics: Binary Search, Greedy, Prefix Sums

Approach:
    For each team, determine if it's possible for that team to still finish
    among the top K teams after all remaining matches (each worth M points)
    are played, given B remaining matches per team.
    - Sort teams by current score, build a prefix sum array for quick range
      sums.
    - For each team, binary search for the boundary where a team's current
      score + max possible gain (M) would surpass it (unavoidable overtakes).
      If more than (B - 1) teams can unavoidably overtake it, it's eliminated.
    - Otherwise, use binary search + prefix sums to compute the minimum
      points needed to secure a top-K rank, and compare against the max
      points obtainable in remaining matches (M * (N - K)).

Time Complexity:  O(N log N) per test case (sorting + binary search per team)
Space Complexity: O(N) for the sorted array and prefix sum array
"""


# ------------------------------------- Solution ------------------------------------------


import sys
from bisect import bisect_right

def solve():
    input = sys.stdin.readline
    T = int(input())
    answers = []
    for _ in range(T):
        N, M, K, B = map(int, input().split())
        X = list(map(int, input().split()))
        teams = sorted((x, idx) for idx, x in enumerate(X))
        a = [x for x, _ in teams]
        pref = [0] * (N + 1)
        for i in range(N):
            pref[i + 1] = pref[i] + a[i]
        L = N - B
        limit = M * (N - K)
        possible = 0
        for pos, (x, original_idx) in enumerate(teams):
            target = x + M
            first_greater = bisect_right(a, target)
            unavoidable = N - first_greater
            if unavoidable > B - 1:
                continue
            if pos < L:
                r = L + 1
            else:
                r = L
            p1 = bisect_right(a, x, 0, r)
            p2 = bisect_right(a, target, 0, r)
            middle_sum = pref[p2] - pref[p1]
            middle_count = p2 - p1
            large_count = r - p2
            required = (
                middle_sum
                - middle_count * x
                + large_count * M
            )
            if required <= limit:
                possible += 1
        answers.append(str(possible))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    solve()
