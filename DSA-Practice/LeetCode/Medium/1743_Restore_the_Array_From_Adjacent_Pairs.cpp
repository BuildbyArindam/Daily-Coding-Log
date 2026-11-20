/*
 * Problem    : 1743. Restore the Array From Adjacent Pairs
 * Platform   : LeetCode
 * Link       : https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
 * Difficulty : Medium
 * Topics     : Array, Hash Table, Depth-First Search
 * Date       : 2026-10-04
 *
 * Approach:
 *   Map each value to the indices of the pairs that contain it. The two
 *   endpoints of the original array appear in exactly one pair, so a value
 *   with a single pair is the start. From there, walk the chain: push the
 *   other element of the current pair, then jump to the other pair that
 *   contains it. Repeat until n + 1 elements are placed.
 *
 * Time Complexity  : O(n), one pass to build the map, one pass to walk the chain
 * Space Complexity : O(n), the map plus the answer array
 */


// -------------------------------------------- Solution -------------------------------------------------------------


class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& nums) {
        vector<int> ans;
        unordered_map<int,vector<int>> mp;
        int n=nums.size();
        for(int i=0;i<n;i++)
        {
              mp[nums[i][0]].push_back(i);
              mp[nums[i][1]].push_back(i);
        }

        int j=0;
        while(ans.size()<n+1)
        {
            if(ans.empty())
            {
                for(int i=0;i<n;i++)
                {
                    if(mp[nums[i][0]].size()==1)
                    {
                        ans.push_back(nums[i][0]);
                        j=i;
                        break;
                    }
                    if(mp[nums[i][1]].size()==1)
                    {
                        ans.push_back(nums[i][1]);
                        j=i;
                        break;
                    }
                }
            }
                if(ans.back()!=nums[j][0])
                {
                    ans.push_back(nums[j][0]);
                    for(auto it:mp[nums[j][0]])
                    {
                      if(j!=it)
                      {
                          j=it;
                          break;
                      }   
                    }
                }
                else 
                {
                    ans.push_back(nums[j][1]);
                    for(auto it:mp[nums[j][1]])
                    {
                      if(j!=it)
                      {
                          j=it;
                          break;
                      }   
                    }
                }
        }
        return ans;
    }
};
