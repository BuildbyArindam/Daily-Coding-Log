"""
Problem   : Ceiling Sum (CEILSUM)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CEILSUM
Difficulty: 1712
Topics    : Basic Math, Parity, Ceiling Division, Constructive Algorithms

Approach:
  For given A, B (A <= B), consider f(x) = ceil((B-x)/2) + ceil((x-A)/2)
  for x in [A, B]. The problem's answer is the MAXIMUM value f(x) can take
  over that range. f is piecewise and "zig-zags" by at most 1 as x moves,
  taking its largest value near the midpoint of [A, B].

  Closed form used here:
    base = ceil((B-A)/2) = (D + 1) // 2   where D = B - A
    if A != B and A, B have the same parity (D is even and D > 0):
        base += 1   # midpoint split is uneven, so the true max is one higher

  This avoids the O(1)-per-x binary search / brute force some editorial
  solutions use, by folding the two candidate x's (mid, mid+1) into one
  parity check.

Time complexity : O(1) per test case, O(T) overall
Space complexity: O(1)
"""


# ----------------------------------- Solution -----------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        D = B - A
        ans = (D + 1) // 2
        if A != B and (A % 2 == B % 2):
            ans += 1
        print(ans)

if __name__ == "__main__":
    solve()
