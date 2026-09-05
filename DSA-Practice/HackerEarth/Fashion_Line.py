"""
Problem: Fashion Line
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/fashion-line-1/
Difficulty: Medium
Topics: Ad-Hoc, Approved, Basic Programming, Implementation, Open
Date Solved: 2026-09-05

Approach:
Count substrings of S whose count of "special" characters (chars in
special_string) falls within [L, R]. Use the standard
"exactly-in-range = atMost(R) - atMost(L-1)" trick: atMost(x) counts
substrings with at most x special characters via a sliding window
(two-pointer), incrementing the window's right edge and shrinking
from the left whenever special_count exceeds x. Each valid right
endpoint contributes (right - left + 1) substrings.

Time Complexity: O(N) per test case (two-pointer window is linear;
special-char membership check is O(1) via set lookup)
Space Complexity: O(1) extra (aside from input storage) — set of
special characters is bounded by alphabet size
"""


# -------------------------- Solution -------------------------------


name = input()        
T = int(name)
def at_most(s, special, x):
    if x < 0:
        return 0
    left = 0
    special_count = 0
    ans = 0
    for right in range(len(s)):
        if s[right] in special:
            special_count += 1
        while special_count > x:
            if s[left] in special:
                special_count -= 1
            left += 1
        ans += right - left + 1
    return ans
for _ in range(T):
    N, K, L, R = map(int, input().split())
    S = input().strip()
    special_string = input().strip()
    special = set(special_string)
    answer = at_most(S, special, R) - at_most(S, special, L - 1)
    print(answer)
