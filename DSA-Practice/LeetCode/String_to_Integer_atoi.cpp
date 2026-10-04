/*
 * Problem:    String to Integer (atoi)
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/string-to-integer-atoi/
 * Difficulty: Medium
 * Topics:     String
 * Date:       2026-10-04
 *
 * Approach:
 *   Single pass over the string in three phases:
 *   1. Skip leading spaces.
 *   2. Read an optional '+' or '-' sign.
 *   3. Read digits until a non-digit appears, checking before each
 *      multiply-by-10 step whether result would exceed INT_MAX
 *      (clamping to INT_MAX or INT_MIN based on sign).
 *
 * Time Complexity:  O(n), where n is the length of the string
 * Space Complexity: O(1)
 */


// ------------------------------------------------ Solution ------------------------------------------------


class Solution {
public:
    int myAtoi(string s) {
        int i = 0;
       int sign = 1;  
       int result = 0;
       while (i < s.length() && s[i] == ' ') {
           i++;
       }
       if (i < s.length() && (s[i] == '-' || s[i] == '+')) {
           sign = (s[i++] == '-') ? -1 : 1;
       }
       while (i < s.length() && isdigit(s[i])) {
           int digit = s[i] - '0'; 
           if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > INT_MAX % 10)) {
               return (sign == 1) ? INT_MAX : INT_MIN;
           }
           result = result * 10 + digit;
           i++;
       }
       return result * sign;
    }
};
