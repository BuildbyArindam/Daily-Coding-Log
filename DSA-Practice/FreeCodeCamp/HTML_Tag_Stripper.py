# Problem: HTML Tag Stripper
# Platform: FreeCodeCamp (Daily Coding Challenge #10-15)
# Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-15
# Date Solved: 2026-09-10
# Difficulty: Easy
# Topics: Regular Expressions, String Manipulation, HTML/Text Parsing, Pattern Matching
# Approach: Use a regex pattern `<[^>]*>` to match any substring starting with
#           '<', followed by any characters that aren't '>', ending with '>',
#           and replace all such matches with an empty string.
# Time Complexity: O(n) — single linear scan of the input string by the regex engine
# Space Complexity: O(n) — new string created for the result


# ---------------------------- Solution --------------------------------


import re
def strip_tags(html):
    return re.sub(r'<[^>]*>', '', html)
