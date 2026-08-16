"""
Problem   : Kth Character
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/kth-character-60eed906/
Difficulty: Easy
Topics    : Basic Programming, Implementation, String Manipulation
Date      : 2026-08-16

Approach:
    For each distinct character in the string, build a candidate string with
    ALL occurrences of that character removed. Among all these candidates,
    return the lexicographically smallest one.

Complexity:
    Time  : O(k * n)  where n = len(s), k = number of distinct characters
            (k <= 26 for lowercase letters, so effectively O(n))
    Space : O(n)  for each candidate string generated during comparison
"""


# ---------------------- Solution -------------------------


import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    unique_chars = set(s)
    smallest_string = None
    for char in unique_chars:
        candidate_string = s.replace(char, "")
        if smallest_string is None or candidate_string < smallest_string:
            smallest_string = candidate_string
    print(smallest_string)

if __name__ == "__main__":
    solve()
