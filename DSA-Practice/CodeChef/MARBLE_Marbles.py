"""
CodeChef: Marbles
Problem: https://www.codechef.com/problems/MARBLE
Date: 2026-09-29
Difficulty: 1716
Topics: Strings, Counting, Brute Force

Approach:
- Process all fixed character pairs directly using the vowel/consonant cost rules.
- For positions containing '?', count how often each fixed character appears.
- Try all 26 possible letters as the replacement for '?' and compute the total cost.
- Positions with "??" can use the same replacement letter, so they add no cost.

Time Complexity: O(N + 26^2) per test case
Space Complexity: O(26)
"""


# ----------------------------------- Solution ------------------------------------------


import sys
input = sys.stdin.readline
VOWELS = set("aeiou")
LETTERS = "abcdefghijklmnopqrstuvwxyz"

def is_vowel(c):
    return c in VOWELS

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().strip()
        P = input().strip()
        fixed_cost = 0
        cnt_s = [0] * 26
        cnt_p = [0] * 26
        both_question = 0
        for s, p in zip(S, P):
            if s == '?' and p == '?':
                both_question += 1
            elif s == '?':
                cnt_s[ord(p) - 97] += 1
            elif p == '?':
                cnt_p[ord(s) - 97] += 1
            else:
                if s == p:
                    continue
                if is_vowel(s) != is_vowel(p):
                    fixed_cost += 1
                else:
                    fixed_cost += 2
        answer = float('inf')
        for c in LETTERS:
            cost = fixed_cost
            for x in range(26):
                count = cnt_s[x]
                if count == 0:
                    continue
                other = LETTERS[x]
                if c == other:
                    cost += 0
                elif is_vowel(c) != is_vowel(other):
                    cost += count
                else:
                    cost += 2 * count
            for x in range(26):
                count = cnt_p[x]
                if count == 0:
                    continue
                other = LETTERS[x]
                if c == other:
                    cost += 0
                elif is_vowel(c) != is_vowel(other):
                    cost += count
                else:
                    cost += 2 * count
            answer = min(answer, cost)
        print(answer)

if __name__ == "__main__":
    solve()
