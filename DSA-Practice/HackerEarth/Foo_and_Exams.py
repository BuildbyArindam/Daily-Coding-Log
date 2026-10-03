"""
Problem   : Foo and Exams
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/foo-and-exams-4/
Date      : 2026-10-03
Difficulty: Easy
Topics    : Binary Search, Sorting, Data Structures, Implementation

Approach:
    f(t) = A*t^3 + B*t^2 + C*t + D is monotonically non-decreasing for t >= 0
    (assuming non-negative coefficients), so we binary search for the largest t
    with f(t) <= K.
      1. If f(0) > K, no valid t exists -> answer 0.
      2. Exponential search: double `high` until f(high) > K to get an upper bound.
      3. Binary search in [low, high) to find the largest t with f(t) <= K.

Complexity (per test case):
    Time  : O(log t_max), where t_max is the answer; about 2*log(t_max) evaluations of f
    Space : O(1)
"""


# ------------------------------------ Solution ---------------------------------------------------


def solve():
    T = int(input())
    for _ in range(T):
        A, B, C, D, K = map(int, input().split())
        def f(t):
            return A * t * t * t + B * t * t + C * t + D
        if f(0) > K:
            print(0)
            continue
        low = 0
        high = 1
        while f(high) <= K:
            high *= 2
        while low + 1 < high:
            mid = (low + high) // 2
            if f(mid) <= K:
                low = mid
            else:
                high = mid
        print(low)

solve()
