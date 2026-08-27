"""
Problem   : Anagram Occurrences
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FAOCU
Date      : 2026-08-27
Difficulty: Easy-Medium (est.)
Topics    : String Manipulation / Sliding Window / Frequency Counting / Hashing

Approach:
    Fixed-size sliding window of length len(P) over S. Maintain a
    26-length frequency array for the window and compare it against
    P's frequency array at each shift. On match, record the starting
    index. Window frequency is updated incrementally (add incoming
    char, remove outgoing char) rather than recomputed from scratch.

Time Complexity : O(26 * (len(S) - len(P))) ~ O(len(S)) since the
                   array comparison is O(26) = O(1) per shift.
Space Complexity: O(1) extra (two fixed 26-length arrays).
"""


# ------------------------------ Solution --------------------------------------


import sys

def find_anagram_occurrences():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    S = input_data[0]
    P = input_data[1]
    len_s = len(S)
    len_p = len(P)
    if len_p > len_s:
        print(-1)
        return
    p_freq = [0] * 26
    win_freq = [0] * 26
    for i in range(len_p):
        p_freq[ord(P[i]) - ord("a")] += 1
        win_freq[ord(S[i]) - ord("a")] += 1
    result = []
    if p_freq == win_freq:
        result.append(0)
    for i in range(len_p, len_s):
        win_freq[ord(S[i]) - ord("a")] += 1
        win_freq[ord(S[i - len_p]) - ord("a")] -= 1
        if win_freq == p_freq:
            result.append(i - len_p + 1)
    if result:
        print(*(result))
    else:
        print(-1)

if __name__ == "__main__":
    find_anagram_occurrences()
