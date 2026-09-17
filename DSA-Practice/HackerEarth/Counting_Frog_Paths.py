"""
Problem: Counting Frog Paths
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/counting-frog-paths-1abd84d5/
Date: 2026-09-17
Difficulty: Easy
Topics: Algorithms, Searching

Approach:
A frog starts at (X, Y) and can take up to `s` steps in the +x direction
and up to `s` steps in the +y direction (independently), landing anywhere
in the grid [X, X+s] x [Y, Y+s]. Count how many of those landing points
(x, y) satisfy x + y <= T by brute-force enumerating the (s+1) x (s+1) grid.

Time Complexity: O(s^2) — nested loop over the (s+1) x (s+1) grid
Space Complexity: O(1) — only a counter is used
"""


# --------------------------------- Solution -------------------------------------------


X, Y, s, T = map(int, input().split())
count = 0
for x in range(X, X + s + 1):
    for y in range(Y, Y + s + 1):
        if x + y <= T:
            count += 1
print(count)
