"""
Problem   : Monk's School
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/monks-school-4/
Date      : 2026-10-29
Difficulty: Easy
Topics    : Sorting, Hash Map

Approach  : Store each teacher's students in a dict (teacher -> list of
            (age, name) tuples). Sort teacher names lexicographically, then
            sort each teacher's list by age (ties broken by name) and print
            in that order. Output is built in a list and written once to
            keep I/O fast.

Time      : O(N log N + M log M), sorting N teachers and M students in total
Space     : O(N + M) for the dict and the output buffer
"""


# -------------------------------------------- Solution ---------------------------------------------------------------


import sys

def emit(lines):
    sys.stdout.write("\n".join(lines))
    sys.stdout.write("\n")

def main():
    tokens = sys.stdin.read().split()
    n, m = int(tokens[0]), int(tokens[1])
    roster = {}
    for t in tokens[2:2 + n]:
        roster[t] = []
    cursor = 2 + n
    for _ in range(m):
        boss = tokens[cursor]
        kid = tokens[cursor + 1]
        years = int(tokens[cursor + 2])
        roster[boss].append((years, kid))
        cursor += 3
    result = []
    for teacher in sorted(roster):
        result.append(teacher)
        for years, kid in sorted(roster[teacher]):
            result.append("%s %d" % (kid, years))
    emit(result)

if __name__ == "__main__":
    main()
