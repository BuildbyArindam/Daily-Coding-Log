"""
Problem: Maximize Array Function
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/approximate/maximize-array-function-2-e692ab46/
Platform: HackerEarth
Date Solved: 2026-09-25
Difficulty: Medium
Topics: Arrays, Data Structures, 1-D

Approach:
    Given a fixed window [lo, hi] of length L in a permutation of 1..n, choose which
    L values occupy that window to maximize (L * window_sum) / (1 + window_xor).
    Start from a greedy seed (top-L values by magnitude), then refine with randomized
    local search: repeatedly swap one "inside" and one "outside" element if the swap
    improves the ratio, until a time budget (~0.85s) is exhausted. Remaining positions
    (outside the window) are filled with the leftover values in shuffled order, since
    their arrangement doesn't affect the scored window.

Time Complexity:  O(n log n) for the initial sort + O(k) local-search iterations
                   bounded by the time budget, each O(1) per swap trial.
Space Complexity: O(n) for storing values, index sets, and the output permutation.
"""


# ------------------------------------------ Solution ------------------------------------------------------


import sys
import random
import time

def read_input():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr]); ptr += 1
    lo = int(data[ptr]); ptr += 1
    hi = int(data[ptr]); ptr += 1
    vals = [int(data[ptr + i]) for i in range(n)]
    return n, lo, hi, vals

def score_ratio(window_sum, window_xor, window_len):
    return (window_len * window_sum) / (1.0 + window_xor)

def build_window_via_local_search(values, window_len, deadline):
    n = len(values)
    order_by_value = sorted(range(n), key=lambda idx: values[idx], reverse=True)
    inside = set(order_by_value[:window_len])
    outside = set(order_by_value[window_len:])
    running_sum = sum(values[idx] for idx in inside)
    running_xor = 0
    for idx in inside:
        running_xor ^= values[idx]
    best_ratio = score_ratio(running_sum, running_xor, window_len)
    inside_list = list(inside)
    outside_list = list(outside)
    if not outside_list or not inside_list:
        return inside
    rng = random.Random(12345)
    checked = 0
    while True:
        checked += 1
        if checked % 256 == 0 and time.time() >= deadline:
            break
        i_pos = rng.randrange(len(inside_list))
        o_pos = rng.randrange(len(outside_list))
        leaving_idx = inside_list[i_pos]
        entering_idx = outside_list[o_pos]
        candidate_sum = running_sum - values[leaving_idx] + values[entering_idx]
        candidate_xor = running_xor ^ values[leaving_idx] ^ values[entering_idx]
        candidate_ratio = score_ratio(candidate_sum, candidate_xor, window_len)
        if candidate_ratio > best_ratio:
            inside_list[i_pos] = entering_idx
            outside_list[o_pos] = leaving_idx
            running_sum = candidate_sum
            running_xor = candidate_xor
            best_ratio = candidate_ratio
    return set(inside_list)

def assemble_permutation(n, lo, hi, chosen_zero_based):
    leftover = [idx for idx in range(n) if idx not in chosen_zero_based]
    rng = random.Random(999)
    rng.shuffle(leftover)
    before_count = lo - 1
    before_part = leftover[:before_count]
    after_part = leftover[before_count:]
    window_part = list(chosen_zero_based)
    b = [0] * n
    for pos, zero_idx in zip(range(1, lo), before_part):
        b[pos - 1] = zero_idx + 1
    for pos, zero_idx in zip(range(lo, hi + 1), window_part):
        b[pos - 1] = zero_idx + 1
    for pos, zero_idx in zip(range(hi + 1, n + 1), after_part):
        b[pos - 1] = zero_idx + 1
    return b

def main():
    start = time.time()
    n, lo, hi, values = read_input()
    window_len = hi - lo + 1
    deadline = start + 0.85
    if window_len == n:
        chosen = set(range(n))
    else:
        chosen = build_window_via_local_search(values, window_len, deadline)
    b = assemble_permutation(n, lo, hi, chosen)
    sys.stdout.write(' '.join(map(str, b)) + '\n')

if __name__ == '__main__':
    main()
