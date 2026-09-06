"""
Problem   : Shil and Palindrome
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/shil-and-palindrome/
Difficulty: Easy
Topic     : Approved, Basic Programming, Open
Date      : 2026-09-06

Approach:
    Count character frequencies. A rearrangement into a palindrome is
    possible only if at most one character has an odd frequency.
    If possible, build the left half by taking floor(freq/2) copies of
    each sorted character, use the single odd-frequency char (if any)
    as the middle, and mirror the left half for the right side.
    Otherwise, print -1.

Time Complexity : O(n log n)  -- dominated by sorting the distinct chars
                                 (n = length of string)
Space Complexity: O(n)        -- Counter + left-half list/string
"""


# ---------------------------- Solution -----------------------------------


name = input()
from collections import Counter
freq = Counter(name)
odd = [ch for ch in freq if freq[ch] % 2 == 1]
if len(odd) > 1:
    print(-1)
else:
    left = []
    middle = ''
    for ch in sorted(freq):
        left.append(ch * (freq[ch] // 2))
    if odd:
        middle = odd[0]
    left = ''.join(left)
    result = left + middle + left[::-1]
    print(result)
