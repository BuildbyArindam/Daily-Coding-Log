"""
Problem   : Maximum Weight Transformation of String
Platform  : GeeksforGeeks 
Link      : https://www.geeksforgeeks.org/problems/maximum-weight-transformation-of-a-given-string3551/1
Date      : 2026-10-27
Difficulty: Medium
Topic     : Dynamic Programming

Approach  :
    dp[i] = max weight for the first i characters.
    At each position, either:
      - take s[i] alone       -> dp[i-1] + 1
      - pair s[i-1] and s[i]  -> dp[i-2] + (3 if same else 4)
    dp[i] depends only on the previous two states, so two rolling
    variables (older, newer) replace the full array.

Time      : O(n)
Space     : O(1)
"""


# --------------------------------------------------- Solution -----------------------------------------------------------------


class Solution:
    def getMaxWeight(self, s):
        # code here
        n = len(s)
        if n == 0:
            return 0
        older = 0   
        newer = 1     
        idx = 1
        while idx < n:
            same = (s[idx] == s[idx - 1])
            gain = 3 if same else 4    
            take_pair = older + gain
            take_single = newer + 1
            current = take_pair if take_pair > take_single else take_single
            older, newer = newer, current
            idx += 1
        return newer
