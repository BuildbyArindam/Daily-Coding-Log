/*
 * Problem:    7. Reverse Integer
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/reverse-integer/
 * Difficulty: Medium
 * Topics:     Math
 * Date:       2026-10-04
 *
 * Approach:
 *   Pop the last digit of x with % 10 and push it onto `reversed`
 *   (reversed = reversed * 10 + pop). Before each push, check whether
 *   multiplying by 10 would overflow a 32-bit int. If so, return 0.
 *
 * Complexity:
 *   Time:  O(log10 |x|), one iteration per digit
 *   Space: O(1)
 */


// --------------------------------------- Solution -------------------------------------------


class Solution {
public:
    int reverse(int x) {
        int reversed = 0;
       int pop;
       while (x != 0) {
           if (reversed > INT_MAX / 10 || reversed < INT_MIN / 10) {
               return 0;
           }
           pop = x % 10;
           x /= 10;
           reversed = reversed * 10 + pop;
       }
       return reversed;
    }
};
