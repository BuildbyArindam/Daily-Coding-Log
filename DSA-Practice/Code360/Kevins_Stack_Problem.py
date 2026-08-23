"""
Problem: Kevin's Stack Problem
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/kevin-s-stack-problem_1169465?kunjiRedirection=true
Date: 2026-08-23
Difficulty: Easy
Topics: Stack, String

Approach:
Push every character of the input string onto a stack, then pop
characters one by one to build the output — since a stack is LIFO,
this naturally reverses the string.

Time Complexity:  O(n)  -> one pass to push, one pass to pop
Space Complexity: O(n)  -> stack holds all n characters
"""


# ---------------------- Solution ----------------------------


from os import *
from sys import *
from collections import *
from math import *

def kevinStackProblem(givenString):
    stack = []
    for ch in givenString:
        stack.append(ch)
    ans = ""
    while stack:
        ans += stack.pop()
    return ans
