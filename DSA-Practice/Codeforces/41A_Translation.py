"""
Problem: Translation
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/41/A
Date Solved: 2026-09-08
Difficulty: *800
Topics: Implementation, Strings

Approach:
Read strings s and t. t is a valid "translation" of s iff t equals s
reversed (Petya's language reads words backwards). Compare t against
s[::-1] directly and print YES/NO.

Time Complexity: O(n) — single string reversal and comparison
Space Complexity: O(n) — storage for the reversed string
"""


# --------------------- Solution ---------------------------


s = input()
t = input()

if s[::-1] == t:
    print("YES")
else:
    print("NO")
