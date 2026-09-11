"""
Problem: Naruto and His New Jutsu
Platform: HackerEarth
Link: https://www.hackerearth.com/problem/algorithm/naruto-and-divisors-1d0e45cc/
Difficulty: Easy
Topic: Mathematics, Divisors

Date Solved: 2026-09-11

Approach:
    For each query n, strip all factors of 2 (since we only care about
    odd divisors), then find the prime factorization of the remaining
    odd part using a precomputed sieve of primes up to sqrt(10^9) ≈ 31623.
    For each prime factor p with exponent e, the sum of its contributions
    to divisor sums is (1 + p + p^2 + ... + p^e), computed incrementally.
    Multiply these across all prime factors (multiplicative property of
    the divisor-sum function) to get the total sum of odd divisors.

Time Complexity:
    Sieve: O(LIMIT log log LIMIT) done once.
    Per query: O(sqrt(n) / ln(sqrt(n))) in the worst case (trial division
    over the prime list up to sqrt(n)).
    Overall: O(LIMIT log log LIMIT + T * sqrt(n) / ln(sqrt(n)))

Space Complexity:
    O(LIMIT) for the sieve and prime list.
"""


# ------------------------------- Solution -----------------------------------------


import sys
import math
LIMIT = 31623
is_prime = [True] * (LIMIT + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(LIMIT)) + 1):
    if is_prime[i]:
        for j in range(i * i, LIMIT + 1, i):
            is_prime[j] = False
primes = [i for i in range(2, LIMIT + 1) if is_prime[i]]

def sum_of_odd_divisors(n):
    while n % 2 == 0:
        n //= 2
    result = 1
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            power_sum = 1
            power = 1
            while n % p == 0:
                n //= p
                power *= p
                power_sum += power
            result *= power_sum
    if n > 1:
        result *= (1 + n)
    return result

def main():
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    answers = []
    for i in range(1, T + 1):
        n = int(input_data[i])
        answers.append(str(sum_of_odd_divisors(n)))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
