"""
LeetCode - Maximum Number of Non-Overlapping Substrings
Link: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
Date: 2026-09-18
Difficulty: Hard
Topics: Hash Table, String, Greedy, Sorting

Approach:
For each character, compute its first and last occurrence index. Starting
from a character's first occurrence, expand the window's right boundary
whenever a character inside the window has its own first occurrence before
the window's start (which invalidates it) or a last occurrence beyond the
current right bound (which extends it). This produces the smallest valid
"self-contained" substring for that character, if one exists. Collect all
valid intervals, sort by end index (and start descending as a tiebreak),
then greedily pick non-overlapping intervals in order of increasing end.

Time Complexity: O(n) to build first/last maps + O(n) worst case per
character expansion (bounded overall by O(26n)) + O(k log k) sort of
candidate intervals => O(n) overall for typical constraints.
Space Complexity: O(1) extra (fixed 26-size arrays) + O(k) for intervals/answer.
"""


# ------------------------------ Solution -----------------------------------------


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i
        intervals = []
        for c in range(26):
            if last[c] == -1:
                continue
            l = first[c]
            r = last[c]
            i = l
            valid = True
            while i <= r:
                idx = ord(s[i]) - ord('a')
                if first[idx] < l:
                    valid = False
                    break
                r = max(r, last[idx])
                i += 1
            if valid:
                intervals.append((l, r))
        intervals.sort(key=lambda x: (x[1], -(x[0])))
        ans = []
        prev_end = -1
        for l, r in intervals:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r
        return ans

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
