"""
Problem   : Even Odd Queries
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/even-odd-queries-f52d76e2/
Difficulty: Easy
Topic     : Ad-Hoc, Implementation
Date      : 2026-08-20

Approach:
    Precompute a prefix-sum array `pref_even` where pref_even[i] = count of
    even numbers in arr[0..i-1]. For each query (K, L, R):
      - total_elements = R - L + 1
      - even_count = pref_even[R] - pref_even[L-1]
      - p = even_count if K == 0 (even) else (total_elements - even_count)
      - q = total_elements
      - Reduce p/q by gcd; print "0" if p == 0, "1" if p == q, else "p q".

Time Complexity : O(N + Q) per test case
                   (O(N) to build prefix sums, O(1) per query + O(log(min(p,q))) for gcd)
Space Complexity: O(N) for the prefix-sum array
"""


# ------------------------------- Solution ---------------------------------


import sys
import math

def solve():
    input_iter = iter(sys.stdin.read().splitlines())
    try:
        line = next(input_iter)
    except StopIteration:
        return
    T = int(line.strip())
    out = []
    for _ in range(T):
        line = next(input_iter).split()
        while not line:
            line = next(input_iter).split()
        N, Q = int(line[0]), int(line[1])
        arr_values = []
        while len(arr_values) < N:
            arr_values.extend(next(input_iter).split())
        pref_even = [0] * (N + 1)
        for i in range(1, N + 1):
            val = int(arr_values[i - 1])
            pref_even[i] = pref_even[i - 1] + (1 if val % 2 == 0 else 0)
        del arr_values
        for _ in range(Q):
            q_line = next(input_iter).split()
            while not q_line:
                q_line = next(input_iter).split()
            K, L, R = int(q_line[0]), int(q_line[1]), int(q_line[2])
            total_elements = R - L + 1
            even_count = pref_even[R] - pref_even[L - 1]
            p = even_count if K == 0 else (total_elements - even_count)
            q = total_elements
            if p == 0:
                out.append("0")
            else:
                common = math.gcd(p, q)
                p //= common
                q //= common
                if p == q:
                    out.append("1")
                else:
                    out.append(f"{p} {q}")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
