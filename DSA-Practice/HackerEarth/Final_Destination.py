"""
Problem: Final Destination
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/final-destination-cakewalk/
Date: 2026-08-27
Difficulty: Easy
Topic: Basic Programming, Implementation

Approach:
Read the move string and simulate final position on a 2D grid by
tracking (x, y) starting at origin. Each character updates one axis:
L/R shift x by -1/+1, U/D shift y by +1/-1. Print the final coordinates.

Time Complexity: O(n) — single pass over the move string
Space Complexity: O(1) — only two counters used (excluding input storage)
"""


# --------------------------- Solution ----------------------------------


import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    x, y = 0, 0
    for move in s:
        if move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
    print(f"{x} {y}")

if __name__ == '__main__':
    solve()
