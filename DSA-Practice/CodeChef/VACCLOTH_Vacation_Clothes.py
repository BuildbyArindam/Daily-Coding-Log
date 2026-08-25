"""
Problem: Vacation Clothes
Platform: CodeChef
Link: https://www.codechef.com/problems/VACCLOTH
Date: 2026-08-25

Approach:
Chef has N vacation days but only 7 unique outfits (one per day of the week,
since laundry cycles weekly). So the number of days he can dress without
repeating an outfit is capped at 7, regardless of how large N is.
Answer = min(N, 7).

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution ---------------------------


import sys

def main():
    N = int(sys.stdin.read().strip())
    print(min(N, 7))

if __name__ == "__main__":
    main()
