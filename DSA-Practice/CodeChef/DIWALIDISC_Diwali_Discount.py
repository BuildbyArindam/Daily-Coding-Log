"""
Problem   : Diwali Discount
Platform  : CodeChef
Link      : https://www.codechef.com/problems/DIWALIDISC
Date      : 2026-08-25

Approach  :
Given the original price A and a discount amount B, the final
price is A - B, but it can never go below 0. So the answer is
simply max(0, A - B).

Time Complexity  : O(1)
Space Complexity : O(1)
"""


# --------------------------- Solution ----------------------------------


import sys

def main():
    A, B = map(int, sys.stdin.read().split())
    print(max(0, A - B))

if __name__ == "__main__":
    main()
