"""
Problem   : Alternate Adding (ALTADD)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ALTADD
Date      : 2026-09-04
Difficulty: Easy
Topics    : Math, Greedy, Absolute Value Manipulation, Telescoping Sum, Constructive Algorithms

Approach:
    We need the maximum possible value of |x1| + |x2| + ... via optimal
    sign assignment, which reduces to the identity:

        answer = (|A[0]| + |A[N-1]| + sum(|A[i-1] + A[i]| for i in 1..N-1)) / 2

    This comes from telescoping: each element A[i] can be paired with its
    neighbor so that consecutive terms either reinforce or cancel, and the
    optimal total is captured by summing absolute values of adjacent sums
    plus the two boundary terms, then halving (each interior element is
    counted twice across the telescoping sum).

Time Complexity  : O(N) per test case  ->  O(sum of N) overall
Space Complexity : O(N) for storing the input array (O(1) extra beyond input)
"""


# -------------------------- Solution -------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        # (|A1| + |AN| + sum |Ai-1 + Ai|) / 2
        ans = abs(A[0]) + abs(A[-1])
        for i in range(1, N):
            ans += abs(A[i - 1] + A[i])
        print(ans // 2)

if __name__ == "__main__":
    solve()
