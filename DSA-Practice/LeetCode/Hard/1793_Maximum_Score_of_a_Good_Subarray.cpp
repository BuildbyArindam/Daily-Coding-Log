/*
 * Problem   : 1793. Maximum Score of a Good Subarray
 * Link      : https://leetcode.com/problems/maximum-score-of-a-good-subarray/
 * Platform  : LeetCode 
 * Difficulty: Hard
 * Date      : 2026-10-07
 *
 * Approach: Greedy two pointers, expanding outward from index k.
 *   - Start with the window [k, k]. A good subarray must contain k.
 *   - At each step, extend toward the neighbor with the larger value
 *     (nums[i-1] vs nums[j+1]) so the running minimum drops as slowly
 *     as possible.
 *   - Track the running min and update the best score min * width
 *     after every expansion, including the initial window.
 *
 * Time    : O(n)
 * Space   : O(1)
 */


// ----------------------------------------- Solution ------------------------------------------------------


class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int n=nums.size();
        if (n == 1) return nums[0];
        int minN=nums[k], i=k, j=k, ans=INT_MIN;
        while (i>0 || j<n-1){
            if (i==0) j++;
            else if (j==n-1) i--;
            else if (nums[i-1]<nums[j+1]) j++;
            else i--;
            minN=min({minN, nums[i], nums[j]});
            ans=max(ans, minN*(j-i+1));
        }
        return ans;
    }
};
