"""
Problem   : Longest Palindrome (LONGPALI)
Platform  : CodeChef (ZCO/INOI practice, IARCSJUD)
Link      : https://www.codechef.com/practice/course/zco-inoi-problems/IARCSJUD/problems/LONGPALI
Date      : 2026-10-21
Difficulty: Hard
Topics    : Strings, Palindromes, Manacher's Algorithm

Approach:
    Manacher's algorithm. Interleave the string with '#' and wrap it in
    sentinels ('^' ... '$') so every palindrome has odd length and the
    expansion loop needs no bounds checks. rad[k] is the palindrome radius
    centred at k, which equals its length in the original string.
    Keep the rightmost palindrome (mid, edge) and reuse the mirrored radius
    rad[2*mid - k] to skip redundant comparisons. The longest radius gives
    the answer, and start = (centre - radius) // 2 maps it back to the
    original string.

Complexity:
    Time : O(n)  (each expansion extends 'edge', so total work is linear)
    Space: O(n)
"""


# -------------------------------------------- Solution ------------------------------------------------------------


import sys

def solve():
    tokens = sys.stdin.read().split()
    word = tokens[-1]
    pad = ['^', '#']
    for ch in word:
        pad.append(ch)
        pad.append('#')
    pad.append('$')
    size = len(pad)
    rad = [0] * size
    mid = 0
    edge = 0
    for k in range(1, size - 1):
        if k < edge:
            rad[k] = min(edge - k, rad[2 * mid - k])
        while pad[k + rad[k] + 1] == pad[k - rad[k] - 1]:
            rad[k] += 1
        if k + rad[k] > edge:
            mid = k
            edge = k + rad[k]
    longest = 0
    where = 0
    for k in range(size):
        if rad[k] > longest:
            longest = rad[k]
            where = k
    begin = (where - longest) // 2
    sys.stdout.write(str(longest) + "\n" + word[begin:begin + longest] + "\n")

if __name__ == "__main__":
    solve()
