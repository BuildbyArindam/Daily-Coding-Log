"""
Problem   : Exam Result (EXMRS)
Platform  : CodeChef (DSAMONDAY022)
Link      : https://www.codechef.com/DSAMONDAY022/problems/EXMRS
Date      : 2026-09-28
Difficulty: Easy
Topics    : Implementation, Math
Approach  : Read the five integers from one line: correct answers, marks per
            correct answer, wrong answers, penalty per wrong answer, and the
            required score. Score = right * reward - wrong * penalty.
            Print YES if the score >= required marks, else NO.
Time      : O(1)
Space     : O(1)
"""


# -------------------------------------- Solution ----------------------------------------------


import sys

def verdict(gain, loss, need):
    return "YES" if gain - loss >= need else "NO"

def main():
    raw = sys.stdin.readline().split()
    nums = list(map(int, raw))
    need = nums.pop()
    penalty = nums.pop()
    wrong = nums.pop()
    reward = nums.pop()
    right = nums.pop()
    earned = right * reward
    lost = wrong * penalty
    print(verdict(earned, lost, need))

main()
