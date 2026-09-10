"""
Problem   : Count Permutations
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/count-permutations-2-b1453c05/
Difficulty: Easy
Topics    : Algorithms, Combinatorics, Linear Search, Observation
Date      : 2026-09-10

Approach:
    For array A of size N, check feasibility conditions in one pass:
      - A[0] must be a valid value in [1, N]
      - A[i] >= i+1 for every position (lower bound constraint)
      - A must be non-decreasing (A[i] >= A[i-1])
      - A[-1] must equal N (upper bound closes at N)
    Whenever a run of equal consecutive values occurs, the number of
    ways to arrange that run is (A[i] - (i+1) + 1), multiplied into
    the running answer (mod 1e9+7). If any condition fails, answer is 0.

Time complexity : O(N) per test case  -> O(sum(N)) overall
Space complexity: O(N) for storing the input array
"""


# --------------------------- Solution -------------------------------------


MOD = 10**9 + 7
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    possible = True
    if A[0] < 1 or A[0] > N:
        possible = False
    for i in range(N):
        if A[i] < i + 1:
            possible = False
        if i > 0 and A[i] < A[i - 1]:
            possible = False
        if i > 0 and A[i] == A[i - 1]:
            choices = A[i] - (i + 1) + 1
            if choices <= 0:
                possible = False
            else:
                ans = (ans * choices) % MOD
    if A[-1] != N:
        possible = False
    print(ans if possible else 0)
