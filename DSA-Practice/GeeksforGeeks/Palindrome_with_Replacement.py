"""
Problem   : Palindrome with Replacement
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/palindrome-with-minimum-sum--170648/1
Difficulty: Medium
Topics    : Strings, Two Pointers, Greedy
Date      : 2026-10-22

Approach:
    Two pointers walk inward from both ends, so only the first half of the
    palindrome needs to be built; the second half mirrors it.
      - If both characters at a pair are letters and differ, no palindrome
        is possible, so return -1.
      - If one side is a letter, that letter fixes the pair's value.
      - If both are '?', the pair copies its neighbour's value, so it adds
        zero cost and can be skipped.
    Each time a fixed value is found, add |current - previous| to the running
    total. The mirrored half contributes the same cost again, so the final
    answer is doubled (answer << 1).

Complexity:
    Time : O(n), a single pass over half the string
    Space: O(1)
"""


# ---------------------------------------------- Solution ---------------------------------------------------------


class Solution:
    def minimumSum(self, s: str) -> int:
        # code here
        length = len(s)
        previous = None 
        answer = 0
        left, right = 0, length - 1
        while left <= right:
            lc, rc = s[left], s[right]
            if lc != '?' and rc != '?' and lc != rc:
                return -1
            if lc != '?':
                current = ord(lc)
            elif rc != '?':
                current = ord(rc)
            else:
                current = None
            if current is not None:
                if previous is not None:
                    answer += abs(current - previous)
                previous = current
            left += 1
            right -= 1
        return answer << 1
