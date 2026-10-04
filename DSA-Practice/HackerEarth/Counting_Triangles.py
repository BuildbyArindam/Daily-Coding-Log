"""
Problem   : Counting Triangles
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/counting-triangles/
Date      : 2026-10-04
Difficulty: Easy
Topics    : Hashing, Hash Maps, Sorting

Approach:
    Two triangles are the same if their side lengths match in any order.
    Sort each triangle's sides to get a canonical form, count occurrences
    with a hash map, then count the triangles whose form appears exactly once.

Complexity:
    Time : O(n)  (sorting 3 elements is O(1) per triangle; hash map ops are O(1) average)
    Space: O(n)  (stores up to n canonical triples)
"""


# ---------------------------------------- Solution ------------------------------------------


from collections import Counter
n = int(input())
triangles = []
for _ in range(n):
    a, b, c = map(int, input().split())
    triangles.append(tuple(sorted((a, b, c))))
freq = Counter(triangles)
answer = sum(1 for count in freq.values() if count == 1)
print(answer)
