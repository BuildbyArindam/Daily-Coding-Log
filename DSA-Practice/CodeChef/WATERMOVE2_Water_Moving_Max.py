"""
Problem   : Water Moving (Max)
Platform  : CodeChef (WATERMOVE2)
Link      : https://www.codechef.com/problems/WATERMOVE2
Date      : 2026-10-14
Difficulty: Easy
Topics    : Greedy, Sorting 

Approach  :
    Each operation lets one cup's water be merged into another, so K
    operations can combine at most K + 1 cups into a single cup. To
    maximise that cup, take the K + 1 largest amounts: sort descending
    and sum the top min(N, K + 1) values.

Time      : O(N log N) per test case (sorting)
Space     : O(N)
"""


# ------------------------------------------------- Solution ---------------------------------------------------------


import sys

def best_cup(amounts, ops):
    take = min(len(amounts), ops + 1)
    return sum(sorted(amounts, reverse=True)[:take])

def main():
    tokens = sys.stdin.read().split()
    ptr = 0
    tests = int(tokens[ptr])
    ptr += 1
    results = []
    while tests > 0:
        tests -= 1
        n = int(tokens[ptr])
        k = int(tokens[ptr + 1])
        ptr += 2
        cups = [int(x) for x in tokens[ptr:ptr + n]]
        ptr += n
        results.append(str(best_cup(cups, k)))
    print("\n".join(results))

main()
