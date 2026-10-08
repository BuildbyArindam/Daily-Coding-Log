"""
Problem   : Swap and Unite
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SWAPUNITE
Difficulty: 1731
Topics    : Two Pointers, Sliding Window, Strings
Date      : 2026-10-08

Approach:
    For each letter with k occurrences, the best target is the length-k
    window of the string that already contains the most occurrences of that
    letter. Every occurrence outside that window needs one swap to move in,
    so the cost is k - (max occurrences in any such window). Positions are
    stored per letter, and a two-pointer sweep finds the largest group of
    positions that fit in a span of k (p[right] - p[left] < k). The answer
    is the minimum cost over all letters.

Time Complexity : O(n) per test case (the position lists total n elements,
                  and each pointer only moves forward; the alphabet is a
                  constant 26)
Space Complexity: O(n) for the position lists
"""


# ------------------------------------------ Solution ---------------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        s = input().strip()
        n = len(s)
        pos = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            pos[ord(ch) - ord('a')].append(i)
        ans = n
        for p in pos:
            k = len(p)
            if k == 0:
                continue
            left = 0
            best = 0
            for right in range(k):
                while p[right] - p[left] >= k:
                    left += 1
                best = max(best, right - left + 1)
            ans = min(ans, k - best)
        print(ans)

if __name__ == "__main__":
    solve()
