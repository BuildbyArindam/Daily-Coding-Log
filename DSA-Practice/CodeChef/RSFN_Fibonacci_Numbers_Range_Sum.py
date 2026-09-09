"""
Problem   : Fibonacci Numbers Range Sum
Link      : https://www.codechef.com/problems/RSFN
Date      : 2026-09-09
Difficulty: Easy (~1000-1200)
Topics    : Dynamic Programming, Fibonacci, Prefix Sums

Approach:
    - Precompute Fibonacci numbers mod 1e9+7 up to max(arr) using O(1) DP recurrence.
    - Build a prefix sum array over fib(arr[i]) so range-sum queries become O(1).
    - Each query (L, R) answered via prefix[R] - prefix[L-1] mod MOD.

Complexity:
    Time  : O(MAX + N + Q)   -- MAX = largest value in arr, Q = number of queries
    Space : O(MAX + N)       -- fib[] array + prefix[] array
"""


# ---------------------------- Solution ----------------------------------


MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    MAX = max(arr)
    fib = [0] * (MAX + 1)
    if MAX >= 1:
        fib[1] = 1
    if MAX >= 2:
        fib[2] = 1
    for i in range(3, MAX + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = (prefix[i - 1] + fib[arr[i - 1]]) % MOD
    for _ in range(Q):
        L, R = map(int, input().split())
        ans = (prefix[R] - prefix[L - 1]) % MOD
        print(ans)

if __name__ == "__main__":
    solve()
