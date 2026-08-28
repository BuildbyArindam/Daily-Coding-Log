"""
Problem   : Next Test
Link      : https://codeforces.com/problemset/problem/27/A
Date      : 2026-08-28
Difficulty: *1200
Topics    : Implementation, Sortings

Approach:
Read n and the set of test numbers already used. Scan integers from 1
to n+1 in order and print the first one not present in the set — that's
the smallest positive integer missing from the array, which is the next
free test number.

Time complexity : O(n) — set lookups are O(1) average, single pass up to n+1
Space complexity: O(n) — storing the input numbers in a set
"""


# -------------------------------- Solution -----------------------------------


n = int(input())
a = set(map(int, input().split()))

for i in range(1, n + 2):
    if i not in a:
        print(i)
        break
