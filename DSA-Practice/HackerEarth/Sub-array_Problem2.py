"""
Problem: Sub-array Problem
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/sub-array-problem-1/
Date Solved: 2026-09-25
Difficulty: Easy
Topics: Sieve of Eratosthenes, Sliding Window

Approach:
Precompute primality up to max(arr) using a sieve. Then use a variable-size
sliding window: expand window_end, track count of primes in the window
(prime_tally), and shrink window_start whenever prime_tally exceeds k.
For each window_end, add (window_end - window_start + 1) to total — this
counts all subarrays ending at window_end whose prime count is <= k.

Time Complexity: O(n log log m + n), where m = max(arr) (sieve + single-pass window)
Space Complexity: O(m) for the sieve flags
"""


# ----------------------------------------- Solution ----------------------------------------------


import sys

def build_prime_flags(upper_bound):
    if upper_bound < 2:
        return bytearray(upper_bound + 1)
    flags = bytearray([1]) * (upper_bound + 1)
    flags[0] = flags[1] = 0
    p = 2
    while p * p <= upper_bound:
        if flags[p]:
            step = p
            start = p * p
            flags[start:upper_bound + 1:step] = bytearray(
                len(flags[start:upper_bound + 1:step])
            )
        p += 1
    return flags

def count_subarrays_with_bounded_primicity(values, limit):
    highest_value = max(values) if values else 0
    prime_flags = build_prime_flags(highest_value)
    total = 0
    window_start = 0
    prime_tally = 0
    for window_end, current_val in enumerate(values):
        if prime_flags[current_val]:
            prime_tally += 1
        while prime_tally > limit:
            if prime_flags[values[window_start]]:
                prime_tally -= 1
            window_start += 1
        total += window_end - window_start + 1
    return total

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    arr = [int(data[idx + i]) for i in range(n)]
    result = count_subarrays_with_bounded_primicity(arr, k)
    print(result)

if __name__ == "__main__":
    main()
