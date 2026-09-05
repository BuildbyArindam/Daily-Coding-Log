# Problem: Duplicate Characters
# Platform: Code360 (Naukri)
# Link: https://www.naukri.com/code360/problems/duplicate-characters_3189116?kunjiRedirection=true
# Difficulty: Easy
# Date: 2026-09-05
# Topic: Hashing, Frequency Counting, String Manipulation
#
# Approach:
#   Count character frequencies with collections.Counter, then collect
#   characters occurring more than once, sorted alphabetically.
#
# Time Complexity:  O(n + k log k)  -- n = len(s), k = distinct chars (counting + sort)
# Space Complexity: O(k)            -- frequency table


# -------------------------- Solution --------------------------------


from sys import *
from collections import *
from math import *
from typing import *
def duplicate_char(s: str, n: int) -> List[Tuple[str, int]]:
    freq = Counter(s)
    ans = []
    for ch in sorted(freq):
        if freq[ch] > 1:
            ans.append((ch, freq[ch]))
    return ans
