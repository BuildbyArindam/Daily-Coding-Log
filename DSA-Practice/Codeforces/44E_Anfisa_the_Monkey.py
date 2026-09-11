"""
Problem: Anfisa the Monkey
Link: https://codeforces.com/problemset/problem/44/E
Platform: Codeforces
Difficulty: *1400
Topic: DP / Greedy
Date solved: 2026-09-11

Approach:
Split a string of length n into exactly k lines, each of length
between a and b characters, choosing each line's length greedily
as large as possible (up to b) while leaving enough characters
for the remaining lines to each have at least a characters.

Time Complexity: O(n)  — single pass over the string
Space Complexity: O(n) — storing/printing substrings
"""


# ---------------------------- Solution ----------------------------------


k, a, b = map(int, input().split())
s = input()
n = len(s)
if n < k * a or n > k * b:
    print("No solution")
else:
    pos = 0
    for i in range(k):
        remaining_lines = k - i - 1
        remaining_chars = n - pos
        length = min(b, remaining_chars - remaining_lines * a)
        print(s[pos:pos + length])
        pos += length
