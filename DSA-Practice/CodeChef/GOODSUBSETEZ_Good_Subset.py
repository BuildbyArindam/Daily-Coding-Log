"""
Problem   : Good Subset (Easy)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/GOODSUBSETEZ
Date      : 2026-09-04
Difficulty: Easy
Topics    : Hashing, Frequency Counting, Bit Manipulation

Approach:
A "good subset" groups numbers sharing the same bit_length (i.e. same
power-of-two range, floor(log2(x)) + 1). For each test case, compute
bit_length() of every element, count frequencies with Counter, and the
answer is the size of the largest such group (max frequency).

Time Complexity  : O(N) per test case (bit_length is O(1) for fixed-width ints)
Space Complexity : O(N) per test case (Counter holds up to N distinct bit lengths)
"""


# ---------------------------- Dolution -------------------------------------


import sys
from collections import Counter

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        freq = Counter(x.bit_length() for x in arr)
        print(max(freq.values()))

if __name__ == "__main__":
    solve()
