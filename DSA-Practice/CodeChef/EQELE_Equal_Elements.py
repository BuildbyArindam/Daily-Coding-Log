"""
Problem   : Equal Elements (EQELE)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/EQELE
Difficulty: 1718
Topics    : Greedy, Arrays
Date      : 2026-10-02

Approach:
    Greedy. Scan left to right and form a pair whenever the current element
    matches an earlier occurrence that lies after the end of the last chosen
    pair. Taking the earliest-finishing pair each time leaves the most room
    for later pairs, so the count is maximal. Tracking only the most recent
    index of each value gives the shortest candidate segment ending at i.
    Answer = 2 * (number of pairs).

Time Complexity : O(N) per test case
Space Complexity: O(N)
"""


# --------------------------------------- Solution ----------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        last = [-1] * (N + 1)
        end = -1
        pairs = 0
        for i, x in enumerate(A):
            if last[x] > end:
                pairs += 1
                end = i
            last[x] = i
        print(2 * pairs)

if __name__ == "__main__":
    solve()
