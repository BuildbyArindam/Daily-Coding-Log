/*
 * Problem    : 1630. Arithmetic Subarrays
 * Platform   : LeetCode
 * Link       : https://leetcode.com/problems/arithmetic-subarrays/
 * Difficulty : Medium
 * Topics     : Array, Hash Table, Sorting
 * Date       : 2026-10-04
 *
 * Approach:
 *   For each query [l[i], r[i]], copy that subarray into a temp vector and
 *   sort it. A set of numbers can be rearranged into an arithmetic sequence
 *   exactly when its sorted form has a constant difference between
 *   neighbours. Compare every adjacent difference to the first one and
 *   record true/false per query.
 *
 * Complexity (n = nums.size(), m = number of queries):
 *   Time  : O(m * n log n) worst case, since each query sorts up to n elements
 *   Space : O(n) for the temp copy, excluding the O(m) output
 */


// ---------------------------------------------- Solution ----------------------------------------------------------


class Solution {
public:
    bool isvalid(int start,int end,vector<int>nums){
        vector<int>temp;
        for(int i=start;i<=end;i++){
            temp.push_back(nums[i]);
        }
        sort(temp.begin(),temp.end());
        int Size=temp.size();
        int curr=temp[1]-temp[0];
        for(int i=1;i<Size-1;i++){
             if(curr!=(temp[i+1]-temp[i])) return false;
        }
        return true;

    }
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        int lSize=l.size();
       int rSize=r.size();
       int i=0; // l
       int j=0; // r
       vector<bool>ans;
       while(i<lSize && j<rSize){
          ans.push_back(isvalid(l[i],r[j],nums));
          i++;
          j++;
       }
        return ans;
    }
};
