"""
Platform   : CodeChef (ICPCOL26POST)
Problem    : Phone Charging
Link       : https://www.codechef.com/ICPCOL26POST/problems/PHNCHRG
Date       : 2026-10-06
Difficulty : Easy
Topics     : Math, Greedy, Implementation

Approach:
    The charge still needed is (100 - level). The top portion, capped at
    20 units, is billed at fast_cost per unit. Everything below that
    portion is billed at slow_cost per unit. So the answer per test case is:
        lower * slow_cost + upper * fast_cost
    where upper = min(100 - level, 20) and lower = (100 - level) - upper.

Complexity:
    Time  : O(T), constant work per test case
    Space : O(T) for the output buffer (O(1) extra per test case)
"""


# ------------------------------------------ Solution --------------------------------------------------------


import sys

def main():
    tokens = sys.stdin.read().split()
    cases = int(tokens[0])
    out = []
    pos = 1
    for _ in range(cases):
        level, slow_cost, fast_cost = (int(v) for v in tokens[pos:pos + 3])
        pos += 3
        remaining = 100 - level
        upper_part = min(remaining, 20)     
        lower_part = remaining - upper_part 
        out.append(str(lower_part * slow_cost + upper_part * fast_cost))
    print("\n".join(out))

main()
