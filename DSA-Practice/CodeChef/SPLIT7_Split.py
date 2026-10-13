"""
Problem   : Split (SPLIT7)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SPLIT7
Difficulty: 1813
Date      : 2026-10-13
Topics    : Binary Search on Answer, Greedy, Strings

Approach:
    Binary search on the answer x (largest value such that the string can be
    cut into at least k parts, each with score >= x).
    The score of a segment is ones + max prefix balance, where balance is
    (#zeros - #ones) over the prefix and the empty prefix counts as 0.
    Equivalently, it is the max over cut points of (zeros before + ones after).
    Feasibility check: scan left to right and cut greedily as soon as the
    current segment's score reaches x. Leftover characters merge into the last
    part, and a segment's score never decreases when extended.
    If we reach k parts, x is feasible. Search range is [1, n // k].

Complexity:
    Time : O(n log(n / k)) per test case
    Space: O(n) for the input string, O(1) extra
"""


# ------------------------------------------------ Solution ---------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        def can(x):
            parts = 0
            ones = 0
            balance = 0
            max_balance = 0
            for ch in s:
                if ch == '0':
                    balance += 1
                else:
                    balance -= 1
                    ones += 1
                max_balance = max(max_balance, balance)
                if ones + max_balance >= x:
                    parts += 1
                    if parts >= k:
                        return True
                    ones = 0
                    balance = 0
                    max_balance = 0
            return False
        low, high = 1, n // k
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        print(ans)

if __name__ == "__main__":
    solve()
