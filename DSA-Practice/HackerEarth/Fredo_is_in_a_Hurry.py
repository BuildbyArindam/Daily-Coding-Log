"""
Problem   : Fredo is in a Hurry
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/fredo-is-in-a-hurry/
Difficulty: Easy
Topics    : Ad-Hoc, Basic Programming
Date      : 2026-08-24

Approach:
    Fredo can either take the stairs (visiting all N floors, cost = N*(N+1)/2
    since he stops at every floor 1..N one at a time) or use the elevator for
    some suffix of floors. Find the largest x such that stopping at floors
    1..x by stairs plus using the elevator for the remaining (N-x) floors
    minimizes total cost. The break-even point is derived by solving
    x^2 + 3x <= 2N (from equating stair cost up to x with elevator cost
    savings), found via isqrt with a small correction loop, then compare
    full-stairs cost vs the hybrid (stairs up to x + elevator for the rest).
    Answer = min(full stairs cost, stairs-to-x + elevator-for-rest).

Complexity:
    Time  : O(1) per test case (isqrt + O(1) correction steps) -> O(T) overall
    Space : O(1)
"""


# -------------------------- Solution ---------------------------


import math

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        d = math.isqrt(9 + 8 * N)
        x = (d - 3) // 2
        while (x + 1) * (x + 1) + 3 * (x + 1) <= 2 * N:
            x += 1
        while x * x + 3 * x > 2 * N:
            x -= 1
        stairs = N * (N + 1) // 2
        elevator = 2 * (N - x)
        print(min(stairs, elevator))

if __name__ == "__main__":
    solve()
