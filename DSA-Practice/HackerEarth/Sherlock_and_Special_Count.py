"""
Problem   : Sherlock and Special Count
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/sherlock-and-special-count/
Difficulty: Medium
Topics    : Algorithms, Approved, Math, Open
Date      : 2026-09-06

Approach:
For a string of length N containing all distinct characters,
the maximum number of "special" (palindromic-pair / valid) counts
achievable is floor(N^2 / 2). K is achievable iff it's even and
does not exceed this maximum, so just check parity and bound.

Time Complexity : O(1) per test case  ->  O(T) overall
Space Complexity: O(1)
"""


# ------------------------- Solution --------------------------------


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    maximum = (N * N) // 2
    if K % 2 == 0 and K <= maximum:
        print("YES")
    else:
        print("NO")
