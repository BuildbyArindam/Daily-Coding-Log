"""
Problem   : Help Mrinmay
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/help-mrinmay/
Difficulty: Easy
Topics    : Strings, Frequency Count
Date      : 2026-09-10

Approach:
    Build a frequency count (26 letters) of the main string.
    For each query string, count required letters and check if the
    required count of any letter exceeds what's available in the main
    string's frequency array. If any letter's demand exceeds supply,
    the query is impossible ("NO"), otherwise it's possible ("YES").
    This is essentially a subset/multiset-containment check.

Time complexity : O(S + sum(Q_i))  -> S = len(main string), Q_i = len(each query)
Space complexity: O(1) extra       -> fixed-size 26-length frequency arrays
"""


# --------------------------- Solution ----------------------------------


import sys
input = sys.stdin.readline
Str = input().strip()
freq = [0] * 26
for ch in Str:
    freq[ord(ch) - ord('a')] += 1
N = int(input())
answers = []
for _ in range(N):
    query = input().strip()
    needed = [0] * 26
    possible = True
    for ch in query:
        idx = ord(ch) - ord('a')
        needed[idx] += 1
        if needed[idx] > freq[idx]:
            possible = False
            break
    answers.append("YES" if possible else "NO")
sys.stdout.write("\n".join(answers))
