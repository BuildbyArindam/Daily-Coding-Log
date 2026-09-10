"""
Problem: Email Validator
Platform: FreeCodeCamp (Daily Coding Challenge #10-16)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-16
Difficulty: Easy–Medium
Related topics: Strings, String Parsing, Input Validation, Edge-Case Handling, Regular Expressions
Date Solved: 2026-09-10

Approach:
    Validate an email address using manual string parsing (no regex).
    - Reject if there isn't exactly one '@'.
    - Split into local and domain parts; reject if either is empty.
    - Local part must contain only letters, digits, '.', '_', '-'.
    - Local part can't start/end with '.', and no '..' allowed in local or domain.
    - Domain must contain a '.', and the substring after the last '.' (TLD)
      must be alphabetic, ASCII, and at least 2 characters long.

Time Complexity:  O(n) — single pass(es) over the string, n = len(email)
Space Complexity: O(n) — split() creates local/domain substrings
"""


# ----------------------------- Solution -------------------------------------


def validate(email):
    if email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not local or not domain:
        return False
    allowed_local = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"
    if any(char not in allowed_local for char in local):
        return False
    if local.startswith(".") or local.endswith("."):
        return False
    if ".." in local or ".." in domain:
        return False
    if "." not in domain:
        return False
    last_dot = domain.rfind(".")
    if last_dot == -1:
        return False
    tld = domain[last_dot + 1:]
    if len(tld) < 2 or not tld.isalpha() or not tld.isascii():
        return False
    return True
