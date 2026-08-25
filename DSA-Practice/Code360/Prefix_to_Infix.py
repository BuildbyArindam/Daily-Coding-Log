"""
Problem   : Prefix to Infix
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/prefix-to-infix_1215000?kunjiRedirection=true
Difficulty: Easy
Date      : 2026-08-25

Approach:
    Scan the prefix expression from right to left using a stack.
    - If the current char is an operand (alpha), push it onto the stack.
    - If it's an operator, pop the top two operands (operand1, operand2)
      and push the combined infix string "(operand1 operator operand2)".
    The final element left on the stack is the fully parenthesized infix expression.

Time Complexity : O(n)   -- each character is processed once, each stack op is O(1)
Space Complexity: O(n)   -- stack holds up to n operand/sub-expression strings
"""


# ------------------------- Solution -----------------------------


def prefixToInfixConversion(s: str) -> str:
    stack = []
    for ch in reversed(s):
        if ch.isalpha():
            stack.append(ch)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append("(" + operand1 + ch + operand2 + ")")
    return stack[-1]
