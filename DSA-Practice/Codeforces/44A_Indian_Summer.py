"""
Problem: Indian Summer
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/44/A
Date Solved: 2026-09-11
Difficulty: *900
Topic: Implementation

Approach:
Read n (species, color) pairs and insert each as a tuple into a set.
Since sets only keep unique elements, duplicate leaves collapse
automatically. The answer is just the size of the set.

Time Complexity: O(n) - single pass, O(1) avg. set insert/lookup
Space Complexity: O(n) - storing up to n unique tuples in the set
"""


# --------------------------- Solution --------------------------------


n = int(input())

leaves = set()
for _ in range(n):
    species, color = input().split()
    leaves.add((species, color))
print(len(leaves))
