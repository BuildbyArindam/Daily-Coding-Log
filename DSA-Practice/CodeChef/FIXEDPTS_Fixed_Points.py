"""
Problem   : Fixed Points
Platform  : CodeChef (START256D)
Link      : https://www.codechef.com/START256D/problems/FIXEDPTS
Date      : 2026-09-16
Difficulty: Easy 
Topics    : Math, Combinatorics, Permutations

Approach:
    For a permutation of length n, exactly k fixed points is achievable
    for any 0 <= k <= n EXCEPT:
      - k == n - 1  (leaving exactly one non-fixed element is impossible,
                      since the last element has nowhere else to go)
      - n == 1 and k == 0 (the only permutation of size 1 is fixed)
    All other (n, k) pairs are constructible (fix k elements, derange the rest).

Time complexity : O(1) per test case  ->  O(T) overall
Space complexity: O(1) extra (excluding input buffering)
"""


# ------------------------------ Solution -------------------------------------


import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out_lines = []
    for _ in range(t):
        n = int(data[idx]); k = int(data[idx+1]); idx += 2
        possible = True
        if n - k == 1:
            possible = False
        elif n == 1 and k == 0:
            possible = False
        out_lines.append("Yes" if possible else "No")
    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
