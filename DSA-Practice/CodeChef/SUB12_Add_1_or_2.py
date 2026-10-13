"""
Problem   : Add 1 or 2 (SUB12)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SUB12
Difficulty: 1813
Date      : 2026-10-13
Topics    : Binary Search on Answer, Greedy

Approach:
    Binary search on the final maximum value `limit`, between max(a) (the
    lower bound) and max(a[i] + b[i]) (the upper bound).
    Feasibility check for a given limit:
      - need  = total excess over limit, sum of (x - limit) for x > limit
      - spare = total capacity below limit, sum of (limit - x) // 2 for x <= limit
    The limit is achievable iff need <= spare. Feasibility is monotonic in
    limit, so the smallest feasible value is found by binary search.

Time  : O(N * log(max(a[i] + b[i]))) per test case
Space : O(N) for the combined array
"""


# --------------------------------------- Solution -----------------------------------------------------------


import sys
input = sys.stdin.readline

def can_achieve(limit, arr):
    need = 0
    spare = 0
    for x in arr:
        if x > limit:
            need += x - limit
        else:
            spare += (limit - x) // 2
    return need <= spare

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        arr = [a[i] + b[i] for i in range(n)]
        low = max(a)
        high = max(arr)
        while low < high:
            mid = (low + high) // 2
            if can_achieve(mid, arr):
                high = mid
            else:
                low = mid + 1
        print(low)

if __name__ == "__main__":
    solve()
