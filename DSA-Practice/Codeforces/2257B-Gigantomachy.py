"""
Problem: 2257B - Gigantomachy
Link: https://codeforces.com/contest/2257/problem/B
Date: 2026-08-18
Topic: Math (constructive / closed-form simulation)

Approach:
Each giant's mountain-descent process reduces to a closed form:
Bea loses after (a1 + n - 1) moves, Ver loses after (b1 + m - 1) moves
(sum of consecutive differences telescopes to first_height + count - 1).
Whoever's total is smaller loses -> print the other giant's number.
Ties go to Bea (giant 1), matching the problem's tie-break rule.

Time complexity: O(n + m) per test case (dominated by input parsing)
Space complexity: O(1) extra (excluding input buffer)
"""


# ----------------------- Solution ---------------------------


import sys

def solve(case_tokens):
    n, m, first_a, first_b = case_tokens
    bea_threshold = first_a + n
    ver_threshold = first_b + m
    return 1 if ver_threshold <= bea_threshold else 2

def stream_cases(tokens):
    pos = 0
    total = int(tokens[pos])
    pos += 1
    for _ in range(total):
        n = int(tokens[pos])
        m = int(tokens[pos + 1])
        pos += 2
        a_head = int(tokens[pos])
        pos += n
        b_head = int(tokens[pos])
        pos += m
        yield (n, m, a_head, b_head)

def main():
    raw = sys.stdin.buffer.read().split()
    answers = [str(solve(case)) for case in stream_cases(raw)]
    sys.stdout.write("\n".join(answers) + "\n")

if __name__ == "__main__":
    main()
