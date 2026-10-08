/*
 * Problem   : 456. 132 Pattern
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/132-pattern/
 * Difficulty: Medium
 * Topics    : Array, Binary Search, Stack, Monotonic Stack, Ordered Set
 * Date      : 2026-10-08
 *
 * Approach:
 *   Keep a stack of candidate (low, high) intervals, one per "1-3" pair seen so far.
 *   For each nums[i]:
 *     - If it falls strictly inside an interval (low < nums[i] < high), a 132
 *       pattern exists, so return true.
 *     - Otherwise, binary search the stack (lows are non-increasing) to check
 *       the other intervals.
 *     - Then update the top interval (lower the low, or raise the high), or
 *       push a new interval when nums[i] is below the current low.
 *
 * Time Complexity : O(n log n), one binary search per element
 * Space Complexity: O(n), for the interval stack in the worst case
 */


// -------------------------------------------- Solution -------------------------------------------------


class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size(),m=0;
        vector<vector<int>> v(2);
        v[0].push_back(INT_MAX);
        v[1].push_back(INT_MIN);
        for(int i=0;i<n;i++){
            if((nums[i]>v[0][0] && nums[i]<v[1][0]) || (nums[i]<v[1][m] && nums[i]>v[0][m])) return true;
            int s=0,l=m;
            while(l!=s+1 && s!=l){
                int mid = (l+s)/2;
                if(nums[i]>v[0][mid] && nums[i]<v[1][mid]) return true;
                if(nums[i]<=v[0][mid]) s = mid;
                else l = mid;
            }
            if(v[1][m] == INT_MIN && v[0][m]>nums[i]) v[0][m] = nums[i];
            else if(v[1][m]<=nums[i]) v[1][m] = nums[i];
            else{
                v[0].push_back(nums[i]);
                v[1].push_back(INT_MIN);m++;
            }
        }
        return false;
    }
};
