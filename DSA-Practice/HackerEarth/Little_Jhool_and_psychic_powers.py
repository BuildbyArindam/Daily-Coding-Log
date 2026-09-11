"""
Problem: Little Jhool and psychic powers
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/psychic-powers/
Date: 2026-09-11
Difficulty: Easy
Topic: Ad-Hoc, Basic Programming, Implementation

Approach:
Read the binary string and check if it contains six consecutive
identical digits ('000000' or '111111') using substring search.
If found, the psychic's claim is disproven ("Sorry, sorry!");
otherwise the claim holds ("Good luck!").

Time Complexity: O(n) - single substring scan over the input string
Space Complexity: O(1) - no extra space beyond the input string
"""


# -------------------------- Solution -------------------------------------


name = input().strip()

if '000000' in name or '111111' in name:
    print("Sorry, sorry!")
else:
    print("Good luck!")
