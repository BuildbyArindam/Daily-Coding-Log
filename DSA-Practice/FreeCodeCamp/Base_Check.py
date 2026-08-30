# Problem: Base Check
# Platform: FreeCodeCamp — Daily Coding Challenge (08-12)
# Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-12
# Date: 2026-08-30
# Difficulty: Easy
# Topics: String Manipulation, Number Bases, Validation
#
# Approach:
#   Validate that a base is in [2, 36] and that every character in the
#   input string is a legal digit for that base. Build the canonical
#   digit set "0-9A-Z" and check each (uppercased) char falls within
#   the first `base` characters of that set.
#
# Time Complexity:  O(n) — n = len(n), one pass with a substring/set membership check per char
# Space Complexity: O(1) — fixed-size 36-character digit string


# -------------------------- Solution ---------------------------------


def is_valid_number(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return base >= 2 and base <= 36 and all(ch.upper() in digits[:base] for ch in n)
