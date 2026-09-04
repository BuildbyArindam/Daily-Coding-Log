"""
Problem: Prateek and his Friends
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/very-cool-numbers/
Date: 2026-09-04
Difficulty: Easy
Topic: Ad-Hoc, Open

Approach:
Precompute a "coolness" score for every integer up to max R across all
queries, where coolness(x) = number of overlapping "101" substrings in
x's binary representation. Then build a 2D prefix-count table
prefix[k][x] = count of numbers in [1, x] with coolness >= k, so each
query (R, K) is answered in O(1) by a direct lookup.

Time complexity: O(max_R * max_cool) for building the prefix table,
                 O(1) per query, O(T) overall query answering
Space complexity: O(max_R * max_cool) for the prefix table
"""


# ------------------------ Solution -------------------------------


name = input()   
T = int(name)
queries = []
max_r = 0
for _ in range(T):
    R, K = map(int, input().split())
    queries.append((R, K))
    max_r = max(max_r, R)
coolness = [0] * (max_r + 1)
for x in range(1, max_r + 1):
    b = bin(x)[2:]
    count = 0
    for i in range(len(b) - 2):
        if b[i:i+3] == "101":
            count += 1
    coolness[x] = count
max_cool = max(coolness)
prefix = [[0] * (max_r + 1) for _ in range(max_cool + 1)]
for k in range(1, max_cool + 1):
    count = 0
    for x in range(1, max_r + 1):
        if coolness[x] >= k:
            count += 1
        prefix[k][x] = count
for R, K in queries:
    if K > max_cool:
        print(0)
    else:
        print(prefix[K][R])
