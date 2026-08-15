"""
Problem   : B. A Prosperous Lot
Platform  : Codeforces
Link      : https://codeforces.com/contest/934/problem/B
Date      : 2026-08-15
Topic     : Constructive Algorithms, Implementation (*1200)

Approach:
  Each digit contributes a fixed number of "loops": digit 8 -> 2 loops,
  digits 0/4/6/9 -> 1 loop, digits 1/2/3/5/7 -> 0 loops.
  Since n <= 10^18, max digit count is 18, so max achievable loops = 36.
  - If k > 36: impossible, print -1.
  - Else: use (k // 2) copies of '8' to cover pairs of loops, and if k is
    odd, append one '6' to cover the leftover single loop.
  This greedily minimizes digit count while satisfying the loop count exactly.

Complexity:
  Time  : O(k) - string built with at most 18 characters
  Space : O(k) - output string storage
"""


# ------------------------- Solution --------------------------------


import sys

def solve():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    k = int(input_data)
    if k > 36:
        print(-1)
        return
    eights = k // 2
    rem = k % 2
    ans = '8' * eights
    if rem == 1:
        ans += '6'
    print(ans)

if __name__ == "__main__":
    solve()
