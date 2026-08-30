"""
Problem: Fibonacci Sequence
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-13
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Arrays, Iteration, Math, Sequence Generation

Approach:
Given a starting sequence and a target length, extend the sequence by
repeatedly summing the last two elements until the desired length is
reached. Uses the seed values already provided (start_sequence) instead
of hardcoding 0 and 1, making it a generalized Fibonacci-style generator.

Time Complexity: O(n) — one append operation per element until length is reached
Space Complexity: O(n) — stores the full output sequence
"""


# --------------------------- Solution ---------------------------------


def fibonacci_sequence(start_sequence, length):
    if length == 0:
        return []
    sequence = start_sequence[:length]
    while len(sequence) < length:
        sequence.append(sequence[-2] + sequence[-1])
    return sequence
