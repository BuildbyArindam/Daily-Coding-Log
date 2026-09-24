"""
Problem   : Minimum Maximum Plants
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/minimum-maximum-plants-7fc77039/
Difficulty: Hard
Topics    : Multi-dimensional Arrays, Data Structures
Date      : 2026-09-24

Approach:
    Each broken cell splits its row into independent runs of consecutive
    usable cells, so every run of length L can be solved on its own:
      - Maximum plants in a run = ceil(L / 2)  -> (L + 1) // 2
      - Minimum plants in a run = ceil(L / 3)  -> (L + 2) // 3
    Rows with no broken cells are one run of length m, so they are counted
    in O(1) as a group instead of being scanned.
    For rows with broken cells, sort the broken columns and read off the gaps
    between them (and the tail after the last one). Sum over all runs.

Complexity:
    Time  : O(n + B log B), where B is the number of broken cells
            (sorting columns within each affected row)
    Space : O(B) for the row -> broken-columns map
"""


# ------------------------------------------------ Solution -------------------------------------------------


import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    total_tokens = len(data)
    def next_int(default=0):
        nonlocal idx
        if idx < total_tokens:
            val = int(data[idx])
            idx += 1
            return val
        return default
    n = next_int()
    m = next_int()
    b = next_int()
    broken = {}
    pairs_read = 0
    while pairs_read < b and idx + 1 < total_tokens:
        i = next_int()
        j = next_int()
        pairs_read += 1
        if 0 <= i < n and 0 <= j < m:
            if i not in broken:
                broken[i] = set()
            broken[i].add(j)
    total_max = 0
    total_min = 0
    rows_with_broken = set(broken.keys())
    count_no_broken = n - len(rows_with_broken)
    if count_no_broken > 0:
        total_max += count_no_broken * ((m + 1) // 2)
        total_min += count_no_broken * ((m + 2) // 3)
    for row, cols in broken.items():
        sorted_cols = sorted(cols)
        prev = -1
        runs = []
        for c in sorted_cols:
            length = c - prev - 1
            if length > 0:
                runs.append(length)
            prev = c
        length = m - prev - 1
        if length > 0:
            runs.append(length)
        for L in runs:
            total_max += (L + 1) // 2
            total_min += (L + 2) // 3
    print(total_max, total_min)

if __name__ == "__main__":
    main()
