"""
Problem   : Killjee and Smallest Palindrome
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/killjee-and-smallest-palindrom-34-e93ac270-a6ee91c1-655ed223-ca02064b-8e621667-d19f700b/
Difficulty: Very Easy
Topics    : String Manipulation, Greedy, Frequency Counting
Date      : 2026-08-29

Approach:
    Read the input string and return its lexicographically smallest
    character — the smallest character available is the natural choice
    when constructing/comparing for the smallest palindrome.

Time Complexity : O(n)  -- single pass via min() over the string
Space Complexity: O(1)  -- no extra data structures beyond input storage
"""


# ------------------------------- Solution ------------------------------------


import sys

def Palindromic_Subsequence(s):
    if not s:
        return "-1"
    return min(s)

def solve():
    s = sys.stdin.read().strip()
    if s:
        print(Palindromic_Subsequence(s))

if __name__ == '__main__':
    solve()
