"""
Problem: Spelling Check
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/39/J
Difficulty: *1500
Topics: Hashing, Implementation, Strings
Date Solved: 2026-09-06

Approach:
Grow matching prefix and suffix pointers between s and t (t is s with one
letter possibly changed). Any mismatch must be confined to a single
contiguous block that lies strictly between the matched prefix and matched
suffix. Compute that block's bounds (left = m-1-suffix, right = prefix);
if left > right, no valid single-letter-change position exists (s == t or
edit distance > 1) — print 0. Otherwise every index in [left, right] is a
valid position where s[i] could have been the misspelling — print all of
them.

Time Complexity: O(m + n) — two linear scans to grow prefix/suffix pointers.
Space Complexity: O(1) extra (excluding output list).
"""


# ------------------------ Solution -----------------------------


import sys

def solve():
    input = sys.stdin.readline
    s = input().strip()
    t = input().strip()
    m = len(s)
    n = len(t)
    prefix = 0
    while prefix < n and s[prefix] == t[prefix]:
        prefix += 1
    suffix = 0
    while suffix < n and s[m - 1 - suffix] == t[n - 1 - suffix]:
        suffix += 1
    left = m - 1 - suffix
    right = prefix
    if left > right:
        print(0)
        return
    ans = range(left + 1, right + 2)
    print(right - left + 1)
    print(*ans)

if __name__ == "__main__":
    solve()
