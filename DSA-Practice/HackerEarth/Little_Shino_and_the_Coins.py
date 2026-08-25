"""
Problem   : Little Shino and the coins
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/little-shino-and-coins-3/
Date      : 2026-08-25
Difficulty: Easy
Topic     : Basic Programming

Approach:
For each starting index i, extend the window rightwards while tracking distinct
characters in a set. Every time the distinct count hits exactly k, count that
substring; stop extending once distinct count exceeds k (further extension can
only add more distinct chars, never fewer).

Time complexity : O(n^2) worst case (n = len(s)) — nested loop, set ops O(1) amortized
Space complexity: O(k) — set holds at most k distinct characters at a time
"""


# ------------------------- Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    s = input_data[1]
    n = len(s)
    ans = 0
    for i in range(n):
        distinct_chars = set()
        for j in range(i, n):
            distinct_chars.add(s[j])
            if len(distinct_chars) == k:
                ans += 1
            elif len(distinct_chars) > k:
                break
    print(ans)

if __name__ == '__main__':
    solve()
