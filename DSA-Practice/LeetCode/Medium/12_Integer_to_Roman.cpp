/*
 * Problem:    12. Integer to Roman
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/integer-to-roman/
 * Difficulty: Medium
 * Topics:     Hash Table, Math, String
 * Date:       2026-10-05
 *
 * Approach:   Greedy. Keep an ordered table of Roman symbols (including the
 *             subtractive pairs CM, CD, XC, XL, IX, IV) from largest to
 *             smallest value. For each symbol, append it while num >= value
 *             and subtract that value from num.
 *
 * Time:       O(1). The symbol table has a fixed size (13) and, for
 *             num <= 3999, the total appends are bounded by a constant.
 * Space:      O(1) extra, apart from the output string.
 */


// --------------------------------------------- Solution ------------------------------------------------------------


class Solution {
public:
    string intToRoman(int num) {
        string roman_numeral = "";
        
        vector<pair<int, string>> roman_symbols = {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, 
            {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"},
            {4, "IV"}, {1, "I"}
        };
        
        for (auto symbol : roman_symbols) {
            int value = symbol.first;
            string numeral = symbol.second;
            while (num >= value) {
                roman_numeral += numeral;
                num -= value;
            }
        }
        return roman_numeral;
    }
};
