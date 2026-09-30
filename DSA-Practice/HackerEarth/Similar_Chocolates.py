"""
Problem   : Similar Chocolates
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/notebook-pages-dbad75a5/
Difficulty: Easy
Topics    : Data Structures, Hash Tables, Hash Maps, Implementation
Date      : 2026-09-30

Approach:
    Two chocolates are similar when their values have the same number of
    divisors. Precompute the divisor count for every number up to max(A)
    with a sieve-style loop (for each d, increment all its multiples).
    Then bucket the array values by divisor count in a hash map. A bucket
    of size k contributes k*(k-1)/2 similar pairs, and the answer is the
    sum over all buckets.

Complexity:
    Time  : O(N + M log M), where M = max(A)
    Space : O(M) for the divisor table, plus O(D) for the hash map
            (D = number of distinct divisor counts)
"""


# --------------------------------------------- Solution ---------------------------------------------


import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
max_val = max(A)
divisor_count = [0] * (max_val + 1)
for d in range(1, max_val + 1):
    for multiple in range(d, max_val + 1, d):
        divisor_count[multiple] += 1
freq = {}
for x in A:
    cnt = divisor_count[x]
    freq[cnt] = freq.get(cnt, 0) + 1
answer = 0
for k in freq.values():
    answer += k * (k - 1) // 2
print(answer)
