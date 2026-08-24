"""
Problem: Min-Max
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/min-max-3/
Platform: HackerEarth | Difficulty: Easy | Topic: Basic Programming
Date: 2026-08-24

Approach:
    Read the array, build a set of its elements, then check whether every
    integer in the inclusive range [min(arr), max(arr)] is present in the set.
    If any value in that range is missing, the array can't form a contiguous
    block from min to max, so print "NO"; otherwise print "YES".

Time Complexity:  O(n + (max - min))  — set build is O(n); range scan is O(max-min)
Space Complexity: O(n)                — for the set and input array
"""


# -------------------------- Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    num_set = set(arr)
    min_val = min(arr)
    max_val = max(arr)
    for x in range(min_val, max_val + 1):
        if x not in num_set:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    solve()
