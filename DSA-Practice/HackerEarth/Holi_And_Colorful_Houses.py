"""
Problem   : Holi And Colorful Houses
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/holi-and-colorful-houses-eb2049cb/
Difficulty: Easy
Topic     : Basic Programming, Implementation
Date      : 2026-08-19

Approach:
    Houses are arranged in a circle, each colored (string S).
    A "change" occurs at index i if S[i] != S[i-1].
    Precompute prefix[i] = number of changes in S[0..i] (linear, non-circular),
    plus total_changes = linear changes + wraparound change (S[N-1] vs S[0]).
    For each query (x, y):
        direct_cost = |prefix[x] - prefix[y]|  -> changes needed going the
                       "short way" through the linear segment
        answer = min(direct_cost, total_changes - direct_cost)
                 -> compares going one way around the circle vs the other

Complexity:
    Time  : O(N + Q) per test case (O(1) per query after O(N) prefix build)
    Space : O(N) for the prefix array
"""


# ---------------------- Solution --------------------------

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    T = int(next(iterator))
    out = []
    for _ in range(T):
        N = int(next(iterator))
        Q = int(next(iterator))
        S = next(iterator)
        pref = [0] * N
        for i in range(1, N):
            pref[i] = pref[i - 1] + (1 if S[i] != S[i - 1] else 0)
        wrap_around = 1 if S[N - 1] != S[0] else 0
        total_changes = pref[N - 1] + wrap_around
        for _ in range(Q):
            x = int(next(iterator)) - 1
            y = int(next(iterator)) - 1
            direct_cost = abs(pref[x] - pref[y])
            ans = min(direct_cost, total_changes - direct_cost)
            out.append(str(ans))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    solve()
