"""
Problem   : The Final Quiz
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/
            basics-of-implementation/practice-problems/algorithm/the-bet-1-dbc1acde/
Date      : 2026-08-20
Difficulty: Easy
Topic     : Implementation, Ad-hoc, Difference Array

Approach:
    Alice's and Bob's true scores can range within [Y-A, Y+A] and [Z-B, Z+B]
    respectively (worst/best case at the interval endpoints). For every guess
    k in [0, X], we want to count how many of the 4 (alice, bob) extreme-value
    combinations k would "win against" -- i.e., k lies outside the band
    [X-M, M] where M = max(alice, bob) for that combination (mirrored around
    the range). Instead of testing each k against each of the 4 combos in
    O(X) per combo, we mark the valid ranges of winning k using a difference
    array, then sweep once over [0, X] to find the k with the maximum
    win-count (best_k), breaking ties by the smallest k.

Complexity:
    Time  : O(T * X)   -- 4 constant-size interval updates + one O(X) sweep per test case
    Space : O(X)        -- diff array of size X + 2
"""


# --------------------------- Solution -------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        X, Y, Z = map(int, input().split())
        A, B = map(int, input().split())
        diff = [0] * (X + 2)
        alice_scores = [Y - A, Y + A]
        bob_scores = [Z - B, Z + B]
        def add_interval(l, r):
            if l <= r:
                diff[l] += 1
                diff[r + 1] -= 1
        for alice in alice_scores:
            for bob in bob_scores:
                M = max(alice, bob)
                l = max(0, M - X + 1)
                r = X
                add_interval(l, r)
                l = 0
                r = min(X, X - M - 1)
                add_interval(l, r)
        best_k = 0
        best_count = -1
        current = 0
        for k in range(X + 1):
            current += diff[k]
            if current > best_count:
                best_count = current
                best_k = k
        print(best_k)

if __name__ == "__main__":
    solve()
