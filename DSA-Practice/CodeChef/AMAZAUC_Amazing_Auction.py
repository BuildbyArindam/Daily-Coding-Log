"""
CodeChef: Amazing Auction
Problem: https://www.codechef.com/problems/AMAZAUC
Date: 2026-09-29
Difficulty: 1715
Topics: Sorting, Greedy

Approach:
- Consider each distinct value in A as the target auction price x.
- Count how many participants already satisfy A[i] >= x.
- If more than K participants qualify, profit is simply K * x.
- Otherwise, choose the cheapest participants to upgrade to x using
  (x - A[i]) * C[i] as the upgrade cost.
- Track the maximum possible profit across all candidate prices.

Complexity:
- Time:  O(N^2 log N) per test case
- Space: O(N)
"""


# -------------------------------------- Solution -----------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        C = list(map(int, input().split()))
        ans = 0
        thresholds = sorted(set(A))
        for x in thresholds:
            already = 0
            costs = []
            for i in range(N):
                if A[i] >= x:
                    already += 1
                else:
                    costs.append((x - A[i]) * C[i])
            need = K + 1 - already
            if need <= 0:
                profit = K * x
            else:
                costs.sort()
                cost = sum(costs[:need])
                profit = K * x - cost
            if profit > ans:
                ans = profit
        print(ans)

if __name__ == "__main__":
    solve()
