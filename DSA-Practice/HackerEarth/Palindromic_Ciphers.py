"""
Problem   : Palindromic Ciphers
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/palindromic-ciphers/
Difficulty: Easy
Topics    : Ad-Hoc, Approved, Open
Date      : 2026-09-05

Approach:
  For each test string, check if it's a palindrome (s == s[::-1]).
  - If yes, print "Palindrome".
  - If no, compute the product of each character's 1-indexed alphabet
    position (a=1, b=2, ..., z=26) and print that product.

Time Complexity : O(n) per test case (n = string length) -> O(sum(n)) overall
Space Complexity: O(1) extra space (excluding input storage)
"""


# ------------------------ Solution -------------------------------


name = input()
t = int(name)
for _ in range(t):
    s = input().strip()
    if s == s[::-1]:
        print("Palindrome")
    else:
        product = 1
        for ch in s:
            product *= ord(ch) - ord('a') + 1
        print(product)
