"""
Problem   : Magnet Sort
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MAGNETSORT
Difficulty: 1804
Date      : 2026-10-10
Topics    : Greedy, Sorting, Case Analysis

Approach:
  - If the array is already sorted, the answer is 0.
  - Otherwise find the first (l) and last (r) positions where the array
    differs from its sorted version. A single operation suffices only if
    a prefix element (index <= l) and a suffix element (index >= r) have
    different magnet types (N/S), so they can be fixed in one move.
  - If one operation isn't enough but both magnet types exist in the
    string, 2 operations always suffice.
  - If every magnet has the same type and the array is unsorted, no
    operation is possible, so the answer is -1.

Complexity:
  Time : O(n log n) per test case (dominated by sorting)
  Space: O(n)
"""


# ------------------------------------------------ Solution ------------------------------------------------------------


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input().strip()
    b = sorted(a)
    if a == b:
        print(0)
        continue
    l = 0
    while a[l] == b[l]:
        l += 1
    r = n - 1
    while a[r] == b[r]:
        r -= 1
    left = set(s[:l + 1])
    right = set(s[r:])
    can_sort_once = (
        ('N' in left and 'S' in right)
        or ('S' in left and 'N' in right)
    )
    if can_sort_once:
        print(1)
    elif len(set(s)) == 1:
        print(-1)
    else:
        print(2)
