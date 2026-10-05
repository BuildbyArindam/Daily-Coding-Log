"""
Problem   : Birthday Feast (BTFEA)
Platform  : CodeChef - DSAMONDAY023
Link      : https://www.codechef.com/DSAMONDAY023/problems/BTFEA
Date      : 2026-10-05
Difficulty: Hard
Topics    : Dynamic Programming, Unbounded Knapsack

Approach  :
  - Keep only the cheapest price for each distinct portion size.
  - Sort the offers by size so the inner loop can break early.
  - Build best[x], the minimum cost to get exactly x units, with an
    unbounded-knapsack DP: best[x] = min(best[x - size] + price).
  - Compute the table once up to max(appetite), then sum best[a] over
    all appetites.

Complexity:
  Time  : O(N + M log M + A * K), where A = max(appetite) and
          K = number of distinct sizes (K <= M)
  Space : O(A + M)
"""


# ----------------------------------- Solution ---------------------------------------------------


import sys

def read_all():
    return sys.stdin.read().split()

def cheapest_per_size(sizes, prices):
    table = {}
    for s, p in zip(sizes, prices):
        if s not in table or p < table[s]:
            table[s] = p
    return sorted(table.items())

def build_costs(limit, offers):
    INF = float("inf")
    best = [INF] * (limit + 1)
    best[0] = 0
    for target in range(1, limit + 1):
        cur = INF
        for size, price in offers:
            if size > target:
                break
            cand = best[target - size] + price
            if cand < cur:
                cur = cand
        best[target] = cur
    return best

def main():
    tokens = read_all()
    n, m = int(tokens[0]), int(tokens[1])
    pos = 2
    appetite = [int(v) for v in tokens[pos:pos + n]]
    pos += n
    fill = [int(v) for v in tokens[pos:pos + m]]
    pos += m
    cost = [int(v) for v in tokens[pos:pos + m]]
    offers = cheapest_per_size(fill, cost)
    best = build_costs(max(appetite), offers)
    answer = 0
    for a in appetite:
        answer += best[a]
    print(answer)

main()
