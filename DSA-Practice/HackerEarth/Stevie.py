"""
Problem   : Stevie
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/stevie/
Difficulty: Easy
Topic     : Maps
Date      : 2026-08-21

Approach:
    For each unique value in array A, track the maximum corresponding value
    in array B using a hash map (val_a -> max val_b seen so far). Then, for
    every element in A, output the max B-value mapped to it.

Time Complexity : O(N)  -> single pass to build map, single pass to build result
Space Complexity: O(N)  -> hash map storing up to N unique keys
"""


# ---------------------- Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : n + 1]]
    b = [int(x) for x in input_data[n + 1 : 2 * n + 1]]
    max_b = {}
    for val_a, val_b in zip(a, b):
        if val_a not in max_b or val_b > max_b[val_a]:
            max_b[val_a] = val_b
    result = [str(max_b[val]) for val in a]
    print(' '.join(result))

if __name__ == '__main__':
    solve()
