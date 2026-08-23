"""
Problem: Decode String
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/decode-string_696319?kunjiRedirection=true
Date: 2026-08-23
Difficulty: Easy
Topics: Stack, String

Approach:
Traverse the string, accumulating digits into `count` and characters into
`current`. On '[', push the current (string, count) state onto the stack
and reset both. On ']', pop the last saved state and expand: the string
built so far gets repeated `repeat_count` times and appended to the
previously saved prefix. Non-bracket, non-digit characters are appended
directly to `current`.

Time Complexity: O(n * maxK) — n is length of input, maxK is the largest
repeat count, since each expansion can multiply substring length.
Space Complexity: O(n) — for the stack and the output string.
"""


# ---------------------- Solution ------------------------------


def decodeString(s):
    stack = []
    current = ""
    count = 0
    for ch in s:
        if ch.isdigit():
            count = count * 10 + int(ch)
        elif ch == '[':
            stack.append((current, count))
            current = ""
            count = 0
        elif ch == ']':
            prev_string, repeat_count = stack.pop()
            current = prev_string + current * repeat_count
        else:
            current += ch
    return current
