"""
Problem   : Count MEX
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/count-mex-8dd2c00c/
Difficulty: Medium
Topics    : Algorithms, Greedy Algorithm, Linear Search
Date      : 2026-09-02

Approach:
For a permutation P of 1..N, precompute pos[v] = index of value v.
The MEX of a subarray [l, r] is k iff values 1..k-1 all lie within
[l, r] and value k does not. So for each k, maintain the running
window [L, R] = [min(pos[1..k-1]), max(pos[1..k-1])] that must be
fully contained in [l, r]. The count of subarrays whose MEX is
exactly k is the number of ways to extend [L, R] outward on
whichever side excludes pos[k] without including pos[k] itself:
  - if pos[k] < L: left endpoint l can range in (pos[k], L],
    right endpoint r can range in [R, N] -> (L - pos[k]) * (N - R + 1)
  - if pos[k] > R: symmetric on the right -> L * (pos[k] - R)
  - if pos[k] is inside [L, R]: impossible to exclude it, so 0
    subarrays have MEX exactly k
MEX = N is a special case: only the full array [1, N] has it, so 1.

Time complexity : O(N) per test case
Space complexity: O(N) for the pos[] array
"""


# --------------------------- Solution -----------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        pos = [0] * N
        for i, x in enumerate(P, 1):
            pos[x] = i
        ans = []
        L = R = pos[0]
        for k in range(1, N):
            pk = pos[k]
            if pk < L:
                left_choices = L - pk
                right_choices = N - R + 1
                ans.append(left_choices * right_choices)
            elif pk > R:
                left_choices = L
                right_choices = pk - R
                ans.append(left_choices * right_choices)
            else:
                ans.append(0)
            L = min(L, pk)
            R = max(R, pk)
        ans.append(1)
        print(*ans)

if __name__ == "__main__":
    solve()
