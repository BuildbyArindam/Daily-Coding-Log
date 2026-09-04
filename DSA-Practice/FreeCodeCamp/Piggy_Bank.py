"""
Problem: Piggy Bank
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-22
Date Solved: 2026-09-04
Difficulty: Easy
Topics: Hashing, Dictionary Lookup, Basic Math, String Formatting

Approach:
Read coin counts from the input dict via .get() with a default of 0 (handles
missing keys safely), convert each coin type to cents using its known value,
sum to get total_cents, then split into dollars (// 100) and cents (% 100).
Format the result as a dollar string with cents zero-padded to 2 digits.

Time Complexity: O(1) — fixed number of dict lookups and arithmetic ops
Space Complexity: O(1) — constant extra space
"""


# ----------------------- Solution -------------------------------


def piggy_bank(coins):
    pennies = coins.get("pennies", 0)
    nickels = coins.get("nickels", 0)
    dimes = coins.get("dimes", 0)
    quarters = coins.get("quarters", 0)
    total_cents = (
        pennies * 1 +
        nickels * 5 +
        dimes * 10 +
        quarters * 25
    )
    dollars = total_cents // 100
    cents = total_cents % 100
    return f"${dollars}.{cents:02d}"
