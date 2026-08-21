"""
Problem   : Jump Out
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/jump-out-34/
Difficulty: Easy
Topic     : Basic Programming / Implementation
Date      : 2026-08-21

Approach:
    For each position i (1-indexed), check if the value at that index
    is >= the number of elements remaining from i to n (inclusive).
    The first index satisfying this condition is the answer — it's the
    earliest point from which you can "jump out" of the array given
    the remaining distance to the end.

Time Complexity : O(n)  -> single pass over the array
Space Complexity: O(n)  -> storing the array itself (O(1) extra otherwise)
"""


# ------------------------ Solution -------------------------------


import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n + 1]]
    for i in range(1, n + 1):
        if a[i - 1] >= (n - i + 1):
            print(i)
            break

if __name__ == '__main__':
    main()
