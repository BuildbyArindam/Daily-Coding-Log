"""
Problem   : Minimum Coins (VISA09)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/VISA09
Date      : 2026-10-19
Difficulty: Hard
Topics    : Dynamic Programming, Coin Change

Approach  : Unbounded knapsack / coin-change DP. ways[a] holds the fewest coins
            needed to make amount a. Denominations larger than the target are
            dropped and duplicates removed. For each coin d, iterate amounts
            upward from d so the coin can be reused, and relax
            ways[a] = min(ways[a], ways[a - d] + 1). If ways[target] is still
            the sentinel INF, the amount is unreachable and we print -1.

Time      : O(n * target)
Space     : O(target)
"""


# --------------------------------------------- Solution --------------------------------------------------------


import sys

def solve():
    raw = sys.stdin.read().split()
    n, target = int(raw[0]), int(raw[1])
    denoms = sorted({int(x) for x in raw[2:2 + n] if int(x) <= target}, reverse=True)
    INF = target + 1
    ways = [INF] * (target + 1)
    ways[0] = 0
    for d in denoms:
        for amt in range(d, target + 1):
            cand = ways[amt - d] + 1
            if cand < ways[amt]:
                ways[amt] = cand
    print(-1 if ways[target] >= INF else ways[target])

if __name__ == "__main__":
    solve()
