"""
Problem: KillCode's Wish
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/killcodes-wish-2/
Date: 2026-08-24
Difficulty: Easy
Topic: Implementation

Approach:
For each element a[i], compute the number of rounds needed to reduce it
to <= 0 given a fixed decrement m per round: rounds = ceil(a[i] / m).
Track the index with the maximum rounds needed; on ties, keep the
latest (highest) index, since ">=" comparison always updates on tie.

Time Complexity: O(n) per test case
Space Complexity: O(n) for storing the array
"""


# ---------------------- Solution ----------------------------


import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    for _ in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr + 1])
        ptr += 2
        a = [int(x) for x in input_data[ptr:ptr + n]]
        ptr += n
        max_rounds = -1
        last_index = -1
        for i in range(n):
            rounds = (a[i] + m - 1) // m
            if rounds >= max_rounds:
                max_rounds = rounds
                last_index = i + 1 
        print(last_index)

if __name__ == "__main__":
    solve()
