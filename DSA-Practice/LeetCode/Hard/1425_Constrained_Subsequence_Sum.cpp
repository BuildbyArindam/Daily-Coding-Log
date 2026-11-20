/*
 * Problem   : 1425. Constrained Subsequence Sum 
 * Link      : https://leetcode.com/problems/constrained-subsequence-sum/
 * Date      : 2026-10-07
 * Difficulty: Hard
 * Topics    : Array, DP, Heap (Priority Queue), Sliding Window, Monotonic Queue
 *
 * Approach:
 *   dp[i] = max sum of a valid subsequence ending at index i.
 *   dp[i] = nums[i] + max(0, max(dp[j])) for j in [i-k, i-1].
 *   A max-heap of {dp[j], j} gives the best candidate in the window.
 *   Stale entries (index < i-k) are removed lazily from the top.
 *   The answer is the max over all dp[i].
 *
 * Complexity:
 *   Time  : O(n log n)  (each index is pushed and popped at most once)
 *   Space : O(n)        (dp array + heap)
 *
 * Note: A monotonic deque brings this down to O(n) time.
 */


// ----------------------------------------- Solution ---------------------------------------------------


class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        int n = nums.size(); priority_queue<pair<int, int>>pq; //max heap to maintain the elements of dp vector in descending order 
        pq.push({nums[0], 0}); // as we can not have empty subsequence 
        vector<int>dp(n, 0); // dp vector for storing maximum sum that can be achieved till ith element 
        dp[0] = nums[0]; int ans = nums[0]; for(int i = 1;i<n;i++) { while(!pq.empty()) // find maximum element from dp vector in the range [i-k, i-1] 
        { auto p = pq.top(); if(i-p.second>k) pq.pop(); else break; } // check if the current element must be first element of subsequence or not 
        dp[i] = max(nums[i], nums[i]+pq.top().first); ans = max(ans, dp[i]); pq.push({dp[i], i}); } 
        return ans;
    }
};
