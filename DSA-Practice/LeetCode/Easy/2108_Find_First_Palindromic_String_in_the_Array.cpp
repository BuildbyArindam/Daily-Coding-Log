/*
 * Problem : 2108. Find First Palindromic String in the Array
 * Link    : https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
 * Platform: LeetCode
 * Level   : Easy
 * Topics  : Array, Two Pointers, String
 * Date    : 2026-10-08
 *
 * Approach:
 *   Scan the words in order. For each word, use two pointers (one from
 *   the start, one from the end) and compare characters moving inward.
 *   Return the first word that is a palindrome, or "" if none exists.
 *
 * Complexity:
 *   Time  : O(N * L), where N = number of words, L = max word length
 *   Space : O(1) extra (no copies; words are passed by reference)
 */


// ----------------------------------------------- Solution -------------------------------------------------


class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for (auto word : words)  // iterate all the string 
      if (isPalindrome(word)) // check palindrome if true 
        return word;      // return the palindrome
    return "";
  }

 private:
  bool isPalindrome(string& s) {  // palindrome function to check
    int i = 0;
    int j = s.length() - 1;
    while (i < j)
      if (s[i++] != s[j--]){
        return false;
      }
    return true;
    }
};
