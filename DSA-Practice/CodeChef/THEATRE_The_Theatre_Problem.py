"""
Problem   : The Theatre Problem (THEATRE)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/THEATRE
Difficulty: 1719
Date      : 2026-10-02
Topics    : Brute Force, Permutations, Implementation

Approach:
    Each of the 4 movies (A-D) is assigned to exactly one of the 4 show
    times (12, 3, 6, 9), and each show time gets a distinct ticket price
    (25, 50, 75, 100). That gives only 4! movie assignments x 4! price
    assignments = 576 combinations per test case, so brute force works.
    Count requests per (movie, time) pair, then for every combination sum
    people * price per slot, or subtract 100 for an empty slot. The best
    value is the answer for the test case. The final line is the sum of
    all test-case answers.

Complexity (per test case):
    Time  : O(N + 4! * 4! * 4) = O(N), since the 576 * 4 term is constant
    Space : O(1), a fixed 4x4 count table
"""


# ------------------------------------- Solution --------------------------------------------------


import sys
from itertools import permutations

def solve():
    input = sys.stdin.readline
    T = int(input())
    total_profit = 0
    movies = ['A', 'B', 'C', 'D']
    times = [12, 3, 6, 9]
    prices = [25, 50, 75, 100]
    idx_movie = {m: i for i, m in enumerate(movies)}
    idx_time = {t: i for i, t in enumerate(times)}
    for _ in range(T):
        N = int(input())
        cnt = [[0] * 4 for _ in range(4)]
        for _ in range(N):
            m, t = input().split()
            m = m.strip()
            t = int(t)
            cnt[idx_movie[m]][idx_time[t]] += 1
        best = -10**18
        for movie_perm in permutations(range(4)):
            for price_perm in permutations(prices):
                profit = 0
                for time_idx in range(4):
                    movie_idx = movie_perm[time_idx]
                    people = cnt[movie_idx][time_idx]
                    if people == 0:
                        profit -= 100
                    else:
                        profit += people * price_perm[time_idx]
                best = max(best, profit)
        print(best)
        total_profit += best
    print(total_profit)

if __name__ == "__main__":
    solve()
