"""
Problem: Spam Detector
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-27
Date Solved: 2026-09-07
Difficulty: Medium
Topics: Regex, String Parsing, Pattern Matching, Validation Logic

Approach:
Use a regex to parse the phone number into its components (country
code, area code, and the two groups of the local number). If the
format doesn't match, it isn't spam by this rule. Then run through a
series of independent spam-indicator checks: an invalid/malformed
country code, an out-of-range area code, the digit-sum of the first
three digits appearing inside the last four digits, and four or more
repeated consecutive digits anywhere in the number. If any rule
triggers, flag it as spam.

Time Complexity: O(n) — regex parsing and digit scanning are linear
                  in the length of the number string
Space Complexity: O(n) — for the extracted groups and the
                  digits-only string
"""


# --------------------------- Solution -----------------------------------


import re
def is_spam(number):
    match = re.fullmatch(r"\+(\d+) \((\d{3})\) (\d{3})-(\d{4})", number)
    if not match:
        return False
    country_code, area_code, first_three, last_four = match.groups()
    if len(country_code) > 2 or not country_code.startswith("0"):
        return True
    area = int(area_code)
    if area > 900 or area < 200:
        return True
    digit_sum = sum(int(digit) for digit in first_three)
    if str(digit_sum) in last_four:
        return True
    digits_only = re.sub(r"\D", "", number)
    if re.search(r"(\d)\1{3,}", digits_only):
        return True
    return False
