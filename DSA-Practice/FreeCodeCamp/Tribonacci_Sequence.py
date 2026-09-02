"""
Problem: Tribonacci Sequence
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-01
Date: 2026-09-02
Difficulty: Easy
Topics: Math, Dynamic Programming (Tabulation), Sequence Generation, Array Manipulation

Approach:
Start with the given seed values (start_sequence) and iteratively build up
the sequence by summing the previous three elements, until it reaches the
target length. Uses bottom-up tabulation — no recursion, no extra memo
structure since the array itself acts as the DP table.

Time Complexity: O(n) — one pass to generate remaining terms, where n = length
Space Complexity: O(n) — output list grows to size length (O(1) extra if
                   input/output isn't counted)
"""


# ------------------------- Solution --------------------------------


def tribonacci_sequence(start_sequence, length):
    if length == 0:
        return []
    sequence = start_sequence[:length]
    while len(sequence) < length:
        sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
    return sequence
