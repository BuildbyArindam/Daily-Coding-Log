"""
Problem: Redundant Brackets
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/651074/offering/10442136
Date: 2026-09-12
Difficulty: Easy
Topics: Stack, String Parsing / Expression Evaluation

Approach:
Traverse the expression character by character using a stack.
On encountering ')', pop elements until '(' is found, tracking
whether any operator (+, -, *, /) was seen in between. If no
operator was found before the matching '(', the bracket pair is
redundant. Otherwise, push characters (including operands,
operators, and '(') onto the stack as usual.

Time Complexity: O(n) — each character is pushed and popped at most once
Space Complexity: O(n) — stack can hold up to n characters
"""


# ---------------------------- Solution ------------------------------


from sys import *
from collections import *
from math import *

def findRedundantBrackets(s:str):
	stack = []
	for ch in s:
		if ch == ')':
			has_operator = False
			while stack and stack[-1] != '(':
				top = stack.pop()
				if top in '+-*/':
					has_operator = True
			if stack:
				stack.pop()
			if not has_operator:
				return True
		else:
			stack.append(ch)
	return False
