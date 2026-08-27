"""
Problem   : Difference Sorting (CIRCUT)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CIRCUT
Difficulty: ~800-1000 (Div 4, Starters 253)
Topics    : Sorting, Greedy, Cyclic Arrays

Approach:
    - Find all "cut points" i where S[i] != S[i+1] (cyclic) — valid_i.
    - Brute-force over all pairs (i, j) of valid cut points such that
      cutting at i and j separates the circle into two arcs with
      matching-color endpoints (S[i] != S[j] and S[i] == S[next_j]).
    - For each valid pair, compute the max of each resulting group
      (g1 = arc between i+1..j, g2 = the rest) and track the best
      sum of the two group maxima.
    - pref_max / suff_max arrays are precomputed to get O(1) range
      max for g2, but g1's max is recomputed via max(A[i+1:j+1])
      each time instead of reusing pref_max, which reintroduces an
      O(N) cost inside the O(N^2) pair loop.

Complexity (as implemented):
    Time  : O(N^2) valid-cut pairs x O(N) inner max recompute
            => O(N^3) worst case per test case
    Space : O(N) for pref_max, suff_max, valid_i

Note: The intended O(N) solution merges consecutive same-color
points into blocks (only each block's max matters), then answer
= sum of the two largest block maxima.
"""


# ------------------------- Solution -----------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    idx = 1
    out = []
    for _ in range(T):
        N = int(data[idx])
        A = [int(x) for x in data[idx + 1 : idx + 1 + N]]
        S = data[idx + 1 + N]
        idx += 1 + N + 1
        pref_max = [0] * N
        suff_max = [0] * N
        pref_max[0] = A[0]
        for k in range(1, N):
            pref_max[k] = max(pref_max[k - 1], A[k])
        suff_max[N - 1] = A[N - 1]
        for k in range(N - 2, -1, -1):
            suff_max[k] = max(suff_max[k + 1], A[k])
        def range_max(l, r):
            if l > r:
                return 0
            res = pref_max[r]
            if l > 0:
                res = max([A[k] for k in range(l, r + 1)]) 
            return res
        max_total_score = 0
        valid_i = []
        for i in range(N):
            next_i = (i + 1) % N
            if S[i] != S[next_i]:
                valid_i.append(i)
        for i_idx in range(len(valid_i)):
            i = valid_i[i_idx]
            for j_idx in range(i_idx + 1, len(valid_i)):
                j = valid_i[j_idx]
                next_j = (j + 1) % N
                if S[i] != S[j] and S[i] == S[next_j]:
                    g1_max = pref_max[j] if i + 1 == 0 else max(A[i + 1 : j + 1])
                    g2_part1 = pref_max[i] if i >= 0 else 0
                    g2_part2 = suff_max[j + 1] if j + 1 < N else 0
                    g2_max = max(g2_part1, g2_part2)
                    max_total_score = max(max_total_score, g1_max + g2_max)
        out.append(str(max_total_score))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
