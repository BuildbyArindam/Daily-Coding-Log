"""
Platform   : CodeChef
Problem    : Chef Anup (CHEFANUP)
Link       : https://www.codechef.com/problems/CHEFANUP
Difficulty : 1718
Topics     : Number System, Mathematics
Date       : 2026-10-01

Approach:
    Sequences of length N over the values 1..K, in lexicographic order, map
    one-to-one onto the base-K numbers 0..K^N - 1 written with N digits
    (each digit shifted by +1). So the L-th sequence is the base-K
    representation of (L - 1), padded to N digits, with 1 added to each digit.
    Digits are extracted from the least significant end by repeated
    x % K and x // K, filling the answer from right to left.

Complexity:
    Time  : O(N) per test case (Python big ints make each divmod
            slightly more than O(1) when L is huge)
    Space : O(N) for the answer array
"""


# ----------------------------------- Solution --------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K, L = map(int, input().split())
        x = L - 1
        ans = [0] * N
        for i in range(N - 1, -1, -1):
            ans[i] = (x % K) + 1
            x //= K
        print(*ans)

if __name__ == "__main__":
    solve()
