"""
Problem   : Print HackerEarth
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/print-hackerearth/
Difficulty: Easy
Topic     : Basic Programming
Date      : 2026-08-25

Approach:
Count frequency of each character in the string. To form the word
"hackerearth", each occurrence needs: h, c, k, t (once each) and
a, e, r (twice each, since they appear twice in "hackerearth").
The number of times we can fully form the word is limited by whichever
letter runs out first, so the answer is the minimum over:
    count[a]//2, count[e]//2, count[h]//2, count[r]//2,
    count[c], count[k], count[t]

Time Complexity : O(n) — single pass to build the Counter, n = len(s)
Space Complexity: O(1) — Counter has at most 26 lowercase letter keys
"""


# ----------------------- Solution --------------------------


import sys
from collections import Counter

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    s = data[1] if len(data) > 1 else ""
    counts = Counter(s)
    possible_words = [
        counts['a'] // 2,
        counts['e'] // 2,
        counts['h'] // 2,
        counts['r'] // 2,
        counts['c'] // 1,
        counts['k'] // 1,
        counts['t'] // 1
    ]
    print(min(possible_words))

if __name__ == '__main__':
    solve()
