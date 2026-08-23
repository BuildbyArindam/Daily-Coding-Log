"""
Problem   : Finding the Subarrays
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/counting-the-subarrays-4187713a/
Difficulty: Easy
Topic     : Arrays, Data Structures, One-dimensional
Date      : 2026-08-23

Approach:
  Build a prefix sum array so any subarray sum is O(1) to compute.
  For every subarray [i, j], compare its average to the average of the
  remaining elements by cross-multiplying (sub_sum * rem_len vs
  rem_sum * sub_len) to avoid floating-point division. Collect all
  (i, j) pairs where the subarray's average strictly exceeds the rest.

Complexity:
  Time : O(n^2)  — every (i, j) pair is checked explicitly
  Space: O(n)    — prefix sum array (output list is extra, size-dependent)

Note: O(n^2) is fine for Easy-tier constraints here, but if n gets large
      (~10^5+), this needs a smarter approach (e.g. reduce to comparing
      sub_sum * n vs total_sum * sub_len, which is the same check but
      still O(n^2) in the worst case for enumerating all pairs — true
      sub-quadratic solutions would need extra structure).
"""


# ------------------------ Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : n + 1]]
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
    total_sum = pref[n]
    results = []
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            sub_len = j - i + 1
            sub_sum = pref[j] - pref[i - 1]
            rem_len = n - sub_len
            rem_sum = total_sum - sub_sum
            if rem_len == 0:
                if sub_sum > 0:
                    results.append((i, j))
            else:
                if sub_sum * rem_len > rem_sum * sub_len:
                    results.append((i, j))
    print(len(results))
    for l, r in results:
        print(f"{l} {r}")

if __name__ == "__main__":
    solve()
