"""
Problem: Make Cat (INCAT)
Platform: CodeChef
Link: https://www.codechef.com/problems/INCAT
Date Solved: 2026-08-30
Difficulty: Cakewalk
Topics: String Manipulation, Sorting, Anagram Checking, Frequency Counting, Basic Implementation

Approach:
Check whether the input string is an anagram of "cat" by comparing
the sorted character sequence of the input against the sorted
character sequence of "cat". If they match, the string is a
rearrangement of exactly {c, a, t} and the answer is YES.

Time Complexity: O(n log n) — dominated by sorting the input string
                  (n is at most 3, so effectively O(1))
Space Complexity: O(n) — for the sorted character lists
"""


# --------------------- Solution ---------------------------


s = input().strip()
if sorted(s) == sorted("cat"):
    print("YES")
else:
    print("NO")
