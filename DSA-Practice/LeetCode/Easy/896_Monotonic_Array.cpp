/*
 * Problem   : 896. Monotonic Array
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/monotonic-array/
 * Date      : 2026-10-08
 * Difficulty: Easy
 * Topics    : Array
 *
 * Approach:
 *   Single pass over the array. Keep a direction flag `d`:
 *     0  -> no direction seen yet (all equal so far)
 *     1  -> increasing
 *    -1  -> decreasing
 *   Skip equal neighbours. On the first unequal pair, set the direction.
 *   If a later pair moves in the opposite direction, the array is not
 *   monotonic, so return false. Otherwise return true.
 *
 * Complexity:
 *   Time : O(n)  - one pass
 *   Space: O(1)  - a single integer flag
 */


// ------------------------------------------------ Solution --------------------------------------------------


class Solution {
public:
    bool isMonotonic(vector<int>& a) { 
        int n = a.size(); 
        if(n<2) return 1; 
        int d = 0 ; 
        for(int i = 1 ; i < n ; i++){ 
            if(a[i] == a[i-1]) continue; 
            if(a[i] > a[i-1]){ 
                if(!d || d==1) d = 1; 
                else return 0; 
            }else{ 
                if(!d || d==-1) d = -1; 
                else return 0; 
            } 
        } 
        return 1;    
    }
};
