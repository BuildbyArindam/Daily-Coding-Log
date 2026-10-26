"""
Problem   : Bank Account Validator (BACVA)
Platform  : CodeChef (DSAMONDAY026)
Link      : https://www.codechef.com/DSAMONDAY026/problems/BACVA
Difficulty: Medium
Topics    : Strings, Implementation, Math 
Date      : 2026-10-26

Approach  : For each account number, sum its digits and mark it "Valid"
            if the sum is divisible by 10, otherwise "Invalid". All
            accounts are read at once and the verdicts are printed in one write.

Time      : O(L), where L is the total number of digits across all accounts
Space     : O(N) for the stored verdicts (O(1) extra per account)
"""


# ------------------------------------------------------- Solution -------------------------------------------------------------------------


import sys

def main():
    tokens = sys.stdin.read().split()
    count = int(tokens[0])
    accounts = tokens[1:1 + count]
    weight = {chr(48 + k): k for k in range(10)}
    verdicts = []
    for acct in accounts:
        running = 0
        for ch in acct:
            running += weight[ch]
        verdicts.append("Valid" if running % 10 == 0 else "Invalid")
    sys.stdout.write("\n".join(verdicts) + "\n")

main()
