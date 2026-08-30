"""
Problem: Unnatural Prime
Platform: FreeCodeCamp - Daily Coding Challenge (08-23)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-23
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Number Theory, Primality Testing, Math

Approach:
    Take the absolute value of n (to handle negative inputs, since
    primality is normally undefined for negatives - hence "unnatural").
    Numbers less than 2 are not prime. Otherwise, trial-divide from 2
    up to sqrt(n); if any divisor is found, n is not prime.

Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""


# --------------------------- Solution --------------------------------


def is_unnatural_prime(n):
    n = abs(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
