"""
Problem   : Mancunian in Palindromia
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/mancunian-in-palindromia-3/
Difficulty: Easy
Topic     : Basic Programming / Implementation
Date      : 2026-08-24

Approach:
For each string, check whether it can be turned into a palindrome using
at most two substring-reversal operations:
  1. Check if it's already a palindrome.
  2. Try every single substring reversal (i..j) and check.
  3. Try every pair of non-overlapping substring reversals (i..j, k..l)
     and check.
Count how many of the N strings satisfy this.

Complexity:
  Time : O(N * L^7) worst case — for a string of length L, the double
         reversal search is O(L^4) combinations, each requiring an
         O(L) palindrome check/string build → O(L^5) per string
         (single-reversal pass adds a lower-order O(L^3) term).
         Repeated across N strings.
  Space: O(L) per candidate string built during the checks.

Note: brute-force; fine for small L, but will not scale — an O(L) or
O(L^2) two-pointer / prefix-suffix mismatch approach would be far
better if L grows large.
"""


# ------------------------- Solution ----------------------------


import sys

def is_palindrome(s):
    return s == s[::-1]

def can_form_palindrome(s):
    if is_palindrome(s):
        return True
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            t = s[:i] + s[i:j+1][::-1] + s[j+1:]
            if is_palindrome(t):
                return True
    for i in range(n):
        for j in range(i, n):
            for k in range(j + 1, n):
                for l in range(k, n):
                    t = (s[:i] + 
                         s[i:j+1][::-1] + 
                         s[j+1:k] + 
                         s[k:l+1][::-1] + 
                         s[l+1:])
                    if is_palindrome(t):
                        return True      
    return False

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    L = int(input_data[1])
    successful_count = 0
    for idx in range(2, 2 + N):
        s = input_data[idx]
        if can_form_palindrome(s):
            successful_count += 1
    print(successful_count)

if __name__ == "__main__":
    solve()
