"""
Problem   : Bucket Game (BGME)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/BGME
Difficulty: 1802
Topics    : Ad-hoc, Observation, Constructive
Date      : 2026-10-04

Approach:
    Count the buckets with an odd number of items.
    - If some buckets are even, the winner depends only on the parity of
      the odd count: odd -> Alice, even -> Bob.
    - If all buckets are odd, the winner depends on the parity of N:
      N odd -> Alice.
      N even -> Draw if at most one bucket has more than 1 item,
      otherwise Bob.

Time  : O(N) per test case
Space : O(N) for the input list (O(1) extra)
"""


# ------------------------------------------ Solution -------------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        odd = sum(x % 2 for x in A)
        if odd == N:
            if N % 2 == 1:
                print("Alice")
            else:
                bigger = sum(x > 1 for x in A)
                if bigger <= 1:
                    print("Draw")
                else:
                    print("Bob")
        else:
            if odd % 2 == 1:
                print("Alice")
            else:
                print("Bob")

if __name__ == "__main__":
    solve()
