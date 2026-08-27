"""
Problem   : Posh Shopping (POSHOP)
Link      : https://www.codechef.com/problems/POSHOP
Date      : 2026-08-27
Difficulty: Cakewalk / Easy
Topics    : Brute Force, Arrays, Greedy

Approach:
For each test case, either buy exactly one item (max value in array) or
buy two items i < j where C[i] <= C[j], maximizing C[i] + C[j].
Brute-force all pairs (i, j) and take the best valid sum, comparing
against the single-item max.

Time complexity : O(N^2) per test case
Space complexity: O(N)
"""


# ----------------------- Solution --------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        c = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        max_spend = max(c)
        for i in range(n):
            for j in range(i + 1, n):
                if c[i] <= c[j]:
                    max_spend = max(max_spend, c[i] + c[j])
        print(max_spend)

if __name__ == '__main__':
    solve()
