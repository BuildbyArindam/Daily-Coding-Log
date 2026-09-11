"""
Problem   : Soft Sort
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/softsort-7/
Difficulty: Easy
Topics    : Basic Programming, Math, Implementation
Date      : 2026-09-11

Approach:
Precompute factorials mod 1e9+7 up to the max query value using a running
product array, so each query n can be answered in O(1) via fact[n].
Answer for each query = (3 * fact[n] + 3) % MOD.

Complexity:
Time  : O(max_n + t)  -> O(max_n) to build factorial table, O(t) to answer queries
Space : O(max_n)      -> factorial table storage
"""


# -------------------------- Solution ----------------------------------


MOD = 1000000007
t = int(input())
queries = [int(input()) for _ in range(t)]
max_n = max(queries)
fact = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    fact[i] = (fact[i - 1] * i) % MOD
for n in queries:
    ans = (3 * fact[n] + 3) % MOD
    print(ans)
