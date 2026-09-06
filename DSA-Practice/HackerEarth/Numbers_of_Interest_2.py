"""
Problem   : Numbers of Interest 2
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/numbers-of-interest-2-1/
Difficulty: Medium
Topics    : Algorithms, Math, Number Theory (SPF Sieve, Sigma Function)
Date      : 2026-09-06

Approach:
    For each n, define f(n) = smallest prime factor of n, and g(n) = sigma(n) - n
    (sum of divisors of n excluding n itself). The answer for a query n is
    (sum of f(i) for i=1..n + sum of g(i) for i=1..n) % n.

    - Build a smallest-prime-factor (SPF) sieve up to max query value in O(N log log N).
    - Use the SPF sieve to compute sigma(n) (sum of divisors) for every n in O(N),
      via the multiplicative recurrence sigma(n) = sigma(m) * (p+1) when n = p*m,
      p prime, p not dividing m; or sigma(n) = sigma(m) + p*(sigma(m) - sigma(m/p))
      when p | m.
    - Precompute running prefix sums of f and g while iterating once from 2 to max_n,
      answering each query as it's reached.

Time complexity : O(N log log N) for the sieve + O(N) for sigma/prefix sums,
                   where N = max query value. Overall O(N log log N).
Space complexity : O(N) for spf[], sigma[] arrays.
"""


# ------------------------------- Solution ------------------------------------


name = input() 
T = int(name)
queries = []
for _ in range(T):
    queries.append(int(input()))
max_n = max(queries)
answers = {}
if max_n == 1:
    for n in queries:
        answers[n] = 0
else:
    spf = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= max_n:
                for j in range(i * i, max_n + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
    sigma = [0] * (max_n + 1)
    sigma[1] = 1
    for n in range(2, max_n + 1):
        p = spf[n]
        m = n // p
        if m % p == 0:
            sigma[n] = sigma[m] + p * (sigma[m] - sigma[m // p])
        else:
            sigma[n] = sigma[m] * (p + 1)
    needed = set(queries)
    f_sum = 0  
    g_sum = 0   
    if 1 in needed:
        answers[1] = 0
    for n in range(2, max_n + 1):
        f_sum += spf[n]
        y = sigma[n] - n
        g_sum += y
        if n in needed:
            answers[n] = (f_sum + g_sum) % n
for n in queries:
    print(answers[n])
