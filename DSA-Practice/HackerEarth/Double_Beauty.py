"""
Problem   : Double Beauty
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/double-beauty-711a7ca1/
Difficulty: Easy
Topics    : Greedy, Sorting
Date      : 2026-11-22

Approach:
    Greedy. Each chosen element contributes twice, so the total is maximized
    by taking the k largest values. Use a heap-based nlargest(k) instead of a
    full sort, then double the sum.

Complexity (per test case):
    Time  : O(n log k)
    Space : O(k) extra for the heap (O(n) for the input array)
"""


# ------------------------------------------ Solution ------------------------------------------------------


import sys
from heapq import nlargest

def best_beauty(values, k):
    return sum(nlargest(k, values)) * 2

def run():
    tokens = sys.stdin.read().split()
    results = []
    pos = 1
    for _ in range(int(tokens[0])):
        n, k = int(tokens[pos]), int(tokens[pos + 1])
        pos += 2
        arr = list(map(int, tokens[pos:pos + n]))
        pos += n
        results.append(str(best_beauty(arr, k)))
    sys.stdout.write("\n".join(results) + "\n")

run()
