"""
Problem: Missing Socks
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-18
Date Solved: 2026-09-10
Difficulty: Easy
Topics: Simulation, Math/Modular Arithmetic

Approach:
Start with pairs*2 individual socks. Simulate each wash cycle from 1
to `cycles`, applying the loss/gain rules based on divisibility
(lose 1 on multiples of 2, gain 1 on multiples of 3, lose 1 on
multiples of 5, gain 2 on multiples of 10). Clamp sock count at 0
after each cycle so it never goes negative, then return the number
of complete pairs at the end.

Time Complexity: O(cycles) - single loop over the cycle range
Space Complexity: O(1) - only a few scalar variables used
"""


# --------------------------- Solution -------------------------------------


def sock_pairs(pairs, cycles):
    socks = pairs * 2
    for cycle in range(1, cycles + 1):
        if cycle % 2 == 0:
            socks -= 1
        if cycle % 3 == 0:
            socks += 1
        if cycle % 5 == 0:
            socks -= 1
        if cycle % 10 == 0:
            socks += 2
        socks = max(0, socks)
    return socks // 2
