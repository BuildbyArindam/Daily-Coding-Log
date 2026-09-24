"""
Problem   : Make Distinct (MAKEDISTK)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MAKEDISTK
Difficulty: 1702
Date      : 2026-09-24
Topics    : Greedy, Sorting, Math

Approach:
    Sort the array, then greedily lift each element to max(a[i], prev + 1).
    This gives the minimum total increments needed for distinctness.
    Let `total` = sum of all increments and `max_inc` = largest increment on
    any single element.
    - Each operation raises an element by at most 1, so the answer is
      at least max_inc.
    - Each operation touches at most K elements, so the answer is at least
      ceil(total / K).
    Answer = max(max_inc, ceil(total / K)).

Complexity:
    Time : O(N log N) per test case (sorting dominates)
    Space: O(N)
"""


# ---------------------------------------- Solution -----------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        A.sort()
        total = 0
        max_inc = 0
        prev = None
        for x in A:
            if prev is None:
                cur = x
            else:
                cur = max(x, prev + 1)
            inc = cur - x
            total += inc
            max_inc = max(max_inc, inc)
            prev = cur
        ans = max(max_inc, (total + K - 1) // K)
        print(ans)

if __name__ == "__main__":
    solve()
