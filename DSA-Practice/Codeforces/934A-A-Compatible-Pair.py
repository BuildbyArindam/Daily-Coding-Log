"""
Problem: A Compatible Pair
Platform: Codeforces
Link: https://codeforces.com/contest/934/problem/A
Rating: 1400
Topics: brute force, games, greedy

Date solved: 2026-08-15

Approach:
Tommy hides exactly one lantern from array a to minimize the best
product Banban can form. Since n, m <= 50, brute-force every choice
of hidden index i, and for each such choice, brute-force every
remaining pair (a[k], b[j]) with k != i to find Banban's maximum
achievable product. Track the minimum such maximum across all i
(minimax over a tiny search space).

Time complexity:  O(n^2 * m)   -- safe since n, m <= 50 (worst case ~125,000 ops)
Space complexity: O(n + m)     -- just the input arrays
"""


# ---------------------------- Solution ---------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    a = [int(x) for x in data[2:2 + n]]
    b = [int(x) for x in data[2 + n:2 + n + m]]
    min_of_max_products = float('inf')
    for i in range(n):
        max_product_for_i = float('-inf')
        for k in range(n):
            if k == i:
                continue
            for j in range(m):
                max_product_for_i = max(max_product_for_i, a[k] * b[j])
        min_of_max_products = min(min_of_max_products, max_product_for_i)
    print(min_of_max_products)

if __name__ == "__main__":
    solve()
