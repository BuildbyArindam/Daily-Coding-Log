"""
Problem : Discount (DSCOP)
Platform: CodeChef (DSAMONDAY022)
Link    : https://www.codechef.com/DSAMONDAY022/problems/DSCOP
Date    : 2026-09-28
Difficulty: Medium
Topics  : Greedy, Strings, Stack

Approach:
    Greedy with a single-pass stack. To minimize the number after removing one
    digit, delete the first digit that is larger than the digit after it.
    If the digits never decrease, delete the last digit. int() at the end
    drops any leading zeros.

Time : O(L) per token, where L is the number of digits
Space: O(L) for the kept-digit stack
"""


# ----------------------------------- Solution --------------------------------------------------


import sys

def cheapest(token):
    kept = []
    dropped = False
    for ch in token:
        if not dropped:
            while kept and kept[-1] > ch:
                kept.pop()
                dropped = True
                break
        kept.append(ch)
    if not dropped:
        kept.pop() 
    return int("".join(kept))

def main():
    tokens = sys.stdin.read().split()
    total = int(tokens[0])
    answers = [str(cheapest(tokens[k])) for k in range(1, total + 1)]
    sys.stdout.write("\n".join(answers) + "\n")

if __name__ == "__main__":
    main()
