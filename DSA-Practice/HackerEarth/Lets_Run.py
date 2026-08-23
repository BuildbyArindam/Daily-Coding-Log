"""
Problem   : Let's Run
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/lets-run/
Difficulty: Easy
Topic     : Modular Arithmetic / Geometric Progression
Date      : 2026-08-23

Approach:
Displacement per interval forms a geometric progression with ratio r = -n (mod C),
since direction flips/scales each step. Sum the full periods (k = T // dt) using
the closed-form geometric series sum (with a modular inverse for the ratio-minus-one
term, and a special case when r == 1 mod C), then add the leftover partial interval
(rem = T % dt) scaled by r^k. Final answer is the shorter arc distance:
min(disp, C - disp), all done under mod C = 1e9+7.

Complexity:
Time : O(Q log k)   -- per query, dominated by modular exponentiation (pow)
Space: O(1) extra per query (O(Q) for the output buffer)
"""


# ---------------------------- Solution ---------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    q = int(data[0])
    results = []
    C = 10**9 + 7
    idx = 1
    for _ in range(q):
        v = int(data[idx])
        dt = int(data[idx + 1])
        n = int(data[idx + 2])
        T = int(data[idx + 3])
        idx += 4
        k = T // dt
        rem = T % dt
        total_disp = 0
        if k > 0:
            r = -n % C
            if (r - 1) % C == 0:
                S_k = k % C
            else:
                num = (pow(r, k, C) - 1) % C
                den_inv = pow(r - 1, C - 2, C)
                S_k = (num * den_inv) % C
            term_full = (v % C) * (dt % C) % C
            term_full = (term_full * S_k) % C
            total_disp = (total_disp + term_full) % C
        if rem > 0:
            term_rem = (v % C) * (rem % C) % C
            factor = pow(-n % C, k, C)
            term_rem = (term_rem * factor) % C
            total_disp = (total_disp + term_rem) % C
        min_dist = min(total_disp, C - total_disp)
        results.append(str(min_dist))
    print("\n".join(results))

if __name__ == "__main__":
    solve()
