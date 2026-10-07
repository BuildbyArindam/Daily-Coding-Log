"""
Problem   : Monk and Chocolates
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/monk-and-chocolates-60875f0e/
Difficulty: Medium
Topics    : Binary Search, Searching (solved with Sliding Window)
Date      : 2026-10-07

Approach:
    For each distinct character `ch` in the string, run a sliding window
    that keeps at most M positions differing from `ch`. Expand the right
    pointer, count mismatches, and shrink from the left whenever mismatches
    exceed M. The answer is the largest valid window over all characters.

Complexity:
    Time  : O(D * N) per test case, D = number of distinct characters
            (at most 26 for lowercase letters)
    Space : O(D) extra, for the set of distinct characters
"""


# ---------------------------------------------- Solution -------------------------------------------------


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    s = input().strip()
    ans = 0
    for ch in set(s):
        left = 0
        changes = 0
        for right in range(N):
            if s[right] != ch:
                changes += 1
            while changes > M:
                if s[left] != ch:
                    changes -= 1
                left += 1
            ans = max(ans, right - left + 1)
    print(ans)
