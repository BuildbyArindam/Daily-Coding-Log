"""
Problem   : Reverse Parenthesis
Platform  : FreeCodeCamp — Daily Coding Challenge
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/08-26
Date      : 2026-08-26
Difficulty: Medium
Topics    : Stack, String Manipulation, Parsing

Approach:
Use a stack to handle nested parentheses. Maintain a `current` string buffer.
On '(': push current buffer onto stack, reset current to "".
On ')': reverse current, then prepend the popped stack value (the string
built before this nesting level) to the reversed result.
On any other char: append to current.
Net effect: each level of nesting gets reversed exactly once, and nested
reversals cancel out correctly due to the stack-based composition.

Time complexity : O(n^2) worst case — repeated slicing/reversal (current[::-1])
                  and string concatenation can each cost O(n), done up to n times.
                  (O(n) amortized in practice for typical inputs; O(n^2) worst-case
                  for deeply nested parentheses.)
Space complexity: O(n) — stack holds partial strings, current buffer holds up to n chars.
"""


# ------------------------ Solution ---------------------------


def decode(s):
    stack = []
    current = ""
    for char in s:
        if char == "(":
            stack.append(current)
            current = ""
        elif char == ")":
            current = current[::-1]
            current = stack.pop() + current
        else:
            current += char
    return current
