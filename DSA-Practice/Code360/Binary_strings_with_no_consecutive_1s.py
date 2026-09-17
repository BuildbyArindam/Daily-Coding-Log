"""
Problem: Binary Strings with No Consecutive 1s
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380926
Date Solved: 2026-09-17
Difficulty: Medium
Topics: Recursion, Backtracking, Dynamic Programming

Approach:
Use backtracking to build binary strings of length N character by
character. At each index, always branch on appending '0'. Only branch
on appending '1' if the current string is empty or its last character
isn't '1' — this constraint prunes any string that would contain
consecutive 1s, so no invalid string is ever fully built.

Time Complexity: O(F(N+2)) to generate valid strings, where F is the
Fibonacci sequence (the count of valid strings of length N follows
Fibonacci); each is built in O(N), so overall O(N * F(N+2)).
Space Complexity: O(N) recursion depth, plus O(N * F(N+2)) to store
all output strings.
"""


# ------------------------------------ Solution ----------------------------------------


from typing import List

def generateString(N: int) -> List[str]:
    result = []
    def backtrack(index: int, current: str):
        if index == N:
            result.append(current)
            return
        backtrack(index + 1, current + '0')
        if not current or current[-1] != '1':
            backtrack(index + 1, current + '1')
    backtrack(0, "")
    return result
