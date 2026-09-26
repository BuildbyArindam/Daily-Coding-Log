"""
Problem: The Mirror of Galadriel
Platform: CodeChef
Link: https://www.codechef.com/practice/course/icpc/ICPCTR07/problems/MSTRINGS
Date: 2026-09-26
Difficulty: Hard
Topics: Strings, Palindrome Check

Approach:
    A string is "magical" if it reads the same forwards and backwards.
    Reverse the string with slicing and compare to the original.

Time Complexity:  O(n) per test case, where n = length of the string
Space Complexity: O(n) for the reversed copy
"""


# ---------------------------------------- Solution ----------------------------------------------


def is_magical_string(text):
    flipped = text[::-1]
    return flipped == text

def process_input():
    total_cases = int(input())
    results = []
    for _ in range(total_cases):
        current_word = input().strip()
        verdict = "YES" if is_magical_string(current_word) else "NO"
        results.append(verdict)
    print("\n".join(results))

if __name__ == "__main__":
    process_input()
