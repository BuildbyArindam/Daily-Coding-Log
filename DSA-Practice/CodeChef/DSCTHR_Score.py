"""
Platform   : CodeChef
Problem    : Score (DSCTHR)
Link       : https://www.codechef.com/problems/DSCTHR
Difficulty : 622
Topics     : Conditional Statements, Inbuilt Functions, Basic Programming Concepts
Date       : 2026-10-12

Approach:
    The final score for each test case is the best (largest) of the three
    throws. Sort the three values in descending order and take the first.
    Input is read in one pass for speed and output is joined and printed once.

Complexity:
    Time  : O(T), since sorting a fixed 3 elements is O(1) per test case
    Space : O(T) for the output buffer, O(1) extra per test case
"""


# --------------------------------------------- Solution -----------------------------------------------------


import sys

def final_score(throws):
    best = 0
    for d in sorted(throws, reverse=True):
        best = d
        break
    return best

def main():
    tokens = sys.stdin.read().split()
    cases = int(tokens[0])
    out = []
    pos = 1
    while cases > 0:
        trio = list(map(int, tokens[pos:pos + 3]))
        pos += 3
        out.append(str(final_score(trio)))
        cases -= 1
    print("\n".join(out))

main()
