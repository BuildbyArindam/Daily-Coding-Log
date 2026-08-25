"""
Problem   : Duplicate Parenthesis
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/duplicate-parenthesis_2663296?kunjiRedirection=true
Difficulty: Medium
Topics    : Stack, String, Expression Validation

Approach:
Traverse the expression using a stack. Push every character except ')'.
On encountering ')', check the top of the stack:
  - If it's '(' immediately, that means the parenthesis pair has no
    operator/operand inside it -> duplicate parenthesis -> return True.
  - Otherwise, pop until '(' is found (this represents a valid, non-duplicate
    sub-expression) and discard the matching '('.
If no such duplicate is found through the whole expression, return False.

Time Complexity : O(n)  -> each character is pushed and popped at most once
Space Complexity: O(n)  -> stack holds up to n characters in the worst case
"""


# ---------------------- Solution ----------------------------


from sys import *
from collections import *
from math import *

def duplicateParanthesis(expr: str) -> bool:
    stack = []
    for ch in expr:
        if ch == ')':
            if stack and stack[-1] == '(':
                return True
            while stack and stack[-1] != '(':
                stack.pop()
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return False
