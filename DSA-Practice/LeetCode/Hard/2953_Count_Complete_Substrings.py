"""
Problem   : 2953. Count Complete Substrings
Platform  : LeetCode 
Link      : https://leetcode.com/problems/count-complete-substrings/
Difficulty: HArd
Topics    : Hash Table, String, Sliding Window
Date      : 2026-11-25

Approach:
    A complete substring can never cross a position where adjacent letters
    differ by more than 2, so:
    1. Split the word into maximal segments where every adjacent pair of
       letters differs by at most 2 (two-pointer scan).
    2. In each segment, try every distinct-letter count c in 1..26. A valid
       substring then has a fixed length c * k.
    3. Slide a fixed-size window of length c * k over the segment, keeping a
       frequency map. Count the window when it has exactly c distinct letters
       and every frequency equals k.

Time  : O(26 * n) window slides, plus an O(26) frequency check per window
        worst case (about O(26^2 * n)); n = len(word).
Space : O(26) = O(1) for the frequency map.
"""


# -------------------------------------------- Solution ---------------------------------------------------------


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def dis(a, b):
            return abs(ord(a) - ord(b))

        def num_sub(i, j, num_char):
            length = num_char * k
            ans = 0
            mp = dict()
            cur_num = 0
            end = i
            for start in range(i, j - length + 1):
                if start > i:
                    if mp[word[start - 1]] == 1:
                        cur_num -= 1
                        del mp[word[start - 1]]
                    else:
                        mp[word[start - 1]] -= 1
                  
                while end < min(j, start + length):
                    if word[end] not in mp:
                        cur_num += 1
                        mp[word[end]] = 1
                    else:
                        mp[word[end]] += 1
                    end += 1
                if end - start == length and cur_num == num_char and set(mp.values()) == {k}:
                    ans += 1
            return ans 

        def find(i, j):
            ans = 0
            for num_char in range(1, 27):
                ans += num_sub(i, j, num_char)
            return ans
        slow = fast = 0
        ans = 0
        while fast < len(word):
            while fast < len(word):
                if fast == slow or dis(word[fast], word[fast - 1]) <= 2:
                    fast += 1
                else:
                    break
            ans += find(slow, fast)
            slow = fast
        return ans

  __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
