"""
Platform   : CodeChef
Problem    : Cursed Indices (CURSED)
Link       : https://www.codechef.com/problems/CURSED
Difficulty : 1803
Topics     : Greedy, Sorting, Prefix Sums
Date       : 2026-10-04

Approach:
    Sort ascending and build a prefix greedily. An element goes into the
    "good" group if it is strictly greater than the running sum of the good
    elements so far. Otherwise it goes into the "bad" group. Because the
    running sum only grows, every bad element stays bad wherever it sits
    after the good prefix, so appending all bad elements at the end gives
    the minimum count. Output len(bad), then good + bad.

Time  : O(N log N) per test case (sorting dominates)
Space : O(N)
"""


# --------------------------------------------- Solution -------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        A.sort()
        good = []
        bad = []
        total = 0
        for x in A:
            if x > total:
                good.append(x)
                total += x
            else:
                bad.append(x)
        print(len(bad))
        print(*(good + bad))

if __name__ == "__main__":
    solve()
