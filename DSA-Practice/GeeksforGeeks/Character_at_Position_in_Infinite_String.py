"""
Problem   : Character at Position in Infinite String
Platform  : GeeksforGeeks 
Link      : https://www.geeksforgeeks.org/problems/the-infinite-string1049/1
Difficulty: Medium
Topics    : Mathematics, Strings, Recursion
Date      : 2026-11-23

Approach:
    The infinite string is built as S_k = S_{k-1} + '$' * k + reverse(S_{k-1}),
    so len(S_k) = 2 * len(S_{k-1}) + k.
    1. Grow the length (without building the string) until it covers `pos`,
       tracking the final step k.
    2. Walk back from step k to 0. At each level the string splits into:
         [ prev part ][ k '$' gap ][ reversed prev part ]
       - pos in the gap           -> answer is '$'
       - pos in the reversed part -> mirror it: pos = size + 1 - pos
       - pos in the prev part     -> stay as is
       Then shrink to the previous level (size = prev, step -= 1).
    3. At step 0, the answer is s[pos - 1].

Time Complexity  : O(log(pos / len(s)))  -> the length roughly doubles each step
Space Complexity : O(1)                  -> no string is ever constructed
"""


# ------------------------------------------- Solution ---------------------------------------------------------


class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        # code here
        size = len(s)
        step = 0
        while size < pos:
            step += 1
            size = size * 2 + step
        while step > 0:
            prev = (size - step) // 2  
            gap_end = prev + step   
            if pos > gap_end:
                pos = size + 1 - pos
            elif pos > prev:
                return '$'

            size = prev
            step -= 1
        return s[pos - 1]
