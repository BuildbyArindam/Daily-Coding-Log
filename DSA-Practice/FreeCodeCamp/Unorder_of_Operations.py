"""
Problem: Unorder of Operations
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-27
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Arrays, String Manipulation, Modular Arithmetic, Simulation

Approach:
Evaluate a list of numbers by cyclically applying a list of operators
(+, -, *, /, %) left to right, without following standard operator
precedence — operators[i] is applied between numbers[i] and numbers[i+1],
cycling back to the start of the operators list once exhausted.

Time Complexity: O(n)  — single pass over `numbers`
Space Complexity: O(1) — only a running result is stored
"""


# --------------------------- Solution --------------------------------


def evaluate(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        operator = operators[(i - 1) % len(operators)]
        number = numbers[i]
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
        elif operator == '*':
            result *= number
        elif operator == '/':
            result /= number
        elif operator == '%':
            result %= number
    return result
