/*
 * Problem   : 647. Palindromic Substrings
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/palindromic-substrings/
 * Difficulty: Medium
 * Topics    : Two Pointers, String, Dynamic Programming
 * Date      : 2026-10-08
 *
 * Approach  : Brute force. Enumerate every substring s[i..j], copy it with
 *             substr(), and check it with a two-pointer palindrome test.
 *             Increment the count for each palindrome.
 *
 * Time      : O(n^3): O(n^2) substrings, each copied and checked in O(n)
 * Space     : O(n): the substring copy
 *
 * Better    : Expand around center is O(n^2) time and O(1) space.
 */


// ----------------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    int count{0};
    bool isPalindrome(string str){
        int left  = 0;
        int right = str.size()-1;

        while(left<right){
            if(str[left] != str[right])
                return false;
            left++;
            right--;
        }
        return true;
    }
    void solve(string str){
        if(isPalindrome(str))
            count++;
    }
    int countSubstrings(string s) {
        int n = s.size();
        int j = 1;
        for(int i{0};i<n;i++){
            for(int j{i};j<n;j++){
                solve(s.substr(i,j-i+1));
            }
        }
        return count;  
    }
};
