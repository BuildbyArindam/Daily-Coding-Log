/*
 * Problem   : 1903. Largest Odd Number in String
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/largest-odd-number-in-string/
 * Difficulty: Easy
 * Topics    : Math, String, Greedy
 * Date      : 2026-10-03
 *
 * Approach:
 *   A number is odd only if its last digit is odd. The largest odd
 *   substring must therefore be a prefix ending at the rightmost odd digit
 *   (a longer prefix means a larger number). Scan from the right, and at
 *   the first odd digit return the prefix up to and including it. If no
 *   odd digit exists, return "".
 *
 * Time Complexity : O(n), single backward scan; substr adds at most O(n)
 * Space Complexity: O(1) extra (excluding the returned string)
 */


// ------------------------------------- Solution --------------------------------------------------


class Solution {
public:
    string largestOddNumber(string num) {
         if (num.back() % 2 == 1) return num;
        int i = num.length() - 1;
        while (i >= 0) {
            int n = num[i];
            if (n % 2 == 1) return num.substr(0, i + 1);
            i--;
        }
        return "";
    }
};
