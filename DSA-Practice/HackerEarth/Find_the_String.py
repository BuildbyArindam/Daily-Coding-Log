"""
Problem   : Find the String
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/find-the-string-4014dec6/
Date      : 2026-09-25
Difficulty: Easy
Topics    : Arrays, Data Structures, String Manipulation

Approach:
  - Build a character-frequency Counter for each row of the grid.
  - For each index i in the target string, the required row is i % n
    (characters are drawn cyclically across the n rows).
  - Check whether that row's counter still has the needed character
    available; if yes, consume it, else the string can't be formed.
  - If every character is satisfied, output "Yes", otherwise "No".

Time Complexity : O(N*M + T*L)  — N*M to build row counters, T*L to
                  scan the target string across T test cases (L = len).
Space Complexity: O(N*26)       — one frequency counter per row.
"""


# ---------------------------------------------- Solution ---------------------------------------------------


import sys
from collections import Counter

def read_ints():
    return map(int, sys.stdin.readline().split())

def build_row_counters(rows, n, m):
    counters = []
    for r in range(n):
        row_chars = rows[r]
        counters.append(Counter(row_chars))
    return counters

def can_form_string(target, counters, n):
    for idx, ch in enumerate(target):
        row_idx = idx % n
        bucket = counters[row_idx]
        if bucket[ch] > 0:
            bucket[ch] -= 1
        else:
            return False
    return True

def process_case():
    n, m = read_ints()
    grid_rows = []
    for _ in range(n):
        line = sys.stdin.readline().strip()
        grid_rows.append(line)
    target_string = sys.stdin.readline().strip()
    row_counters = build_row_counters(grid_rows, n, m)
    result = can_form_string(target_string, row_counters, n)
    return "Yes" if result else "No"

def main():
    t = int(sys.stdin.readline())
    outputs = []
    for _ in range(t):
        outputs.append(process_case())
    print("\n".join(outputs))

if __name__ == "__main__":
    main()
