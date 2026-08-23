"""
Problem   : Noldbach Problem
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/17/A
Difficulty: *1000
Topics    : Brute Force, Math, Number Theory
Date      : 2026-08-23

Approach:
Sieve of Eratosthenes up to n to mark primes. Collect all primes <= n.
For each pair of consecutive primes (p_i, p_i+1), check if p_i + p_i+1 + 1
is itself prime and <= n — such pairs are "Noldbach pairs". Count them and
compare against k.

Complexity:
Time  : O(n log log n) for sieve + O(pi(n)) for pair scan  ->  O(n log log n)
Space : O(n) for the is_prime sieve array
"""


# ------------------------------- Solution ----------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    count = 0
    for i in range(len(primes) - 1):
        candidate = primes[i] + primes[i + 1] + 1
        if candidate <= n and is_prime[candidate]:
            count += 1
    if count >= k:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
