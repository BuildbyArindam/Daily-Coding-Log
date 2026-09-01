"""
Problem   : Shell Game
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/35/A
Difficulty: *1000
Topic     : Implementation
Date      : 2026-09-01

Approach:
Track which cup index (0/1/2) currently holds the ball. For each of the
three swaps, if the tracked cup matches one of the two swapped positions,
update it to the other position; otherwise it's untouched.

Complexity:
Time  : O(1) — fixed 3 swaps regardless of input
Space : O(1) — constant extra storage
"""


# -------------------------- Solution ----------------------------


import os
import sys

if os.path.exists("input.txt"):
    with open("input.txt", "r") as f:
        data = f.read().split()
else:
    data = sys.stdin.read().split()
cup = int(data[0])
for i in range(1, 7, 2):
    a = int(data[i])
    b = int(data[i + 1])
    if cup == a:
        cup = b
    elif cup == b:
        cup = a
if os.path.exists("input.txt"):
    with open("output.txt", "w") as f:
        f.write(str(cup))
else:
    print(cup)
