"""
Problem   : Letter Combinations of a Phone Number
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380922
Difficulty: Medium
Date      : 2026-09-17
Topics    : Recursion, Backtracking, Hash Table, String

Approach:
    Map each digit (2-9) to its corresponding letters on a phone keypad.
    Use backtracking/DFS: at each recursion level, pick one possible letter
    for the current digit and recurse to the next index, building up the
    combination string. When the index reaches the length of input string,
    the current combination is complete and added to the result list.

Time Complexity : O(4^n * n)
    - n = length of digit string
    - Each digit maps to at most 4 letters (worst case, e.g. '7' or '9')
    - 4^n possible combinations, each of length n to build/copy

Space Complexity: O(n)
    - Recursion call stack depth is O(n)
    - (Output storage of O(4^n * n) not counted as extra space)
"""


# ----------------------------- Solution ----------------------------------------


def combinations(s):
    keypad = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    result = []
    def backtrack(index, current):
        if index == len(s):
            result.append(current)
            return
        for ch in keypad[s[index]]:
            backtrack(index + 1, current + ch)
    backtrack(0, "")
    return result
