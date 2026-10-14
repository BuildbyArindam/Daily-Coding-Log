"""
Problem   : Roll Characters of String
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/roll-the-characters-of-a-string2127/1
Difficulty: Medium
Topics    : Arrays, Strings
Date      : 2026-10-14

Approach:
    roll[i] = r means the first r characters each shift forward by one
    (wrapping z -> a). Instead of applying every roll separately, count how
    many rolls cover each index. Mark increments[r-1] += 1 for each roll,
    then take a suffix sum so increments[i] is the number of rolls with
    r-1 >= i. Each character is shifted by increments[i] % 26.

Time Complexity : O(n + m), n = len(s), m = len(roll)
Space Complexity: O(n) for the increments array and the result list
"""


# --------------------------------------------- Solution --------------------------------------------------------


class Solution:
    def findRollOut(self, s, roll):
        # code here
        n = len(s)
        count = 0
        arr = list(s)
        for i in range(len(roll) - 1, -1, -1):
            count = (count + 1) % 26
            arr[roll[i] - 1] = arr[roll[i] - 1]
        count = 0
        increments = [0] * n
        for r in roll:
            increments[r - 1] += 1
        for i in range(n - 2, -1, -1):
            increments[i] += increments[i + 1]
        for i in range(n):
            shift = increments[i] % 26
            arr[i] = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        return ''.join(arr)
