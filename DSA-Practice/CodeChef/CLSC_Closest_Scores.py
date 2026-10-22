"""
Platform   : CodeChef
Problem    : Closest Scores (CLSC)
Link       : https://www.codechef.com/problems/CLSC
Difficulty : 1050
Topics     : Sorting, Arrays, Brute Force, Algorithms
Date       : 2026-10-22

Approach:
    The minimum absolute difference between any two values is always
    between two neighbours in sorted order. Sort the scores, then scan
    adjacent pairs and keep the smallest gap.

Complexity:
    Time  : O(N log N), dominated by the sort; the scan is O(N)
    Space : O(N) for the sorted copy
"""


# ----------------------------------------------- Solution -------------------------------------------------------


import sys

def smallest_gap(values):
    ordered = sorted(values)
    best = float("inf")
    prev = ordered[0]
    for cur in ordered[1:]:
        gap = cur - prev
        if gap < best:
            best = gap
        prev = cur
    return best

def main():
    tokens = sys.stdin.read().split()
    count = int(tokens[0])
    marks = list(map(int, tokens[1:1 + count]))
    print(smallest_gap(marks))

if __name__ == "__main__":
    main()
