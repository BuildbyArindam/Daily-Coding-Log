"""
Problem   : C*++ Calculations
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/39/A
Difficulty: *2000
Date      : 2026-09-06
Topics    : Expression Parsing, Greedy, Simulation

Approach:
Parse the C*++ statement into a list of (coefficient, pre/post-increment) terms,
where pre=1 for "++a" style operands and pre=0 for "a++" style. Compute the base
answer by summing coeff * (a + pre) across all terms — this accounts for each
operand's contribution assuming increments happen "in order" but before use for
prefix ops. Since the actual execution order of increments is unspecified/free to
choose, to maximize the final value we want positive-coefficient terms' operand
value boosted by increments that happen earlier, and negative-coefficient terms
boosted by increments happening later (or vice versa depending on max/min ask).
Sort coefficients and add k * coeff for each term at sorted position k, which
distributes the k prior increments optimally across terms by coefficient rank
(greedy exchange argument: to maximize sum, pair larger increment counts with
larger coefficients).

Time complexity : O(n log n)  — dominated by sorting the coefficients
Space complexity: O(n)        — storing parsed terms and coefficients
"""


# -------------------------- Solution ---------------------------------


a = int(input())
s = input().strip()
terms = []
i = 0
n = len(s)
while i < n:
    sign = 1
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        sign = -1
        i += 1
    coeff = 0
    has_coeff = False
    while i < n and s[i].isdigit():
        coeff = coeff * 10 + int(s[i])
        i += 1
        has_coeff = True
    if not has_coeff:
        coeff = 1
    coeff *= sign
    if i < n and s[i] == '*':
        i += 1
    if s[i:i + 3] == "a++":
        pre = 0
    else:
        pre = 1
    i += 3
    terms.append((coeff, pre))
answer = 0
coefficients = []
for coeff, pre in terms:
    answer += coeff * (a + pre)
    coefficients.append(coeff)
coefficients.sort()
for k, coeff in enumerate(coefficients):
    answer += coeff * k
print(answer)
