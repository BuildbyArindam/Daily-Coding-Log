"""
Problem   : Modify Sequence
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/modify-sequence/
Date      : 2026-09-12
Difficulty: Easy
Topic     : Ad-Hoc, Basic Programming

Approach:
    Simulate a running transformation over the array: starting from prev = 0,
    compute current = a[i] - prev for each element (except the last). If any
    current value goes negative, the sequence can't be validly "reduced", so
    the answer is immediately NO. Otherwise, carry current forward as the new
    prev. Finally, check that the last element of the array matches the last
    computed prev value — this confirms the sequence is consistent end-to-end.

Time complexity : O(n)  — single pass over the array
Space complexity: O(1)  — excluding O(n) for storing the input list itself
"""


# ---------------------------- Solution ----------------------------------


n = int(input())
a = list(map(int, input().split()))
prev = 0
possible = True
for i in range(n - 1):
    current = a[i] - prev
    if current < 0:
        possible = False
        break
    prev = current
if possible and a[n - 1] != prev:
    possible = False
print("YES" if possible else "NO")
