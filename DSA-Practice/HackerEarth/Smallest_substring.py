"""
Problem: Smallest Substring Containing All Distinct Characters
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/smallest-substring-e1862fcf/
Date: 2026-09-23
Difficulty: Medium
Topics: Algorithms, Binary Search, Searching

Approach:
Sliding window. Track the total count of distinct characters in S.
Expand the window with `right`, updating a frequency map. Once the
window contains all distinct characters, try to shrink it from the
left while it still contains all of them, recording the minimum
window length seen. This avoids re-scanning the string for each
candidate window.

Time Complexity: O(n) — each pointer (left, right) traverses the
string at most once.
Space Complexity: O(k) — k = number of distinct characters in S,
bounded by alphabet size.
"""


# ------------------------------------------ Solution ------------------------------------------------


def SmallestSubString(S):
    total_distinct = len(set(S))
    freq = {}
    left = 0
    distinct = 0
    ans = len(S)
    for right in range(len(S)):
        ch = S[right]
        freq[ch] = freq.get(ch, 0) + 1
        if freq[ch] == 1:
            distinct += 1
        while distinct == total_distinct:
            ans = min(ans, right - left + 1)
            left_ch = S[left]
            freq[left_ch] -= 1
            if freq[left_ch] == 0:
                distinct -= 1
            left += 1
    return ans

S = input()
out_ = SmallestSubString(S)
print(out_)
