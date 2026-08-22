"""
Problem   : Rhezo and Character Frequency
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/rhezo-and-character-frequency-3/
Difficulty: Easy
Topic     : Basic Programming / Implementation
Date      : 2026-08-22

Approach:
  - Build a prefix-sum array over S to count occurrences of C in O(1) per range.
  - Slide a window of size P across S to find Z, the maximum frequency of C
    in any window of length P.
  - Target frequency becomes Z + 1. Scan candidate insertion/change positions
    from the rightmost index down, checking (using prefix sums split across
    up to three sub-ranges around the affected position) whether placing C
    or another character at that position lets some window of length P reach
    the target frequency. Return the rightmost valid index, else -1.

Time Complexity : O(N * P) worst case (nested scan over insertion points and
                   window starts per point).
Space Complexity: O(N) for the prefix-sum array.
"""


# -------------------------- Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    S = input_data[0]
    C = input_data[1]
    P = int(input_data[2])
    N = len(S)
    pref = [0] * (N + 1)
    for i in range(N):
        pref[i + 1] = pref[i] + (1 if S[i] == C else 0)
    Z = 0
    for i in range(N - P + 1):
        freq = pref[i + P] - pref[i]
        if freq > Z:
            Z = freq
    target = Z + 1
    ans = -1
    for i in range(N, -1, -1):
        possible = False
        for ch in [C, '#']: 
            is_c = 1 if ch == C else 0
            start_min = max(0, i - P + 1)
            start_max = min(i, N + 1 - P)
            for j in range(start_min, start_max + 1):
                end1 = min(i, j + P)
                c1 = pref[end1] - pref[j] if end1 > j else 0
                c2 = is_c if (j <= i < j + P) else 0
                start3 = max(i, j)
                end3 = j + P - 1
                c3 = pref[end3] - pref[start3] if end3 > start3 else 0
                total_c = c1 + c2 + c3
                if total_c == target:
                    possible = True
                    break
            if possible:
                break
        if possible:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    solve()
