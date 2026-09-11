"""
Problem   : Letter
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/43/B
Difficulty: *1100
Date Solved: 2026-09-11
Topics    : Implementation, Strings

Approach:
    Count the frequency of each letter (ignoring spaces) available in the
    newspaper heading (s1). Then, for every letter required in the message
    (s2, ignoring spaces), check if it's still available in the counter and
    decrement it. If any required letter runs out, print "NO" and stop;
    otherwise print "YES".

Complexity:
    Time  : O(N + M), where N = len(s1), M = len(s2)
    Space : O(1) — at most 26 lowercase letters stored in the Counter
"""


# ----------------------------- Solution ----------------------------------


from collections import Counter
s1 = input()
s2 = input()
available = Counter(c for c in s1 if c != ' ')
for c in s2:
    if c == ' ':
        continue
    if available[c] == 0:
        print("NO")
        break
    available[c] -= 1
else:
    print("YES")
