"""
Problem: P@ssw0rd Str3ngth!
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-03
Date Solved: 2026-09-09
Difficulty: Easy
Topics: String Manipulation, Conditional Logic, Rule-Based Validation

Approach:
Check the password against 4 independent rules (length >= 8, mixed case,
contains a digit, contains a special character from a fixed set) and count
how many rules pass. Bucket the count into weak (<2), medium (2-3), or
strong (4) categories.

Time Complexity: O(n) - each rule scans the password once (n = password length)
Space Complexity: O(1) - only boolean/counter variables, no extra structures
"""


# -------------------------- Solution ---------------------------------


def check_strength(password):
    length_ok = len(password) >= 8
    mixed_case = any(c.isupper() for c in password) and any(c.islower() for c in password)
    number_ok = any(c.isdigit() for c in password)
    special_ok = any(c in "!@#$%^&*" for c in password)
    rules_met = sum([length_ok, mixed_case, number_ok, special_ok])
    if rules_met < 2:
        return "weak"
    elif rules_met < 4:
        return "medium"
    else:
        return "strong"
