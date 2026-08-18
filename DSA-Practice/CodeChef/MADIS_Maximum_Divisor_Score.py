# Problem: Maximum Divisor Score
# Platform: CodeChef
# Link: https://www.codechef.com/problems/MADIS
# Date solved: 2026-08-18
#
# Approach:
#   - Precompute divisor counts for every integer up to `cap` using a
#     sieve (for each factor f, increment count of every multiple of f).
#   - Treat integers as nodes in an implicit graph, linked to v-1, v+1,
#     2v, 3v, v/2 (if even), v/3 (if divisible by 3).
#   - Process the array left to right. For each value x, look at the
#     best score already recorded (best_for_value) among its linked
#     neighbors, add x's own divisor count, and store that as the best
#     score reachable at x. Track the running maximum as the answer.
#
# Time complexity:  O(cap * log(cap) + n)
#   - Sieve construction dominates: O(cap log cap)
#   - Each array element does O(1) neighbor lookups (6 candidates)
#
# Space complexity: O(cap)
#   - div_count[] and best_for_value[] arrays sized to `cap`


# ----------------------- Solution -------------------------


import sys

def compute_divisor_counts(limit):
    counts = [0] * (limit + 1)
    for factor in range(1, limit + 1):
        for multiple in range(factor, limit + 1, factor):
            counts[multiple] += 1
    return counts

def linked_values(v, cap):
    candidates = []
    if v - 1 >= 1:
        candidates.append(v - 1)
    if v + 1 <= cap:
        candidates.append(v + 1)
    if 2 * v <= cap:
        candidates.append(2 * v)
    if 3 * v <= cap:
        candidates.append(3 * v)
    if v % 2 == 0:
        candidates.append(v // 2)
    if v % 3 == 0:
        candidates.append(v // 3)
    return candidates

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))
    cap = 100000
    if arr:
        cap = max(cap, max(arr))
    div_count = compute_divisor_counts(cap)
    best_for_value = [0] * (cap + 1)
    top_score = 0
    for x in arr:
        incoming_best = 0
        for nb in linked_values(x, cap):
            bv = best_for_value[nb]
            if bv > incoming_best:
                incoming_best = bv
        score_here = div_count[x] + incoming_best
        if score_here > best_for_value[x]:
            best_for_value[x] = score_here
        if score_here > top_score:
            top_score = score_here
    print(top_score)

if __name__ == "__main__":
    main()
