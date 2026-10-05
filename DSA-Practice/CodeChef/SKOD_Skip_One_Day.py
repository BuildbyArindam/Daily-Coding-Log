"""
Platform   : CodeChef
Problem    : Skip One Day (SKOD)
Link       : https://www.codechef.com/DSAMONDAY023/problems/SKOD
Date       : 2026-10-05
Difficulty : Easy
Topics     : Greedy, Arrays, Math

Approach:
    Exactly one element is skipped, and the goal is to maximize the sum of
    the rest. Greedy: take the total sum and subtract the minimum element.
    Input is read in one pass with sys.stdin.buffer for speed.

Complexity:
    Time  : O(N) per test case (one sum + one min)
    Space : O(N) per test case for the parsed values, O(T) for the answers
"""


# ------------------------------------ Solution ------------------------------------------------------


import sys

def solve_all():
    tokens = sys.stdin.buffer.read().split()
    cursor = 0
    cases = int(tokens[cursor])
    cursor += 1
    answers = []
    for _ in range(cases):
        length = int(tokens[cursor])
        cursor += 1
        chunk = tokens[cursor:cursor + length]
        cursor += length
        values = list(map(int, chunk))
        answers.append(str(sum(values) - min(values)))
    return answers

if __name__ == "__main__":
    sys.stdout.write("\n".join(solve_all()) + "\n")
