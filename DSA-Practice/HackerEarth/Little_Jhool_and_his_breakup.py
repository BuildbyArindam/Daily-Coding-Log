"""
Problem: Little Jhool and his breakup
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/little-jhool-and-his-breakup/
Difficulty: Easy
Topic: Basic Programming, Implementation
Date: 2026-09-11

Approach:
Check if "love" appears as a subsequence of the input string using a
two-pointer / greedy scan — advance a pointer into "love" whenever the
current character of the name matches the next needed letter. If the
pointer reaches the end of "love", all its letters appeared in order.

Time Complexity: O(n), n = length of name (single pass)
Space Complexity: O(1), only a pointer and fixed-length target string
"""


# ----------------------------- Solution -----------------------------------


name = input().strip()
word = "love"
j = 0
for ch in name:
    if j < len(word) and ch == word[j]:
        j += 1
if j == len(word):
    print("I love you, too!")
else:
    print("Let us breakup!")
