"""
Problem   : Lexicographically Smallest Rotation
Platform  : GeeksforGeeks (Hard)
Link      : https://www.geeksforgeeks.org/problems/lexicographically-smallest-string--151951/1
Date      : 2026-10-02
Topics    : Strings

Approach  : Minimum expression (least rotation) with two pointers.
            Concatenate s with itself so every rotation is a length-n window.
            Keep two candidate start indices i and j and a match length k.
            - If ss[i+k] == ss[j+k], extend k.
            - If ss[i+k] > ss[j+k], i can't start the smallest rotation,
              nor can any of i..i+k, so jump i past them.
            - Symmetric case for j.
            The smaller of i and j when one pointer reaches n (or k reaches n)
            is the start of the smallest rotation.

Time      : O(n)  (i, j only move forward, so total work is linear)
Space     : O(n)  (the doubled string s + s)
"""


# ----------------------------------------- Solution ------------------------------------------------------


class Solution:
    def lexiString(self, s: str) -> str:
        # code here
        n = len(s)
        ss = s + s
        i, j, k = 0, 1, 0
        while i < n and j < n and k < n:
            a = ss[i + k]
            b = ss[j + k]
            if a == b:
                k += 1
                continue
            if a > b:
                i = i + k + 1
                if i <= j:
                    i = j + 1
            else:
                j = j + k + 1
                if j <= i:
                    j = i + 1
            k = 0
        start = min(i, j)
        return ss[start:start + n]
