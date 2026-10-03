"""
Problem   : Discover the Monk
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/discover-the-monk/
Difficulty: Easy
Topics    : Binary Search, Searching, Sorting
Date      : 2026-10-03

Approach  : Store the N integers in a hash set so each of the Q queries
            becomes an O(1) average-case membership check, instead of
            a linear scan or sort + binary search per query.

Complexity: Time  -> O(N + Q) average (O(N) to build the set, O(1) per query)
            Space -> O(N)
"""


# ------------------------------------ Solution ---------------------------------------------


N, Q = map(int, input().split())
A = set(map(int, input().split()))

for _ in range(Q):
    X = int(input())
    if X in A:
        print("YES")
    else:
        print("NO")
