"""
Problem: Sub-array Problem
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/sub-array-problem-1/
Date: 2026-09-22
Difficulty: Easy
Topics: Two Pointers / Sliding Window, Sieve of Eratosthenes

Approach:
    1. Sieve all primes up to max(A) using a bytearray sieve.
    2. Use a variable-size sliding window [left, right]; expand `right`
       and count primes in the window; whenever prime_count exceeds K,
       shrink from `left` until it's valid again.
    3. For each `right`, every subarray ending at `right` and starting
       anywhere in [left, right] is valid, so add (right - left + 1)
       to the answer.

Time Complexity:  O(N + max_val log log max_val)  -- sieve + one pass two-pointer
Space Complexity: O(max_val)                       -- sieve array
"""


# -------------------------------------- Solution --------------------------------------


import sys

data = list(map(int, sys.stdin.buffer.read().split()))
N = data[0]
K = data[1]
A = data[2:2 + N]
max_val = max(A)
is_prime = bytearray(b'\x01') * (max_val + 1)
if max_val >= 0:
    is_prime[0] = 0
if max_val >= 1:
    is_prime[1] = 0
p = 2
while p * p <= max_val:
    if is_prime[p]:
        start = p * p
        count = (max_val - start) // p + 1
        is_prime[start:max_val + 1:p] = b'\x00' * count
    p += 1
left = 0
prime_count = 0
answer = 0
for right in range(N):
    if is_prime[A[right]]:
        prime_count += 1
    while prime_count > K:
        if is_prime[A[left]]:
            prime_count -= 1
        left += 1
    answer += right - left + 1
print(answer)
