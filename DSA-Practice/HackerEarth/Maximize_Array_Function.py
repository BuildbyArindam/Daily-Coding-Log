"""
Problem   : Maximize Array Function
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/approximate/maximize-array-function-2-e692ab46/
Difficulty: Medium
Topics    : Arrays, Data Structures, 1-D
Date      : 2026-09-12

Approach:
    This is an APPROXIMATE/optimization problem, not exact-answer. We must choose
    which K = R-L+1 elements occupy the fixed window [L, R] to maximize
    S / (1 + X), where S = sum of chosen elements and X = sum over bit positions
    of (count of 1-bits * count of 0-bits * 2^bit) among the chosen elements.

    Strategy:
      1. Generate multiple greedy starting selections (top-K by value, and
         top-K by value/(1 + XOR-with-anchor) for a few high-value anchors).
      2. Run local search (best-improvement 1-swap, ~6 iterations) on each
         starting selection using a linear-in-the-objective surrogate score
         (q = S/(1+X)) to pick promising swap candidates without O(K*(N-K))
         brute force every round (restricted to top ~220 candidates per side).
      3. Keep the best (S, X) found across all starts, place chosen indices
         (1-indexed) into positions [L-1, R-1] of the output permutation,
         fill remaining positions with unused indices in order.

Complexity:
    Let K = R-L+1, B = bit-length of max(A) (~20-30 for typical constraints).
    Time : O(starts * iters * (N*B + TOP^2))  — heuristic, not guaranteed optimal.
    Space: O(N + B)

Note: This is a heuristic/local-search approach (no exact optimality proof),
appropriate since the platform scores "approximate" solutions.
"""


# -------------------------- Solution --------------------------------


import sys
from heapq import nlargest

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    N, L, R = data[0], data[1], data[2]
    A = data[3:3 + N]
    left = L - 1
    right = R - 1
    K = R - L + 1
    if K == N:
        print(*range(1, N + 1))
        return
    BITS = max(1, max(A).bit_length())
    POW = [1 << b for b in range(BITS)]
    TOP = 220
    def xor_sum(x, ones):
        total = 0
        for b, w in enumerate(POW):
            cnt1 = ones[b]
            if x & w:
                total += (K - cnt1) * w
            else:
                total += cnt1 * w
        return total
    def evaluate(selected):
        ones = [0] * BITS
        S = 0
        for idx in selected:
            x = A[idx]
            S += x
            for b, w in enumerate(POW):
                if x & w:
                    ones[b] += 1
        X = 0
        for b, w in enumerate(POW):
            cnt1 = ones[b]
            cnt0 = K - cnt1
            X += cnt1 * cnt0 * w
        return S, X, ones
    def local_search(selected):
        selected = selected[:]
        used = [False] * N
        for idx in selected:
            used[idx] = True
        S, X, ones = evaluate(selected)
        for _ in range(6):
            denominator = 1 + X
            q = S / denominator
            outgoing = []
            for idx in selected:
                y = A[idx]
                cost_y = xor_sum(y, ones)
                remove_score = q * cost_y - y
                outgoing.append((remove_score, idx, cost_y))
            outgoing = nlargest(
                min(TOP, K),
                outgoing
            )
            incoming = []
            for idx in range(N):
                if used[idx]:
                    continue
                x = A[idx]
                add_cost = xor_sum(x, ones)
                add_score = x - q * add_cost
                incoming.append((add_score, idx, add_cost))
            incoming = nlargest(
                min(TOP, N - K),
                incoming
            )
            best_swap = None
            best_delta = 0.0
            for _, i, add_cost in incoming:
                x = A[i]
                for _, j, cost_y in outgoing:
                    y = A[j]
                    delta_S = x - y
                    delta_X = -cost_y + add_cost - (x ^ y)
                    delta = delta_S - q * delta_X
                    if delta > best_delta:
                        best_delta = delta
                        best_swap = (i, j, delta_S, delta_X)
            if best_swap is None:
                break
            i, j, delta_S, delta_X = best_swap
            used[j] = False
            used[i] = True
            for p in range(K):
                if selected[p] == j:
                    selected[p] = i
                    break
            S += delta_S
            X += delta_X
            ones = [0] * BITS
            for idx in selected:
                x = A[idx]
                for b, w in enumerate(POW):
                    if x & w:
                        ones[b] += 1
        return selected, S, X
    order = sorted(range(N), key=A.__getitem__, reverse=True)
    starts = [order[:K]]
    for anchor_idx in order[:min(3, N)]:
        anchor = A[anchor_idx]
        candidate_order = sorted(
            range(N),
            key=lambda i: A[i] / (1 + (A[i] ^ anchor)),
            reverse=True
        )
        starts.append(candidate_order[:K])
    best_selected = None
    best_S = 0
    best_X = 1
    for start in starts:
        selected, S, X = local_search(start)
        if best_selected is None or S * (1 + best_X) > best_S * (1 + X):
            best_selected = selected
            best_S = S
            best_X = X
    chosen = [False] * N
    for idx in best_selected:
        chosen[idx] = True
    remaining = [i for i in range(N) if not chosen[i]]
    B = [0] * N
    for pos, idx in enumerate(best_selected, start=left):
        B[pos] = idx + 1
    ptr = 0
    for pos in range(N):
        if left <= pos <= right:
            continue
        B[pos] = remaining[ptr] + 1
        ptr += 1
    print(*B)

if __name__ == "__main__":
    solve()
