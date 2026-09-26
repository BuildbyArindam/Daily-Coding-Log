"""
Problem   : Wormtongue's Mind (MINMAX)
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/MINMAX
Difficulty: Hard
Date      : 2026-09-26

Topics    : Probability, Expected Value, Order Statistics,
            Bernstein Polynomials, Polynomial Multiplication,
            Combinatorics, Recursion / Expression Tree Evaluation

Approach  :
    Each leaf 'x' in the expression is an independent random variable,
    represented by its CDF as a degree-1 Bernstein polynomial [0, 1]
    (i.e. F(t) = t on [0, 1]).

    The expression is parsed as a binary tree ('M' = max, other op = min).
    For two independent variables with CDFs F, G:
        CDF(max(X, Y))(t) = F(t) * G(t)
        CDF(min(X, Y))(t) = 1 - (1 - F(t)) * (1 - G(t))

    Bernstein polynomials of degree d and e multiply to a Bernstein
    polynomial of degree d+e via:
        C(d,i)*C(e,j)/C(d+e,i+j) * a_i * b_j   (multiply_bernstein)

    Once the CDF of the whole expression is known as a Bernstein
    polynomial, E[result] = 1 - integral(F) = 1 - mean(coefficients),
    since the Bernstein basis polynomials each integrate to 1/(d+1).

Complexity (n = number of variable leaves in the expression):
    Time  : O(n^2) per test case — each merge multiplies two Bernstein
            polynomials of degree dp, dq in O(dp*dq); summed over the
            expression tree this is O(n^2) in the worst case regardless
            of tree shape (naive convolution, not FFT-accelerated).
    Space : O(n) — polynomial coefficient arrays plus O(n) recursion
            depth for parsing/building the tree.
"""


# --------------------------------------- Solution --------------------------------------------


import sys
import math

def multiply_bernstein(p, q):
    dp = len(p) - 1
    dq = len(q) - 1
    total = dp + dq
    ans = [0.0] * (total + 1)
    left_choose = [math.comb(dp, i) for i in range(dp + 1)]
    right_choose = [math.comb(dq, j) for j in range(dq + 1)]
    whole_choose = [math.comb(total, k) for k in range(total + 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            k = i + j
            factor = (
                left_choose[i]
                * right_choose[j]
                / whole_choose[k]
            )
            ans[k] += a * b * factor
    return ans

def expectation(expr):
    at = 0
    def build():
        nonlocal at
        symbol = expr[at]
        at += 1
        if symbol == 'x':
            # F(t) = t
            return [0.0, 1.0]
        first = build()
        second = build()
        if symbol == 'M':
            return multiply_bernstein(first, second)
        first_bar = [1.0 - z for z in first]
        second_bar = [1.0 - z for z in second]
        both_greater = multiply_bernstein(first_bar, second_bar)
        return [1.0 - z for z in both_greater]
    polynomial = build()
    degree = len(polynomial) - 1
    integral_f = math.fsum(polynomial) / (degree + 1)
    return 1.0 - integral_f

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []
    for expr in data[1:t + 1]:
        out.append(f"{expectation(expr):.6f}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
