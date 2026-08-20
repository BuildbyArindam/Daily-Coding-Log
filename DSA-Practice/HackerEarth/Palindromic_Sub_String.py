"""
Problem   : Palindromic Sub-String <P2SME>
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/partition-string-db2c970d/
Difficulty: Easy
Topic     : Basic Programming, String Manipulation
Date      : 2026-08-20

Approach:
    Brute-force generation of all substrings of S (length >= 2).
    For each substring, reverse it and check if the reversed string
    exists anywhere in S. Track the maximum length substring that
    satisfies this condition. If any such substring is found, output
    "YES" with its max length; otherwise output "NO".

Time Complexity : O(n^3)
    - O(n^2) substrings generated via the (i, j) double loop
    - O(n) for slicing + O(n) for the `in` substring search per candidate
Space Complexity: O(n)
    - Dominated by the substring/reversed-substring slices created per iteration
"""


# --------------------------- Solution ---------------------------------


import sys

def process_string(S):
    n = len(S)
    max_len = 0
    for i in range(n):
        for j in range(i + 2, n + 1):
            sub = S[i:j]
            rev_sub = sub[::-1]
            if rev_sub in S:
                max_len = max(max_len, len(sub))
    if max_len > 0:
        return f"YES\n{max_len}"
    else:
        return "NO"

if __name__ == '__main__':
    S = sys.stdin.read().strip()
    if S:
        print(process_string(S))
