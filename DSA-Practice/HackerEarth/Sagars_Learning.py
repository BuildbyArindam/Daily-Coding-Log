"""
Problem   : Sagar's Learning
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/sagars-learning/
Difficulty: Easy
Date      : 2026-08-24

Approach:
For each n, if n < 3 no valid triplet exists (-1). Otherwise, split n into
three parts in ratio 1:2:3 using k = n // 3, giving (k, 2k, 3k).

Time Complexity : O(1) per query, O(T) overall
Space Complexity: O(1) extra (excluding input buffer)
"""


# -------------------------- Solution ----------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    for i in range(1, t + 1):
        n = int(input_data[i])
        if n < 3:
            print("-1")
        else:
            k = n // 3
            print(f"{k} {2 * k} {3 * k}")

if __name__ == "__main__":
    solve()
