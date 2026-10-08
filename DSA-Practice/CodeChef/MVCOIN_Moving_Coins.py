"""
Problem   : Moving Coins (MVCOIN)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MVCOIN
Difficulty: 1733
Topics    : Greedy, Math
Date      : 2026-10-08

Approach:
    Scan the positions 1..1000 once. The i-th empty cell must end up at
    position N + i (all coins packed to the left). The gap between its
    current and target position equals the number of coins to its right.
    Each move covers up to K of that gap, so the cell costs
    ceil(gap / K). The answer is the sum over all empty cells.

Complexity:
    Time : O(M) per test case, where M = 1000 is the position bound
           (plus O(N) to mark occupied cells)
    Space: O(M) for the occupancy array
"""


# --------------------------------------------- Solution ----------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        X = list(map(int, input().split()))
        occupied = [False] * 1001
        for x in X:
            occupied[x] = True
        answer = 0
        empty_index = 0
        for pos in range(1, 1001):
            if not occupied[pos]:
                empty_index += 1
                target = N + empty_index
                distance = target - pos
                answer += (distance + K - 1) // K
        print(answer)

if __name__ == "__main__":
    solve()
