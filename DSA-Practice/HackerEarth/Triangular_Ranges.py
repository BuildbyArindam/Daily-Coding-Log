"""
Problem   : Triangular Ranges
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/triangular-ranges-2/
Date      : 2026-10-11
Difficulty: Medium
Topics    : Binary Search, Two Pointers, Prefix-style range counting

Approach  :
  - Precompute all triangular numbers T(n) = n(n+1)/2 up to max R across queries.
  - For a limit X, count pairs (i <= j) with T(i) + T(j) <= X using two
    pointers on the sorted list: if the sum fits, every pair (i, k) for
    k in [i, j] also fits, so add j - i + 1 and advance i; else shrink j.
  - Answer each query as f(R) - f(L - 1).
  - Early exit when limit < 2 (smallest possible sum is 1 + 1).

Complexity:
  - Time  : O(sqrt(maxR)) precompute + O(Q * sqrt(maxR)) for queries
  - Space : O(sqrt(maxR)) for the triangular numbers array
"""


# -------------------------------------- Solution ---------------------------------------------------


import sys
from array import array

def count_pairs(tri, limit):
    if limit < 2:
        return 0
    i = 0
    j = len(tri) - 1
    count = 0
    while i <= j:
        if tri[i] + tri[j] <= limit:
            count += j - i + 1
            i += 1
        else:
            j -= 1
    return count

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    Q = data[0]
    queries = []
    max_R = 0
    for i in range(Q):
        L = data[2 * i + 1]
        R = data[2 * i + 2]
        queries.append((L, R))
        max_R = max(max_R, R)
    tri = array('Q')
    n = 1
    while n * (n + 1) // 2 <= max_R:
        tri.append(n * (n + 1) // 2)
        n += 1
    ans = []
    for L, R in queries:
        result = count_pairs(tri, R) - count_pairs(tri, L - 1)
        ans.append(str(result))
    sys.stdout.write('\n'.join(ans))

if __name__ == "__main__":
    main()
