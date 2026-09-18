"""
Problem   : Remainder Twist
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/remainder-twist-987a698c/
Date      : 2026-09-18
Difficulty: Hard
Topics    : Algorithms, Binary Search

Approach:
    For a threshold x, define F(x) as the total count (summed over all
    b in (x, N]) of numbers a in [1, N] whose remainder a % b is >= x.
    F(x) is monotonically non-increasing as x increases, so the largest
    x with F(x) >= R can be found via binary search on x in [0, N-1].
    For each candidate x, F(x) is computed in O(N) by iterating b from
    x+1 to N and using divmod to count qualifying remainders per block
    in O(1), with early exit once the running total reaches R.
    If R exceeds N*N (the maximum possible F(0)), the answer is -1.

Time complexity : O(N log N) per test case (O(log N) binary search
                   iterations x O(N) per possible() call)
Space complexity: O(1) auxiliary
"""


# ------------------------------------- Solution --------------------------------------


import sys

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    for _ in range(T):
        N, R = map(int, input().split())
        if R > N * N:
            print(-1)
            continue
        def possible(x):
            """Return True if F(x) >= R."""
            if x == 0:
                return True
            total = 0
            for b in range(x + 1, N + 1):
                q, rem = divmod(N, b)
                cnt = q * (b - x)
                if rem >= x:
                    cnt += rem - x + 1
                total += cnt
                if total >= R:
                    return True
            return False
        lo, hi = 0, N - 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if possible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        print(ans)

if __name__ == "__main__":
    solve()
