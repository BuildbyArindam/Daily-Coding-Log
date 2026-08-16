"""
Problem   : The Alphabet Chocolate
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/count-vowels-1-1da7c4d0/
Difficulty: Easy
Topic     : Basic Programming, Basics of Implementation, Implementation
Date      : 2026-08-16

Approach:
For each vowel at index i (0-indexed) in a string of length n, the number
of substrings that contain that character equals (i+1) * (n-i)
[choices for left boundary * choices for right boundary]. Summing this
weight over every vowel position gives the total "taste" for that string.
Read all input at once via sys.stdin for fast I/O across multiple test cases.

Time complexity : O(N) per test case, O(total length of all strings) overall
Space complexity: O(1) extra space (excluding input storage/output buffer)
"""


# ------------------------ Solution ----------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    num_test_cases = int(data[0])
    vowels = set("aeiouAEIOU")
    results = []
    for t in range(1, num_test_cases + 1):
        s = data[t]
        n = len(s)
        total_taste = 0
        for i, char in enumerate(s):
            if char in vowels:
                total_taste += (i + 1) * (n - i)
        results.append(str(total_taste))
    print("\n".join(results))

if __name__ == "__main__":
    solve()
