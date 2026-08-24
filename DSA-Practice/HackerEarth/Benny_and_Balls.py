"""
Problem: Benny and Balls
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/benny-and-balls/
Date: 2026-08-24
Difficulty: Medium
Topic: Basic Programming, Implementation

Approach:
Simulate ball placement into N boxes using a pseudo-random index generator
(curr_x = (a * curr_x + b) % N). For each of T balls, increment the count
in the target box; when a box's count reaches its threshold p[i], count it
as an "opening" and reset that box to 0. Track total openings per query.

Time Complexity: O(N + T) per query — O(N) to read/init, O(T) to simulate
Space Complexity: O(N) per query — balls[] and p[] arrays
"""


# ------------------------- Solution ----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    Q = int(input_data[0])
    ptr = 1
    for _ in range(Q):
        N = int(input_data[ptr])
        ptr += 1
        p = [int(x) for x in input_data[ptr:ptr + N]]
        ptr += N
        x1 = int(input_data[ptr])
        a = int(input_data[ptr + 1])
        b = int(input_data[ptr + 2])
        t = int(input_data[ptr + 3])
        ptr += 4
        balls = [0] * N
        openings = 0
        curr_x = x1
        for step in range(t):
            if step > 0:
                curr_x = (a * curr_x + b) % N
            balls[curr_x] += 1
            if balls[curr_x] >= p[curr_x]:
                openings += 1
                balls[curr_x] = 0
        print(openings)

if __name__ == "__main__":
    solve()
