"""
Problem   : Typing World (TYPWRL)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/TYPWRL
Date      : 2026-10-07
Difficulty: Medium
Topics    : Strings, Simulation

Approach:
    Put the left-hand keys in a set for O(1) lookup. Walk through the word
    once, mapping each character to a hand (0 = left, 1 = right). If it's
    the same hand as the previous character, extend the current run;
    otherwise reset the run to 1. The answer is the longest run seen.

Complexity (per test case):
    Time  : O(n + m) -> O(m) to build the set, O(n) to scan the word
    Space : O(m)     -> the set of left-hand keys
"""


# -------------------------------------------------- Solution ------------------------------------------------------


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    word = input().strip()
    left_keys = set(input().strip())
    best = 0
    current = 0
    previous_hand = None
    for ch in word:
        hand = 0 if ch in left_keys else 1
        if hand == previous_hand:
            current += 1
        else:
            current = 1
            previous_hand = hand
        if current > best:
            best = current
    print(best)
