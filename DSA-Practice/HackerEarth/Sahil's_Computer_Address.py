"""
Problem: Sahil's Computer Address
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/sahils-computer-address-20/
Date: 2026-08-22
Difficulty: Easy
Topics: Implementation, String Validation, Data Structures

Approach:
Split the input string on '.' and check that it produces exactly 4 parts.
Each part must be a non-empty numeric string whose integer value lies
between 0 and 255 (inclusive) to qualify as a valid IPv4 address.

Time Complexity: O(n) - single pass to split and validate each of the 4 octets
Space Complexity: O(n) - storage for the split parts list
"""


# ----------------------------- Solution -------------------------------


import sys

def is_valid_ip(s):
    parts = s.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part or not part.isdigit():
            return False
        val = int(part)
        if val < 0 or val > 255:
            return False
    return True

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    if is_valid_ip(s):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
