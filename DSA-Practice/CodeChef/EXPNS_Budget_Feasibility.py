"""
Platform   : CodeChef
Problem    : Budget Feasibility (EXPNS)
Link       : https://www.codechef.com/problems/EXPNS
Difficulty : 456
Topics     : Math, Implementation
Date       : 2026-10-19

Approach:
    The budget covers a 30-day month only if budget >= per_day * 30.
    For each test case, evaluate that inequality and print YES or NO.
    Input is read in one go and output is joined into a single write,
    which keeps I/O fast for many test cases.

Complexity:
    Time  : O(T), constant work per test case
    Space : O(T) for the token list and stored answers
"""


# ----------------------------------------------------- Solution -----------------------------------------------------------------


import sys
DAYS = 30

def can_cover(budget, per_day):
    return budget >= per_day * DAYS

def run():
    tokens = sys.stdin.read().split()
    cases = int(tokens[0])
    pos = 1
    answers = []
    for _ in range(cases):
        budget = int(tokens[pos])
        per_day = int(tokens[pos + 1])
        pos += 2
        answers.append("YES" if can_cover(budget, per_day) else "NO")
    sys.stdout.write("\n".join(answers) + "\n")

if __name__ == "__main__":
    run()
