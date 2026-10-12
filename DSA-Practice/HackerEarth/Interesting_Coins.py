"""
Problem   : Interesting Coins
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/interesting-coins-5/
Difficulty: Medium
Topics    : Binary Search, Greedy, Sorting
Date      : 2026-10-12

Approach  :
    Binary search on the answer c (the maximum allowed change per coin).
    possible(a, c) checks a given c greedily from left to right. Each coin x
    can become any value in [max(1, x - c), x + c], and the final values must
    be strictly increasing. Each coin takes the smallest allowed value, which
    is max(low, prev + 1), so the most room is left for later coins. If that
    value exceeds x + c, c is infeasible.
    Feasibility is monotonic in c (a larger c only widens every range), so
    binary search finds the smallest feasible c.

Complexity:
    Time  : O(n * log(max(a) + n)) per test case
    Space : O(1) extra (besides the input array)
"""


# --------------------------------------- Solution --------------------------------------------------


import sys
input = sys.stdin.readline

def possible(a, c):
    prev = 0
    for x in a:
        low = max(1, x - c)
        high = x + c
        curr = max(low, prev + 1)
        if curr > high:
            return False
        prev = curr
    return True

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        left, right = 0, max(a) + n
        while left < right:
            mid = (left + right) // 2
            if possible(a, mid):
                right = mid
            else:
                left = mid + 1
        print(left)

if __name__ == "__main__":
    solve()
