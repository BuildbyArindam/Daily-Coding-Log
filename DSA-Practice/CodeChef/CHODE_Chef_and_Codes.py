"""
Problem : Chef and Codes (CHODE)
Platform: CodeChef
Link    : https://www.codechef.com/problems/CHODE
Difficulty: 1703
Topics  : Strings, Sorting, Frequency Counting, Implementation
Date    : 2026-09-24

Approach:
    Count how often each letter appears in the encrypted text, case-insensitively.
    Sort the 26 letters by (frequency, alphabetical index) so ties break
    deterministically, then map the i-th ranked cipher letter to the i-th letter
    of the given frequency string. Decode by substituting each letter, keeping
    its original case and leaving non-letters untouched.

Complexity (per test case, N = length of encrypted text):
    Time : O(N + 26 log 26), which is O(N)
    Space: O(N) for the output, O(1) for the counting and mapping tables
"""


# -------------------------------- Solution -----------------------------------------------


T = int(input())

for _ in range(T):
    frequency = input().strip()
    encrypted = input()
    count = [0] * 26
    for ch in encrypted:
        if 'a' <= ch <= 'z':
            count[ord(ch) - ord('a')] += 1
        elif 'A' <= ch <= 'Z':
            count[ord(ch) - ord('A')] += 1
    cipher_order = sorted(range(26), key=lambda i: (count[i], i))
    mapping = [''] * 26
    for i in range(26):
        mapping[cipher_order[i]] = frequency[i]
    result = []
    for ch in encrypted:
        if 'a' <= ch <= 'z':
            result.append(mapping[ord(ch) - ord('a')])
        elif 'A' <= ch <= 'Z':
            result.append(mapping[ord(ch) - ord('A')].upper())
        else:
            result.append(ch)
    print(''.join(result))
