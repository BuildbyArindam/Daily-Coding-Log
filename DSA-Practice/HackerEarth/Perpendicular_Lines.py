"""
Problem: Perpendicular Lines
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/sam-in-trouble-2-131edb9c/
Difficulty: Easy
Topic: Math

Approach:
For each test case, compute direction vectors of both lines:
  (dx1, dy1) = (x2 - x1, y2 - y1)
  (dx2, dy2) = (x4 - x3, y4 - y3)
Two lines are perpendicular iff their dot product is zero:
  dx1*dx2 + dy1*dy2 == 0
A line is INVALID if its two endpoints coincide (zero-length vector,
direction undefined).

Time Complexity:  O(T) - constant work per test case
Space Complexity: O(T) - only for storing output lines before printing

Date Solved: 2026-08-16
"""


# ---------------------- Solution -------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    idx = 1
    out = []
    for _ in range(T):
        x1, y1, x2, y2 = map(int, input_data[idx:idx+4])
        x3, y3, x4, y4 = map(int, input_data[idx+4:idx+8])
        idx += 8
        if (x1 == x2 and y1 == y2) or (x3 == x4 and y3 == y4):
            out.append("INVALID")
            continue
        dx1 = x2 - x1
        dy1 = y2 - y1
        dx2 = x4 - x3
        dy2 = y4 - y3
        if dx1 * dx2 + dy1 * dy2 == 0:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == '__main__':
    solve()
