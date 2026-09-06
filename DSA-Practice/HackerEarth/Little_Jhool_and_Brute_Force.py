"""
Problem   : Little Jhool and Brute Force
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/little-jhool-and-brute-force-18/
Difficulty: Easy
Topics    : Approved, Basic Programming, Brute-force search, Open
Date      : 2026-09-06

Approach:
    A number N is "nice" if it can be written as a^3 + b^3 in at least
    two distinct ways (1 <= a <= b). Precompute all sums of two cubes up
    to the maximum query value, count how many (a,b) pairs produce each
    sum, and keep only sums with >= 2 ways. Sort these valid sums, then
    for each query binary-search for the largest valid sum <= N (or -1
    if none exists).

Complexity:
    Let L = cube root of MAX_N (the largest limit for a, b).
    Time : O(L^2 log L) to build+sort the candidate sums,
           O(Q log L^2) for Q binary-searched queries.
    Space: O(L^2) worst case for the `count` dict of sums.
"""


# --------------------------- Solution ---------------------------------


import sys
from bisect import bisect_left
name = input()   
t = int(name)
queries = [int(input()) for _ in range(t)]
MAX_N = max(queries)
limit = 1
while (limit + 1) ** 3 <= MAX_N:
    limit += 1
count = {}
cubes = [i ** 3 for i in range(limit + 1)]
for a in range(1, limit + 1):
    for b in range(a, limit + 1):
        s = cubes[a] + cubes[b]
        if s > MAX_N:
            break
        count[s] = count.get(s, 0) + 1
valid = sorted(s for s, ways in count.items() if ways >= 2)
out = []
for n in queries:
    idx = bisect_left(valid, n)
    if idx == 0:
        out.append("-1")
    else:
        out.append(str(valid[idx - 1]))
sys.stdout.write("\n".join(out))
