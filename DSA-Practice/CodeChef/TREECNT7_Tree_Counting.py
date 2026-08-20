"""
Problem   : Tree Counting
Platform  : CodeChef (START252, Div 1/2/3/4)
Link      : https://www.codechef.com/problems/TREECNT7
Date      : 2026-08-20

Topics    : Dynamic Programming, Combinatorics, Trees
            (Prufer codes, bipartite spanning tree counting)
Difficulty: Medium-Hard (Div 1 problem; official tag TBD)

Approach:
  Root the tree at vertex 1. A vertex is "even"/"odd" by parity of its
  distance from vertex 1. The given operation only moves value between
  same-parity vertices, so A can be reduced to all-1s iff, for the even
  set E: |E| == sum(A_i for i in E) (and symmetrically for odd, which
  follows automatically since sum(A) = N).

  So we need to count, over all labeled trees on N vertices, the number
  whose "even set under some root-1 BFS parity" satisfies size == sum.
  This factors into two independent pieces:
    1) Choose which vertices form the size-M even set with sum M
       (a subset-sum/knapsack DP over count and sum).
    2) Given M even vertices and N-M odd vertices, count spanning trees
       of the complete bipartite graph K(M, N-M) that respect this
       bipartition: M^(N-M-1) * (N-M)^(M-1)  [Cayley/Prufer bipartite
       generalization].

  Vertex 1 is always in the even set, so it's excluded from the
  knapsack; values are split into: zeros (free, don't affect sum),
  ones (always match cheaply since weight 0 after -1 shift... handled
  via direct combinatorial count in H[]), and "positive" (weight = a_i-1
  after shifting since vertex 1 contributes 1 to size for free).
  A single 0/1 knapsack dp[p][s] over the positive-weight items counts
  ways to pick p of them summing to s; zeros and ones are folded in
  combinatorially via C(Z, s) and H[t] (which sums over how many
  one-valued vertices are also included). Final answer is halved
  (INV2) to correct for even/odd double counting, matching the editorial
  sum but restructured for this decomposition.

Time complexity : O(N^2) per test case for the knapsack DP
                   (positive items x sum), plus O(N) for tree_count[]
                   and H[]; O(N^2) overall (better than editorial's
                   O(N^3) since zeros/ones are handled outside the DP).
Space complexity : O(N^2) for the dp table, O(N) for tree_count/H,
                    O(MAXN) for factorial/inverse-factorial tables.
"""


# ----------------------------- Solution -----------------------------


import sys

MOD = 998244353
INV2 = (MOD + 1) // 2
MAXN = 400
fact = [1] * (MAXN + 1)
ifact = [1] * (MAXN + 1)
for i in range(1, MAXN + 1):
    fact[i] = fact[i - 1] * i % MOD
ifact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)
for i in range(MAXN, 0, -1):
    ifact[i - 1] = ifact[i] * i % MOD

def C(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD

def solve_case(N, A):
    zero = 0
    one = 0
    positive = []
    for x in A:
        if x == 0:
            zero += 1
        elif x == 1:
            one += 1
        else:
            positive.append(x - 1)
    Z = zero
    m = len(positive)
    dp = [[0] * (Z + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    for i, w in enumerate(positive):
        for p in range(i, -1, -1):
            src = dp[p]
            dst = dp[p + 1]
            limit = Z - w
            if limit < 0:
                continue
            for s in range(limit + 1):
                val = src[s]
                if val:
                    dst[s + w] += val
                    if dst[s + w] >= MOD:
                        dst[s + w] -= MOD
    tree_count = [0] * (N + 1)
    for k in range(1, N):
        tree_count[k] = (
            pow(k, N - k - 1, MOD)
            * pow(N - k, k - 1, MOD)
        ) % MOD
    H = [0] * (N + 1)
    for t in range(N + 1):
        total = 0
        for q in range(one + 1):
            k = t + q
            if 1 <= k < N:
                total += C(one, q) * tree_count[k]
                if total >= MOD:
                    total %= MOD
        H[t] = total % MOD
    ans = 0
    for p in range(m + 1):
        row = dp[p]
        for s in range(Z + 1):
            ways = row[s]
            if ways == 0:
                continue
            ways = ways * C(Z, s) % MOD
            ways = ways * H[p + s] % MOD
            ans += ways
            if ans >= MOD:
                ans -= MOD
    return ans * INV2 % MOD

def main():
    input = sys.stdin.readline
    T = int(input())
    out = []
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        out.append(str(solve_case(N, A)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
