"""
Problem   : Magical String
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/magical-string_1475043?kunjiRedirection=true
Date      : 2026-08-25
Difficulty: Easy
Topics    : Stack, String

Approach:
Traverse the string maintaining a stack. If the top of the stack is the
same letter as the current character but in opposite case (e.g. 'a' & 'A'),
pop it (they cancel out). Otherwise, push the current character. The final
stack content, joined, is the reduced "magical" string.

Time Complexity : O(n)  — each character is pushed/popped at most once
Space Complexity: O(n)  — worst case, stack holds all characters
"""


# ------------------- Solution -------------------------------


from os import *
from sys import *
from collections import *
from math import *

def magicalString(s):
    stack = []
    for ch in s:
        if stack and stack[-1].lower() == ch.lower() and stack[-1] != ch:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)
