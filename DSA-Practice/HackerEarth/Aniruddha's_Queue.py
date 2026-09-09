"""
Problem   : Aniruddha's Queue
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/aniruddhas-queue-4/
Difficulty: Easy
Topics    : Basic Programming, Implementation
Date      : 2026-09-09

Approach:
    Each of the N people holds X[i] chocolates. Chocolates are handed out
    in a repeating (circular) round: person 1's share, then person 2's,
    ..., person N's, then back to person 1, and so on. We need to find
    which person receives the M-th chocolate overall.

    - total = sum(X) is the size of one full cycle.
    - remaining = M % total gives the position of the M-th chocolate
      within the current cycle. If remaining == 0, the M-th chocolate
      falls exactly on the last person of a full cycle, so set
      remaining = total.
    - Walk the prefix sum of X until it first reaches/exceeds
      `remaining`; that index (1-based) is the answer.
    - Special case: M == 0 means no chocolates have been distributed
      yet, so the first person (1) is trivially "next up" -> print 1.

Time complexity : O(N) per test case  ->  O(sum(N)) overall
Space complexity: O(N) for storing X
"""


# ---------------------------- Solution ----------------------------------------


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    M = int(input())
    if M == 0:
        print(1)
        continue
    total = sum(X)
    remaining = M % total
    if remaining == 0:
        remaining = total
    current = 0
    for i in range(N):
        current += X[i]
        if current >= remaining:
            print(i + 1)
            break
