"""
Problem: Nonogram Validator
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-07
Date Solved: 2026-08-30
Difficulty: Easy-Medium
Topics: Arrays / String-like Sequence Processing / Simulation / Pattern Validation / Run-Length Encoding

Approach:
Scan the row of cells left to right, counting consecutive runs of filled
cells (1s). Whenever a run of 1s ends (a 0 is hit or the array ends),
push the run length into a groups list. Compare the resulting groups
list against the given clue list — a match means the row satisfies
the nonogram clue.

Time Complexity: O(n)  — single pass over the cells list
Space Complexity: O(k) — k = number of groups found (worst case n/2)
"""


# ------------------------ Solution --------------------------------


def is_valid_nonogram(clue, cells):
    groups = []
    count = 0
    for cell in cells:
        if cell == 1:
            count += 1
        elif count > 0:
            groups.append(count)
            count = 0
    if count > 0:
        groups.append(count)
    return clue == groups
