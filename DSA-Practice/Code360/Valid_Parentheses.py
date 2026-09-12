"""
Problem: Valid Parentheses
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/651074/offering/10442135
Difficulty: Easy
Date Solved: 2026-09-12
Topics: Stack, String

Approach:
Use a stack to track opening brackets. For each closing bracket,
check if the top of the stack matches its corresponding opening
bracket — if not (or stack is empty), the string is invalid.
Valid only if the stack is empty at the end (all brackets matched).

Time Complexity:  O(n) — single pass through the string
Space Complexity: O(n) — worst case, stack holds all opening brackets
"""


# --------------------------- Solution -------------------------------------


def isValidParenthesis(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0
