"""
Problem   : Monochrome Cut (CIRCUT)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CIRCUT
Date      : 2026-08-28
Difficulty: Simple / Cakewalk-Easy
Topics    : Ad-hoc, Greedy, Sorting, Cyclic Traversal, Block Grouping

Approach:
  Points sit on a circle with values (A) and colors (S). Any run of
  consecutive same-colored points must stay together in a group no
  matter where the cuts are made, so only the maximum of each such
  "block" matters. The best achievable score is always the sum of
  the two largest block maxima.
  Shortcut: the block containing the global max A[p] is guaranteed
  to be one of the top two, so we only need to:
    1. Find the global max and expand left/right while the color
       stays the same to get that block's full range.
    2. Scan every index OUTSIDE that range for the next largest
       value (the second block maximum).
  Sum of the two = answer.

Complexity:
  Time  : O(N) per test case (each index visited O(1) times total)
  Space : O(1) extra (excluding input storage)
"""


# ---------------------------- Solution ----------------------------------


import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    it = iter(input_data)
    T = int(next(it))
    ans = []
    for _ in range(T):
        n = int(next(it))
        A = [int(next(it)) for _ in range(n)]
        S = next(it) 
        mx = max(A)
        p = A.index(mx)
        color = S[p]
        left = p
        while S[(left - 1) % n] == color:
            left = (left - 1) % n
        right = p
        while S[(right + 1) % n] == color:
            right = (right + 1) % n
        second = 0
        if left <= right:
            for i in range(n):
                if not (left <= i <= right):
                    if A[i] > second:
                        second = A[i]
        else:
            for i in range(right + 1, left):
                if A[i] > second:
                    second = A[i]
        ans.append(str(mx + second))
    sys.stdout.write("\n".join(ans))
    
if __name__ == "__main__":
    solve()
