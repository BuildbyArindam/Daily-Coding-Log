"""
Problem: Good String
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/good-string-3/
Difficulty: Easy
Topics: Ad-Hoc, Basic Programming, Implementation
Date Solved: 2026-08-22

Approach:
A string is "good" only if every character in it is unique. To make the
given string good, we must delete all but one occurrence of each repeated
character. The minimum number of deletions needed equals the count of
characters minus the count of distinct characters (len(s) - len(set(s))),
since one occurrence of each distinct character can always be kept.

Time Complexity:  O(n)  -> single pass to build the set from the string
Space Complexity: O(k)  -> k = number of distinct characters (at most O(n))
"""


# --------------------------- Solution ----------------------------------


import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    ans = len(s) - len(set(s))
    print(ans)

if __name__ == "__main__":
    solve()
