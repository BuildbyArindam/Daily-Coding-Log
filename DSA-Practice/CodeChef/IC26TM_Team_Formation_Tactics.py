"""
Platform   : CodeChef (ICPC OL 26 Postround)
Problem    : Team Formation Tactics (IC26TM)
Link       : https://www.codechef.com/ICPCOL26POST/problems/IC26TM
Date       : 2026-10-06
Difficulty : ~1900 (Medium)
Topics     : Greedy, Sorting, Binary Search, Prefix Sums

Approach:
  - Sort the 3N values in descending order and build prefix sums.
  - Enumerate `a`, the number of elements taking the highest-weight role.
  - For each `a`, binary search `b`, the number of pairs worth taking.
    The marginal gain of adding one more pair is non-increasing, so the
    first non-positive gain marks the optimum.
  - Evaluate each (a, b) in O(1) with prefix sums and keep the maximum.

Complexity:
  Time  : O(N log N) per test case (sort + N binary searches over O(log N))
  Space : O(N)
"""


# ---------------------------------------- Solution ------------------------------------------------------


import sys

def main():
    rd = sys.stdin.buffer.read().split()
    ptr = 0
    T = int(rd[ptr]); ptr += 1
    res = []
    while T:
        T -= 1
        n = int(rd[ptr]); ptr += 1
        m = 3 * n
        arr = sorted(map(int, rd[ptr:ptr + m]), reverse=True)
        ptr += m
        pre = [0] * (m + 1)
        run = 0
        for idx in range(m):
            run += arr[idx]
            pre[idx + 1] = run
        top = 0
        for a in range(n + 1):
            lo, hi = 0, n - a   
            while lo < hi:
                mid = (lo + hi) >> 1
                gain = arr[a + 2 * mid] + arr[a + 2 * mid + 1] \
                       - 3 * arr[m - 2 * a - mid - 1]
                if gain > 0:
                    lo = mid + 1
                else:
                    hi = mid
            b = lo
            val = 2 * pre[a] + pre[a + 2 * b] + 3 * pre[m - 2 * a - b]
            if val > top:
                top = val
        res.append(top)
    sys.stdout.write("\n".join(map(str, res)) + "\n")

main()
