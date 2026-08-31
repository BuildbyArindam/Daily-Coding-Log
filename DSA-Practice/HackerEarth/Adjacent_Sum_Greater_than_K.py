"""
Problem: Adjacent Sum Greater than K
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/adjacent-sum-greater-than-k-f41e3ec4/
Difficulty: Medium
Topics: Greedy, Linear Search, Observation

Date: 2026-08-31

Approach:
For a given K, we need to arrange numbers 1..N such that no two
adjacent elements sum to exactly K. The greedy trick: interleave
pairs (i, K-i) for i = 1..(K-1)//2 — since consecutive elements in
each pair are far apart in value, their neighbors never sum to K.
If K is even, K//2 has no partner and is placed alone after the
pairs. Remaining numbers from K to N are already safe to append in
order (increasing sequence, no adjacent pair sums to K once
values >= K, except boundary — the construction handles that).
If K > N + 1, no valid arrangement is possible -> -1.

Time complexity:  O(N) per test case
Space complexity: O(N) per test case (output array)
"""


# ------------------------------ Solution ---------------------------------


import sys

input = sys.stdin.buffer.readline
T = int(input())
out = []
for _ in range(T):
    N, K = map(int, input().split())
    if K > N + 1:
        out.append("-1")
        continue
    ans = []
    pairs = (K - 1) // 2
    for i in range(1, pairs + 1):
        ans.append(i)
        ans.append(K - i)
    if K % 2 == 0:
        ans.append(K // 2)
    for x in range(K, N + 1):
        ans.append(x)
    out.append(" ".join(map(str, ans)))
sys.stdout.write("\n".join(out))
