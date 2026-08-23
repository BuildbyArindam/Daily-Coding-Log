"""
Problem: 2 Arrays
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/2-arrays-90c9019c/
Difficulty: Easy
Topic: 1-D Array, Arrays, Data Structures
Date Solved: 2026-08-23

Approach:
Two arrays a and b may each contain 0, 1, or 2 wildcard entries (-1),
representing unknown values that can be any non-negative integer.
- If both arrays have at least one -1: infinitely many assignments
  can equalize the sums -> "Infinite".
- If only one array has -1(s): compute the fixed sums and the
  required total 'diff' the wildcard(s) must cover.
    - 1 wildcard: exactly one way to hit an exact target if diff >= 0,
      else impossible.
    - 2 wildcards: diff can be split across two non-negative integers
      in (diff + 1) ways if diff >= 0, else 0 ways.
- If neither array has -1: sums are fixed, so count is implicitly 0
  or 1 (not explicitly handled in current code — see note below).

Time Complexity: O(n) — single pass to count -1s and sum remaining elements
Space Complexity: O(n) — storing arrays a and b
"""


# ----------------------- Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : n + 1]]
    b = [int(x) for x in input_data[n + 1 : 2 * n + 1]]
    count_a1 = a.count(-1)
    count_b1 = b.count(-1)
    sum_a = sum(x for x in a if x != -1)
    sum_b = sum(x for x in b if x != -1)
    if count_a1 > 0 and count_b1 > 0:
        print("Infinite")
    elif count_a1 > 0 and count_b1 == 0:
        diff = sum_b - sum_a
        if count_a1 == 1:
            print(1 if diff >= 0 else 0)
        elif count_a1 == 2:
            print(diff + 1 if diff >= 0 else 0)
    elif count_b1 > 0 and count_a1 == 0:
        diff = sum_a - sum_b
        if count_b1 == 1:
            print(1 if diff >= 0 else 0)
        elif count_b1 == 2:
            print(diff + 1 if diff >= 0 else 0)

if __name__ == "__main__":
    solve()
