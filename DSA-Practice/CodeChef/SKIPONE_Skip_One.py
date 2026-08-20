"""
Problem   : Skip One (SKIPONE)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SKIPONE
Date      : 2026-08-20
Difficulty: ~800-1000 (Beginner, official rating not yet published)
Topics    : Greedy, Prefix Sums, Arrays

Approach:
    You must buy items strictly in order 1..N (skipping one blocks all
    future purchases), and you hold one coupon that zeroes out a single
    item's price. For any prefix of length i, the optimal move is to use
    the coupon on the most expensive item in that prefix, so the cost of
    buying the first i items is:
        prefix_sum(1..i) - max(1..i)
    Walk left to right, maintaining a running prefix sum and running max.
    The moment (prefix_sum - max) exceeds K, no larger prefix can work
    either (costs are non-decreasing as more items are forced in), so
    stop and report the last valid i.

Time Complexity  : O(N) per test case
Space Complexity : O(N) to store the array (O(1) extra beyond input)
"""


# ------------------------- Solution ---------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        prefix_sum = 0
        max_price = 0
        answer = 0
        for i in range(N):
            prefix_sum += A[i]
            max_price = max(max_price, A[i])
            cost = prefix_sum - max_price
            if cost <= K:
                answer = i + 1
            else:
                break
        print(answer)

if __name__ == "__main__":
    solve()
