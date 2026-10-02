"""
Problem   : Sub-array Problem
Platform  : HackerEarth (Easy)
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/sub-array-problem-1/
Date      : 2026-10-02
Topics    : Sliding Window, Two Pointers, Sieve of Eratosthenes

Approach  : Count the subarrays that contain at most K prime numbers.
            1. Build a prime sieve up to max(A) with a bytearray, using
               slice assignment to mark composites.
            2. Slide a window [left, right]. When the prime count exceeds K,
               advance `left` until the window is valid again.
            3. Every right endpoint adds (right - left + 1) valid subarrays
               ending at `right`.

Time      : O(M log log M + N), where M = max(A)
Space     : O(M + N)
"""


# ----------------------------------- Solution ------------------------------------------------------


import sys

def solve():
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

if __name__ == "__main__":
    solve()
