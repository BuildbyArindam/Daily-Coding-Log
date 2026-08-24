"""
Problem: Addition Ain't Simple
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/addition-aint-simple/
Platform: HackerEarth
Date: 2026-08-24
Difficulty: Easy
Topic: Implementation / String Manipulation

Approach:
For each string, reverse it and add corresponding characters (as values 0-25)
position-wise with the reversed string, plus 1, mod 26, mapping back to a
lowercase letter. This is essentially a positional "addition" over the
alphabet ring (mod 26) between each character and its mirror.

Time Complexity:  O(L) per string, O(N*L) overall (N strings, L = max length)
Space Complexity: O(L) per string for the result buffer
"""


# -------------------------- Solution ---------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    for k in range(1, n + 1):
        s = input_data[k]
        rev_s = s[::-1]
        result = []
        for c1, c2 in zip(s, rev_s):
            v1 = ord(c1) - ord('a')
            v2 = ord(c2) - ord('a')
            new_val = (v1 + v2 + 1) % 26
            result.append(chr(ord('a') + new_val))
        print("".join(result))

if __name__ == "__main__":
    solve()
