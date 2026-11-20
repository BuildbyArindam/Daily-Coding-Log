/*
 * Problem:    905. Sort Array By Parity
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/sort-array-by-parity/
 * Difficulty: Easy
 * Topics:     Array, Two Pointers, Sorting
 * Date:       2026-10-07
 *
 * Approach:
 *   Allocate a result array of the same size. Walk through the input once:
 *   even numbers are written from the front (startIndex moving right),
 *   odd numbers are written from the back (endIndex moving left).
 *   The two write pointers never collide, so every slot is filled exactly once.
 *
 * Time Complexity:  O(n)  - single pass over the array
 * Space Complexity: O(n)  - separate result array (O(1) extra possible with in-place two pointers)
 */


// ---------------------------------------- Solution -----------------------------------------------------


class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> res(A.size());
        int startIndex = 0;
        int endIndex = A.size() - 1;
        
        for (int i = 0; i < A.size(); ++i) {
            if (A[i] % 2 == 0) {
                res[startIndex++] = A[i];
            }
            else {
                res[endIndex--] = A[i];
            }
        }
        
        return res; 
    }
};
