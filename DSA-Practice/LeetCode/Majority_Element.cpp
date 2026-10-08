/*
 * Problem   : 169. Majority Element
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/majority-element/
 * Difficulty: Easy
 * Date      : 2026-10-08
 *
 * Approach  : Boyer-Moore Majority Vote Algorithm
 *   Keep a candidate and a counter. If the counter is 0, adopt the current
 *   number as the candidate. Matching numbers increment the counter and
 *   different numbers decrement it. Since the majority element appears more
 *   than n/2 times, it outlasts all other elements and is the final candidate.
 *   (Relies on the problem's guarantee that a majority element exists.)
 *
 * Time      : O(n), single pass
 * Space     : O(1)
 */


// ------------------------------------------ Solution --------------------------------------------


class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;    
        int element = 0; 

        for (int i = 0; i < nums.size(); i++) {
            if (count == 0) {
                element = nums[i];
                count = 1;
            } else if (element == nums[i]) {
                count++;
            } else {
                count--;
            }
        }

        return element; 
    }
};
