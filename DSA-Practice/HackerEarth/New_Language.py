"""
Problem   : New Language
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/new-language-8c0781c4/
Difficulty: Easy
Topic     : Basic Programming, Implementation
Date      : 2026-08-15

Approach:
    Ninjas use a base-9 numeral system with digits {0,1,2,3,4,5,6,7,9} —
    i.e. the digit '8' doesn't exist, and '9' actually represents the
    value 8 in that base-9 place-value system.
    1. Parse each expression, split on the operator (+, -, *, /).
    2. Convert both operands from "ninja" base-9 notation to decimal
       (ninja_to_dec): walk digits left to right, mapping '9' -> 8,
       accumulating val = val*9 + digit_val.
    3. Perform the requested integer operation in decimal.
    4. Convert the result back to ninja notation (dec_to_ninja) by
       repeated division by 9, mapping remainder 8 -> '9'.

Time complexity : O(L) per test case, where L = length of the expression
                   string (each conversion is linear in digit count);
                   O(sum of L) overall across T test cases.
Space complexity: O(L) for the digit list built during conversion
                   (O(1) extra beyond input/output storage).
"""


# ---------------------- Solution -------------------------


import sys

def ninja_to_dec(s: str) -> int:
    val = 0
    for char in s:
        d = int(char)
        digit_val = d if d < 8 else 8
        val = val * 9 + digit_val
    return val

def dec_to_ninja(n: int) -> str:
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        rem = n % 9
        digits.append(str(rem) if rem < 8 else '9')
        n //= 9
    return "".join(reversed(digits))

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    results = []
    for expr in input_data[1:T + 1]:
        for op in ['+', '-', '*', '/']:
            if op in expr:
                a_str, b_str = expr.split(op)
                a = ninja_to_dec(a_str)
                b = ninja_to_dec(b_str)
                if op == '+':
                    res = a + b
                elif op == '-':
                    res = a - b
                elif op == '*':
                    res = a * b
                elif op == '/':
                    res = a // b
                results.append(dec_to_ninja(res))
                break
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
