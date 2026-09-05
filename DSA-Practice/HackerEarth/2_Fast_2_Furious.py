"""
Problem: 2 Fast 2 Furious
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/2-fast-2-furious/
Difficulty: Easy
Topics: Ad-Hoc, Basic Programming, Implementation
Date Solved: 2026-09-05

Approach:
Read speed sequences for Dom and Brian. For each, compute the maximum
absolute difference between consecutive speed readings — this represents
their biggest single "jump" in speed. Whoever has the larger max jump wins
(printed with that max value); equal max jumps -> "Tie".

Time Complexity: O(n) — single pass over both arrays
Space Complexity: O(n) — storing the two input lists
"""


# --------------------------- Solution ----------------------------------


import sys
n = int(input())
dom = list(map(int, input().split()))
brian = list(map(int, input().split()))
dom_max = 0
brian_max = 0
for i in range(1, n):
    dom_change = abs(dom[i] - dom[i - 1])
    brian_change = abs(brian[i] - brian[i - 1])
    if dom_change > dom_max:
        dom_max = dom_change
    if brian_change > brian_max:
        brian_max = brian_change
if dom_max > brian_max:
    print("Dom")
    print(dom_max)
elif brian_max > dom_max:
    print("Brian")
    print(brian_max)
else:
    print("Tie")
    print(dom_max)
