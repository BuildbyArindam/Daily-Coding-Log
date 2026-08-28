"""
Problem   : Bob and Bombs
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/bob-and-bombs-cake-walk/
Difficulty: Easy
Topics    : Approved, Basic Programming, Implementation, Open
Date      : 2026-08-28

Approach:
For each 'B' in the string, mark any 'W' within a distance of 2 on either
side as destroyed (using a boolean array to avoid double counting).
Count all destroyed 'W's at the end.

Time complexity : O(N) per test case  (each index does O(1) work, 4 fixed offset checks)
Space complexity: O(N) per test case  (for the destroyed[] boolean array)
"""


# --------------------------- Solution ------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        s = list(input_data[i])
        n = len(s)
        destroyed = [False] * n
        for idx in range(n):
            if s[idx] == "B":
                if idx - 1 >= 0 and s[idx - 1] == "W":
                    destroyed[idx - 1] = True
                if idx - 2 >= 0 and s[idx - 2] == "W":
                    destroyed[idx - 2] = True
                if idx + 1 < n and s[idx + 1] == "W":
                    destroyed[idx + 1] = True
                if idx + 2 < n and s[idx + 2] == "W":
                    destroyed[idx + 2] = True
        results.append(str(sum(destroyed)))
    print("\n".join(results))

if __name__ == "__main__":
    solve()
