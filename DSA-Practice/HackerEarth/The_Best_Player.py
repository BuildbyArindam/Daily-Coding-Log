"""
Problem   : The Best Player
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/the-best-player-1/
Difficulty: Easy
Topics    : Sorting, Brute Force, Bubble Sort, Basic Programming
Date      : 2026-10-16

Approach:
    Read all players as (name, score) pairs. Sort them with a custom
    comparator: higher score first, and on equal scores, lexicographically
    smaller name first. Print the names of the first K players.

Complexity:
    Time  : O(N log N) for the sort (plus O(N) input parsing)
    Space : O(N) to store the roster
"""


# --------------------------------------------------- Solution ----------------------------------------------------


import sys
from functools import cmp_to_key

def compare(a, b):
    if a[1] != b[1]:
        return -1 if a[1] > b[1] else 1
    if a[0] != b[0]:
        return -1 if a[0] < b[0] else 1
    return 0

def main():
    tokens = sys.stdin.read().split()
    limit = int(tokens[1])
    total = int(tokens[0])
    roster = []
    pos = 2
    for _ in range(total):
        roster.append((tokens[pos], int(tokens[pos + 1])))
        pos += 2
    roster.sort(key=cmp_to_key(compare))
    out = []
    for idx in range(limit):
        out.append(roster[idx][0])
    print("\n".join(out))

main()
