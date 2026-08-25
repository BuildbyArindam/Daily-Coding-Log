"""
Problem: String Sum
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/string-sum/
Difficulty: Easy
Topic: Implementation
Date: 2026-08-25

Approach:
Read the input string and sum the "weight" of each lowercase letter,
where weight = (position in alphabet, a=1 ... z=26). Print the total.

Time Complexity: O(n)  — single pass over the string
Space Complexity: O(1) — only an accumulator, ignoring input storage
"""


# -------------------------- Solution -----------------------------


import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    total_weight = sum(ord(char) - ord('a') + 1 for char in s)
    print(total_weight)

if __name__ == '__main__':
    solve()
