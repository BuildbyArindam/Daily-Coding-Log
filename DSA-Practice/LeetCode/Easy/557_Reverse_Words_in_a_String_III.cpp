/*
 * Problem   : 557. Reverse Words in a String III
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/reverse-words-in-a-string-iii/
 * Difficulty: Easy
 * Topics    : Two Pointers, String
 * Date      : 2026-10-05
 *
 * Approach:
 *   Scan the string once. Each time a space is found (or the last character
 *   is reached), a word has ended, so reverse that word in place using two
 *   pointers (left/right) moving toward each other. Then set the start of
 *   the next word to i + 1.
 *
 * Time Complexity : O(n)  - every character is visited once by the scan and
 *                           at most once more by a reversal.
 * Space Complexity: O(1)  - in-place reversal (the input copy is the output).
 */


// ------------------------------------------- Solution ---------------------------------------------------


class Solution {
public:
    void swap_str(string& s, int start, int end){
        int left = start, right = end;
        while(left<=right){
            char temp = s[left];
            s[left++] = s[right];
            s[right--] = temp;
        }
    }
    string reverseWords(string s) {
        if(s.size()==1)
            return s;
        int start=0,end=0;
        
        for(int i=0;i<s.size();i++){
            if(s[i] == ' '){//stop
                swap_str(s,start,i-1);
                start = i+1;
            }else if(i == s.size()-1){
                swap_str(s,start,i);
            }
        }
        
        return s;
    }
};
