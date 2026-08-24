"""
Problem   : Sagar's Gift
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/sagars-gift-6/
Date      : 2026-08-24
Difficulty: Easy
Topic     : Implementation / String-Sorting

Approach:
Read N numbers as raw strings (not ints, since leading zeros or
very large values would otherwise be mangled). Flatten every digit
from every number into a single character list, sort that list in
descending order, and join it back into one string — the largest
possible number formed from all given digits combined.

Time Complexity : O(D log D) per test case, where D = total digit
                   count across all N numbers (dominated by the sort).
Space Complexity: O(D) to hold the flattened digit list.
"""


# --------------------- Solution ----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    ptr = 1
    for _ in range(T):
        N = int(input_data[ptr])
        ptr += 1
        numbers = input_data[ptr:ptr + N]
        ptr += N
        all_digits = []
        for num in numbers:
            all_digits.extend(list(num))
        all_digits.sort(reverse=True)
        print("".join(all_digits))

if __name__ == "__main__":
    solve()
