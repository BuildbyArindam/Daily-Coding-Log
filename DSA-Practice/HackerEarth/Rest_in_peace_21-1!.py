"""
Problem: Rest in peace - 21-1!
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/rest-in-peace-21-1/
Date: 2026-09-17
Difficulty: Easy
Topics: Ad-Hoc, Basic Programming

Approach:
For each number, check two conditions: whether "21" appears as a substring
in its decimal representation, or whether it's exactly divisible by 21.
If either holds, the streak is broken; otherwise it lives on.

Time Complexity: O(d) per test case, where d = number of digits in n
                  (from the substring check) -> O(T*d) overall
Space Complexity: O(1) extra space (excluding input storage)
"""


# ----------------------------------- Solution --------------------------------------------


t = int(input())

for _ in range(t):
    n = int(input())
    if "21" in str(n) or n % 21 == 0:
        print("The streak is broken!")
    else:
        print("The streak lives still in our heart!")
