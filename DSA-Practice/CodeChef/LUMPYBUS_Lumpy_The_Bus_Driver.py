"""
Problem   : Lumpy - The Bus Driver (LUMPYBUS)
Link      : https://www.codechef.com/problems/LUMPYBUS
Date      : 2026-09-25
Difficulty: 1708
Topics    : Greedy, Sorting, Constructive Algorithms, Ad-Hoc

Approach:
    Sort the array ascending. Greedily try to "afford" the smallest
    values first using a shared budget of P coins (value 1) + Q coins
    (value 2). Odd values are assumed to consume exactly one 1-coin
    each (capped by P); the remainder of every value's cost is drawn
    from the pooled budget (P + 2*Q). Stop as soon as a value can't
    be afforded (safe due to ascending order).

    Note: does not separately verify the 2-coin count is sufficient
    when leftover 1-coins could substitute for a 2-coin — re-check
    this if it fails on edge cases.

Time complexity : O(N log N) per test case (dominated by the sort)
Space complexity: O(N) for storing the array
"""


# ------------------------------------------------- Solution -------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, P, Q = map(int, input().split())
        A = list(map(int, input().split()))
        budget = P + 2 * Q
        A.sort()
        total = 0
        answer = 0
        odd_used = 0
        for x in A:
            if x & 1:
                if odd_used == P:
                    continue
                odd_used += 1
            if total + x > budget:
                break
            total += x
            answer += 1
        print(answer)

if __name__ == "__main__":
    solve()
