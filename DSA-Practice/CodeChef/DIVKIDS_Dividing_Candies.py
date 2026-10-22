"""
Problem   : Dividing Candies (DIVKIDS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/DIVKIDS
Difficulty: 845
Topics    : Math, Implementation 
Date      : 2026-10-22

Approach:
    Each jar can be given out only if its candy count is divisible by the
    number of children. Scan all jars, keep the largest count that
    satisfies c % children == 0, and output 0 if none qualifies.

Complexity (per test case, N = number of jars):
    Time  : O(N)
    Space : O(N) to store the jars (O(1) extra beyond that)
"""


# ------------------------------------------ Solution --------------------------------------------------------


import sys

def pick_jar(children, jars):
    best = 0
    for c in jars:
        if c % children:
            continue
        if c > best:
            best = c
    return best

def run():
    tokens = iter(sys.stdin.read().split())
    cases = int(next(tokens))
    results = []
    while cases > 0:
        cases -= 1
        count = int(next(tokens))
        kids = int(next(tokens))
        jars = [int(next(tokens)) for _ in range(count)]
        results.append(str(pick_jar(kids, jars)))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    run()
