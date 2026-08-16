"""
Problem   : Equal Median
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/equal-median-8aba723b/
Difficulty: Medium
Topic     : Basic Programming / Basics of Implementation / Implementation
Date      : 2026-08-16

Approach:
    - For N elements each in arrays A and B, want min swaps (A[i] <-> B[i])
      so that both arrays share a common median value x, chosen from the
      union of values present in A and B.
    - For each candidate median x, classify every element of A and B into
      Less / Equal / Greater relative to x, then compute the counts of
      Less (L), Equal (E), Greater (G) needed in the FINAL array A so both
      A and B end up with median == x (using the standard "median = x"
      feasibility bounds on L/G counts for an array of size N).
    - The feasible region for (L, G) is bounded by four inequalities from
      the median-position constraints; each boundary is represented as a
      line, and the optimal integer point minimizing swaps is found by
      intersecting bounding lines pairwise (small constant number of
      line pairs) and checking feasibility, rather than brute-forcing all
      (L, G) pairs.
    - Swaps needed for a given feasible (L, G, E) target = sum of
      shortfalls versus A's current L/G/E counts (only counting elements
      that must move FROM B TO A, since a swap fixes one position).
    - Answer = min swaps across all candidate median values x.

Complexity:
    - Time : O(N log N) per test case (sorting A, B, and candidate values,
      plus O(1) line intersections per candidate value).
    - Space: O(N) for sorted arrays and candidate value list.
"""


# --------------------- Solution----------------------

import sys
from bisect import bisect_left, bisect_right

def solve_case(N, A, B):
    m = N // 2
    A.sort()
    B.sort()
    INF = 10**30
    answer = INF
    for x in sorted(set(A + B)):
        la = bisect_left(A, x)
        ra = bisect_right(A, x)
        aL = la
        aE = ra - la
        aG = N - ra
        lb = bisect_left(B, x)
        rb = bisect_right(B, x)
        bL = lb
        bE = rb - lb
        bG = N - rb
        totalL = aL + bL
        totalE = aE + bE
        totalG = aG + bG
        if totalE < 2:
            continue
        if totalL > N - 1 or totalG > N - 1:
            continue
        l0 = max(0, totalL - m)
        l1 = min(m, totalL)
        g0 = max(0, totalG - m)
        g1 = min(m, totalG)
        s0 = N - totalE + 1
        s1 = N - 1
        if l0 > l1 or g0 > g1:
            continue
        if max(l0 + g0, s0) > min(l1 + g1, s1):
            continue
        if (
            l0 <= aL <= l1
            and g0 <= aG <= g1
            and s0 <= aL + aG <= s1
        ):
            answer = 0
            continue 
        lines = [
            (1, 0, l0),
            (1, 0, l1),
            (0, 1, g0),
            (0, 1, g1),
            (1, 1, s0),
            (1, 1, s1),
            (1, 0, aL),       
            (0, 1, aG),       
            (1, 1, aL + aG)  
        ]
        best_for_x = INF
        for i in range(len(lines)):
            a, b, c = lines[i]
            for j in range(i + 1, len(lines)):
                d, e, f = lines[j]
                det = a * e - b * d
                if det == 0:
                    continue
                l_num = c * e - b * f
                g_num = a * f - c * d
                l = l_num // det
                g = g_num // det
                if not (l0 <= l <= l1):
                    continue
                if not (g0 <= g <= g1):
                    continue
                if not (s0 <= l + g <= s1):
                    continue
                e_count = N - l - g
                swaps = (
                    max(l - aL, 0)
                    + max(g - aG, 0)
                    + max(e_count - aE, 0)
                )
                best_for_x = min(best_for_x, swaps)
        answer = min(answer, best_for_x)
    return -1 if answer == INF else answer

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        print(solve_case(N, A, B))

if __name__ == "__main__":
    main()
  
