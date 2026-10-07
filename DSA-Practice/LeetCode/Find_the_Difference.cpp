/*
 * Problem   : 389. Find the Difference
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/find-the-difference/
 * Difficulty: Easy
 * Topics    : Hash Table, String, Bit Manipulation, Sorting
 * Date      : 2026-10-07
 *
 * Approach  : Running-sum carry. t is s plus one extra character, so
 *             t[i+1] += t[i] - s[i] pushes the running difference forward.
 *             After the loop, t's last element equals
 *             sum(t) - sum(s), which is the extra character.
 *             Overflow in char wraps modulo 256, and the true result is a
 *             valid lowercase letter, so the answer stays correct.
 *
 * Time      : O(n)
 * Space     : O(1) extra (t is modified in place; the by-value copy is not
 *             counted as algorithmic space)
 */


// ------------------------------------------------- Solution ---------------------------------------------------


class Solution {
public:
    char findTheDifference(string s, string t) {
        for(int i=0;i<s.size();i++)
    t[i+1]+=t[i]-s[i]; //Passing the diff: (t[i]-s[i]) to t[i+1]
      return t[t.size()-1]; //The diff will be carried over to the last element eventually
    }
};
