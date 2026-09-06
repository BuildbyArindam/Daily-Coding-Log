"""
Problem   : Inverse Function
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/39/G
Difficulty: *2400
Topic     : Implementation

Date solved: 2026-09-06

Approach:
    Parse the given C-style function f(n) into an AST via a small hand-rolled
    recursive-descent parser (tokenize with regex, then parse if/return
    statements and +,-,*,/ expressions over n, constants, and nested f(...)
    calls). Since all arithmetic is done mod 32768 (2^15) and n is bounded
    in that range, compute f(n) for every n in [0, 32767) by evaluating the
    AST against a memo table 'values[]' filled in increasing order of n
    (recursive calls always target smaller/previously computed indices
    because of how f is defined). Once the full value table is built,
    scan from n = 32767 down to 0 and return the largest n with
    f(n) == target (the problem guarantees at least one preimage exists
    and asks for the largest one), else -1.

Complexity:
    Time : O(MOD * S) where MOD = 32768 and S is the size of the function
           body's AST (constant per problem, so effectively O(MOD)).
    Space: O(MOD) for the values[] table, plus O(T) for the token list.
"""


# ----------------------- Solution ------------------------------


import sys
import re
MOD = 32768

def solve(data):
    lines = data.splitlines()
    target = int(lines[0].strip())
    source = '\n'.join(lines[1:])
    tokens = re.findall(
        r'int|if|return|f|n|\d+|==|[{}();+\-*/<>]',
        source
    )
    pos = 0
    def eat(expected=None):
        nonlocal pos
        tok = tokens[pos]
        if expected is not None and tok != expected:
            raise ValueError(f"Expected {expected}, got {tok}")
        pos += 1
        return tok
    eat("int")
    eat("f")
    eat("(")
    eat("int")
    eat("n")
    eat(")")
    eat("{")
    def parse_expr():
        return parse_sum()
    def parse_sum():
        node = parse_product()
        while pos < len(tokens) and tokens[pos] in ("+", "-"):
            op = eat()
            right = parse_product()
            node = (op, node, right)
        return node
    def parse_product():
        node = parse_multiplier()
        while pos < len(tokens) and tokens[pos] in ("*", "/"):
            op = eat()
            right = parse_multiplier()
            node = (op, node, right)
        return node
    def parse_multiplier():
        tok = tokens[pos]
        if tok == "n":
            eat("n")
            return ("n",)
        if tok.isdigit():
            eat()
            return ("const", int(tok))
        eat("f")
        eat("(")
        arg = parse_expr()
        eat(")")
        return ("f", arg)
    operators = []
    while tokens[pos] != "}":
        if tokens[pos] == "if":
            eat("if")
            eat("(")
            left = parse_expr()
            cmp_op = eat()
            right = parse_expr()
            eat(")")
            eat("return")
            ret = parse_expr()
            eat(";")
            operators.append((cmp_op, left, right, ret))
        else:
            eat("return")
            ret = parse_expr()
            eat(";")
            operators.append((None, None, None, ret))
    eat("}")
    values = [0] * MOD
    def eval_expr(node, n):
        typ = node[0]
        if typ == "n":
            return n
        if typ == "const":
            return node[1]
        if typ == "f":
            arg = eval_expr(node[1], n)
            return values[arg]
        left = eval_expr(node[1], n)
        right = eval_expr(node[2], n)
        if typ == "+":
            return (left + right) & 32767
        if typ == "-":
            return (left - right) & 32767
        if typ == "*":
            return (left * right) & 32767
        return left // right
    for n in range(MOD):
        for cmp_op, left, right, ret in operators:
            if cmp_op is None:
                values[n] = eval_expr(ret, n)
                break
            a = eval_expr(left, n)
            b = eval_expr(right, n)
            ok = (
                (cmp_op == ">" and a > b) or
                (cmp_op == "<" and a < b) or
                (cmp_op == "==" and a == b)
            )
            if ok:
                values[n] = eval_expr(ret, n)
                break
    for n in range(MOD - 1, -1, -1):
        if values[n] == target:
            return n
    return -1

if __name__ == "__main__":
    data = sys.stdin.read()
    print(solve(data))
