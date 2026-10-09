"""
Problem   : Sum of Modes (SUMMODE)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SUMMODE
Difficulty: 1734
Topics    : Prefix Sums, Hashing, Strings
Date      : 2026-10-09

Approach:
    Treat '1' as +1 and '0' as -1 and track a running prefix balance.
    A substring has equal 0s and 1s exactly when two prefix balances match,
    so a hashmap of balance frequencies counts these substrings in one pass.
    Every substring contributes a base of 1 (n(n+1)/2 in total), and each
    balanced substring adds 1 more, so answer = n(n+1)/2 + balanced.

Time Complexity : O(n) per test case
Space Complexity: O(n) per test case (frequency map of prefix balances)
"""


# -------------------------------------------- Solution ----------------------------------------------------


t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    total = n * (n + 1) // 2
    freq = {0: 1}
    balance = 0
    balanced = 0
    for ch in s:
        if ch == '1':
            balance += 1
        else:
            balance -= 1
        balanced += freq.get(balance, 0)
        freq[balance] = freq.get(balance, 0) + 1
    print(total + balanced)
