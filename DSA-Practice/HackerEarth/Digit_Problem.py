"""
Problem: Digit Problem
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/digit-problem/
Date: 2026-08-22
Difficulty: Easy
Topic: Basic Programming / Implementation

Approach:
Greedy digit replacement. To maximize the resulting number, change the
leftmost non-'9' digits to '9' first (since higher place values have
greater impact on the number's magnitude), up to K allowed changes.
Stop changing once K changes are used or a '9' is encountered (no-op).

Time Complexity: O(N) — single pass over the digit string, N = len(X)
Space Complexity: O(N) — result list holding N characters
"""


# ---------------------------- Solution --------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    X, K = input_data[0], int(input_data[1])
    result = []
    changes = 0
    for char in X:
        if char != "9" and changes < K:
            result.append("9")
            changes += 1
        else:
            result.append(char)
    print("".join(result))

if __name__ == "__main__":
    solve()
