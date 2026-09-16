# Problem: Golden rectangles
# Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/almost-golden-rectangular-1c9d72c0/
# Date: 2026-09-16
# Difficulty: Easy 
# Topic: Algorithms, Searching
# Approach: Normalize each rectangle so w >= h, then check whether
#           1.6 <= w/h <= 1.7 using integer arithmetic:
#           16*h <= 10*w <= 17*h.
# Time: O(n)
# Space: O(n) due to storing all input; O(1) auxiliary space.


# --------------------------- Solution --------------------------------------


import sys
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
count = 0
for i in range(n):
    w = data[2 * i + 1]
    h = data[2 * i + 2]
    if w < h:
        w, h = h, w
    if 16 * h <= 10 * w <= 17 * h:
        count += 1
print(count)
