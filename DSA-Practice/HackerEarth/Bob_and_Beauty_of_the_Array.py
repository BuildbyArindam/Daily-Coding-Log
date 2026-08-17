"""
Problem   : Bob and Beauty of the Array
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/bob-and-beauty-of-the-array-3b35ef14/
Date      : 2026-08-17
Difficulty: Medium
Topics    : Basic Programming, Implementation, Hash Maps

Approach:
    - Sort array, group into unique values with their frequencies.
    - "Beauty" of a subsequence = OR of its min and max element.
      Sum this over all subsequences of size >= 2.
    - Split into two cases:
        1. Same-value subsequences (min == max): for a value with
           count `cnt`, number of subsets of size >= 2 drawn from
           those cnt equal elements is (2^cnt - cnt - 1). Contributes
           val * ways (since val | val == val).
        2. Cross-value subsequences: for each pair of distinct values
           (prev_val as min, val as max), count subsequences where:
             - at least one copy of prev_val is included,
             - at least one copy of val is included,
             - any subset of the "middle" elements (values strictly
               between prev_val and val) can be freely included.
           Ways = (2^prev_cnt - 1) * (2^cnt - 1) * 2^(middle_count).
           `pre_factor[p_idx]` accumulates the running middle-element
           count between each earlier value and the current one.

Time Complexity : O(n^2) worst case (nested loop over unique values
                   when all elements are distinct).
Space Complexity: O(n) for frequency map, prefix powers, and pre_factor array.
"""


-------------------- Solution -------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    MOD = 1000000007
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow2[i] = (pow2[i - 1] * 2) % MOD
    arr.sort()
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    unique_vals = sorted(freq.keys())
    total_beauty = 0
    for val in unique_vals:
        cnt = freq[val]
        if cnt >= 2:
            ways = (pow2[cnt] - cnt - 1) % MOD
            total_beauty = (total_beauty + (val | val) * ways) % MOD
    accumulated_prefix = 0
    for val in unique_vals:
        cnt = freq[val]
        if accumulated_prefix > 0:
            ways_y = pow2[cnt] - 1
            ways_pair = (accumulated_prefix * ways_y) % MOD
        current_contrib = (pow2[cnt] - 1) * pow2[accumulated_prefix] 
        accumulated_prefix += cnt
    total_beauty = 0
    pre_factor = [0] * len(unique_vals)
    running_elements = 0
    for idx, val in enumerate(unique_vals):
        cnt = freq[val]
        if cnt >= 2:
            ways = (pow2[cnt] - cnt - 1) % MOD
            total_beauty = (total_beauty + val * ways) % MOD
        ways_max = pow2[cnt] - 1
        for p_idx in range(idx):
            prev_val = unique_vals[p_idx]
            prev_cnt = freq[prev_val]
            ways_min = pow2[prev_cnt] - 1
            ways_mid = pow2[pre_factor[p_idx]]
            total_ways = (ways_min * ways_max) % MOD
            total_ways = (total_ways * ways_mid) % MOD
            total_beauty = (total_beauty + (prev_val | val) * total_ways) % MOD
            pre_factor[p_idx] += cnt
        pre_factor[idx] = 0
    print(total_beauty % MOD)

if __name__ == '__main__':
    solve()
