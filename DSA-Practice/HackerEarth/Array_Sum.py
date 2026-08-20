"""
Problem: Array Sum
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/array-sum-2-725368ac/
Date: 2026-08-20
Difficulty: Easy
Topic: Implementation

Approach:
    Read n followed by n integers from stdin, then output their sum.
    Straightforward single-pass accumulation using Python's built-in sum().

Time Complexity: O(n)  -- one pass to read and sum the array
Space Complexity: O(n) -- storing the array itself (O(1) extra if summed while parsing)
"""


# --------------------------- Solution -------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = list(map(int, input_data[1 : n + 1]))
    print(sum(arr))

if __name__ == "__main__":
    solve()
