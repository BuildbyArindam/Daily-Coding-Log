"""
Problem   : Car Names
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/car-names-4/
Difficulty: Easy
Topics    : Ad-Hoc, Approved, Implementation, Open
Date      : 2026-09-04

Approach:
  A car name is "OK" only if its length is a non-zero multiple of 3 and it
  splits into three equal-length blocks, where each block consists of a
  single repeated character, and all three characters are pairwise distinct.
  Read N names, check each condition directly (length%3==0, len>=3, each
  third is homogeneous via set(), and no two thirds share a character),
  print "OK"/"Not OK" accordingly.

Time complexity : O(N * L)  — L = length of each string, single pass per string
Space complexity: O(L)      — for slicing/sets per string, no extra structures
"""


# ----------------------- Solution -------------------------------


name = input()                  # Reading input from STDIN
N = int(name)
for _ in range(N):
    s = input().strip()
    if len(s) < 3:
        print("Not OK")
        continue
    if len(s) % 3 != 0:
        print("Not OK")
        continue
    n = len(s) // 3
    first = s[:n]
    second = s[n:2 * n]
    third = s[2 * n:]
    if (len(set(first)) == 1 and
        len(set(second)) == 1 and
        len(set(third)) == 1 and
        first[0] != second[0] and
        second[0] != third[0] and
        first[0] != third[0]):
        print("OK")
    else:
        print("Not OK")
