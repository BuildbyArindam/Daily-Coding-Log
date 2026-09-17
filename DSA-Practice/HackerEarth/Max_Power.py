"""
Problem   : Max Power (Increasing Subsequence)
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/practice-problems/algorithm/increasing-subsequence-fbb63e3c/
Date      : 2026-09-17
Difficulty: Easy
Topics    : Algorithms, Quick Sort, Sorting

Approach:
    Maintain a monotonic increasing stack over indices. For each new
    element x, pop indices whose values exceed x (they can no longer
    start a valid "power" pair with x), then compare x against the
    value at the new stack top to update the best difference. This
    captures the max (a[j] - a[i]) for i < j where the subsequence
    from i to j stays non-decreasing in a relevant sense.
    Special-cased when global min is at the last index and global max
    is at the first index (edges of the array), checking second-min/
    second-max to avoid missing a valid pair.

Time complexity : O(n) per test case (each index pushed/popped once)
Space complexity: O(n) for the stack
"""


# ----------------------------- Solution ---------------------------------------


import sys

def original_power(a):
    stack = []
    best = 0
    for i, x in enumerate(a):
        while stack and a[stack[-1]] > x:
            stack.pop()
        if stack:
            best = max(best, x - a[stack[-1]])
        stack.append(i)
    return best

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        mn = min(a)
        mx = max(a)
        min_pos = a.index(mn)
        max_pos = a.index(mx)
        if n == 2:
            print(mx - mn)
            continue
        if min_pos != n - 1 or max_pos != 0:
            print(mx - mn)
            continue
        second_min = float('inf')
        second_max = float('-inf')
        for x in a:
            if x != mn:
                second_min = min(second_min, x)
            if x != mx:
                second_max = max(second_max, x)
        ans = original_power(a)
        ans = max(ans, mx - second_min)
        ans = max(ans, second_max - mn)
        print(ans)

if __name__ == "__main__":
    solve()
