"""
Problem: 3 Strikes
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-20
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Brute Force, Number Theory, String Manipulation

Approach:
    Iterate i from 1 to n, compute i*i, and check if the digit '3'
    appears anywhere in its string representation. Count all such i.

Time Complexity: O(n * d), where d = number of digits in i*i (effectively O(n))
Space Complexity: O(1) extra space (ignoring the temporary string per iteration)
"""


# ----------------------- Solution ------------------------------


def squares_with_three(n):
    count = 0
    for i in range(1, n + 1):
        square = i * i
        if '3' in str(square):
            count += 1
    return count
