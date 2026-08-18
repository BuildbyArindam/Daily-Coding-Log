"""
Problem   : Secret Cipher
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/secret-cipher--141631/1
Difficulty: Hard
Topic     : Stack / KMP (LPS Array)
Date      : 2026-08-18

Approach:
    - Build the LPS (Longest Prefix Suffix) array of the string using the
      standard KMP preprocessing step.
    - Walk the string from the last index down to the first. For the
      current prefix s[0..i] (length = i+1), check if it is an exact
      doubling of its own smaller half, i.e. s[0..i] = t + t for some t.
      This is detected using the classic "smallest period divides length"
      trick: lps[i] >= length//2 and length % (2*(length - lps[i])) == 0.
    - If the prefix is a valid doubling AND its length is even (i odd),
      replace the whole prefix with a single '*' and jump directly to the
      midpoint (i = i // 2) instead of processing it character by character.
    - Otherwise, keep the character as-is and move one step back (i -= 1).
    - Reverse the collected result at the end since we built it back-to-front.

Time Complexity : O(n)
    - LPS array construction is O(n).
    - The compression loop appears nested (while + halving), but each index
      is visited at most once overall — every step either consumes one
      character (i -= 1) or jumps to i // 2, so total work is bounded by n
      (amortized single pass).

Space Complexity: O(n)
    - O(n) for the LPS array.
    - O(n) for the output list/stack `ans`.
"""


# ---------------------------------- Solution -----------------------------


class Solution:
    def compress(self, s):
        # code here
        n = len(s)
        lps = [0] * n
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
            lps[i] = j
        ans = []
        i = n - 1
        while i >= 0:
            length = i + 1
            if (
                i % 2 == 1
                and lps[i] >= length // 2
                and length % (2 * (length - lps[i])) == 0
            ):
                ans.append('*')
                i = i // 2
            else:
                ans.append(s[i])
                i -= 1
        return ''.join(reversed(ans))
