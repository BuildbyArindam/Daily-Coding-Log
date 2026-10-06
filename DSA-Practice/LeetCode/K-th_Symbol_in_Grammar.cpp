/*
 * Problem   : 779. K-th Symbol in Grammar
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/k-th-symbol-in-grammar/
 * Difficulty: Medium
 * Topics    : Math, Bit Manipulation, Recursion
 * Date      : 2026-10-07
 *
 * Approach:
 *   Row n is built from row n-1 by turning 0 -> 01 and 1 -> 10, so row n has
 *   2^(n-1) symbols. The first half of row n is identical to row n-1, and the
 *   second half is its complement. Let mid = 2^(n-1) / 2.
 *     - If k <= mid: the answer is kthGrammar(n-1, k).
 *     - Otherwise:   the answer is the flip of kthGrammar(n-1, k-mid).
 *   The base case is n == 1, where the only symbol is 0.
 *
 * Time Complexity : O(n), one recursive call per row.
 * Space Complexity: O(n), recursion stack depth.
 */


// ---------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    int kthGrammar(int n, int k) {
        if(n==1 && k==1){
            return 0;
        }
        
        int mid = pow(2, n-1)/2;
        
        if(k<=mid){
            return kthGrammar(n-1, k);
        }
        else{
            return !(kthGrammar(n-1, k-mid));
        }
    }
};
