"""
Problem: Even Length Palindromic Number (Pepper and Palindromic Love)
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/pepper-and-palindromic-love-76ae8763/
Difficulty: Easy
Topic: Basic Programming, Basics of Implementation, Implementation
Date Solved: 2026-08-17

Approach:
For each test case, count the frequency of each digit (0-9) in the number
string. The digit with the highest frequency is the one that can be repeated
the most times to form the largest possible block — output that digit.
Ties are broken by picking the smaller digit (since we scan d = 0..9 and
only update on strictly greater counts).

Time Complexity: O(T * L) — T test cases, L = length of each number string
Space Complexity: O(1) per test case (fixed-size freq array of 10)
"""


# ------------------------- Solution -----------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        n_str = input_data[i]
        freq = [0] * 10
        for char in n_str:
            freq[ord(char) - ord('0')] += 1
        best_digit = 0
        max_count = -1
        for d in range(10):
            if freq[d] > max_count:
                max_count = freq[d]
                best_digit = d
        results.append(str(best_digit))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
