/*
 * Problem   : 229. Majority Element II
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/majority-element-ii/
 * Difficulty: Medium
 * Topics    : Array, Hash Table, Sorting, Counting, Boyer-Moore Voting
 * Date      : 2026-10-07
 *
 * Approach  : Sorting + run counting.
 *   Sort the array so equal values are adjacent, then count the length of
 *   each run. Any value whose run exceeds floor(n/3) goes into the answer
 *   (at most 2 such values can exist). n < 3 is handled up front, since a
 *   run of length 1 already exceeds floor(n/3) = 0 there.
 *
 * Time      : O(n log n)  (sorting dominates; the scan is O(n))
 * Space     : O(1) extra  (ignoring sort's internal stack; ans holds <= 2 items)
 *
 * Follow-up : Boyer-Moore voting with two candidates solves it in O(n) time, O(1) space.
 */


// ------------------------------------------------- Solution -----------------------------------------------


class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
      if(n==1){
        return nums;
          }
      else  if(n==2 && nums[0] != nums[1]){
            return nums;
        }
        vector<int> ans;
        int cnt = 0;
        int temp = n/3;
        for(int i=0;i<n;i++){
            
            if( i>0 && nums[i] == nums[i-1]){
               cnt++;
                if(cnt > temp && find(ans.begin(), ans.end(), nums[i]) == ans.end()){
                    ans.push_back(nums[i]);
                   
                }
            }
            else{
                cnt = 1;
            }
        }
        return ans;
    }
};
