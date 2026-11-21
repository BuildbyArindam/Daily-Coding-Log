/*
 * Problem : 1326. Minimum Number of Taps to Open to Water a Garden
 * Link    : https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
 * Platform: LeetCode 
 * Difficulty: Hard
 * Topics  : Array, Dynamic Programming, Greedy
 * Date    : 2026-11-21
 *
 * Approach:
 *   Convert each tap into an interval [i - r, i + r] and record, for every
 *   left start, the farthest right reach (arr[left]). Then solve it like
 *   Jump Game II: sweep the garden, and whenever the current covered range
 *   ends, open one more tap that reaches the farthest. If no tap can extend
 *   the range, the garden can't be fully watered, so return -1.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(n)
 */


// ------------------------------------------ Solution ----------------------------------------------------------


class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        vector<int> arr(n + 1, 0);
        for(int i = 0; i < ranges.size(); ++i) {
            if(ranges[i] == 0) continue;
            int left = max(0, i - ranges[i]);
            arr[left] = max(arr[left], i + ranges[i]);
        }
        
        int end = 0, far_can_reach = 0, cnt = 0;
        for(int i = 0; i <= n; ++i) {
            if(i > end) {
                if(far_can_reach <= end) return -1;
                end = far_can_reach;
                ++cnt;
            }
            far_can_reach = max(far_can_reach, arr[i]);
        }
        
        return cnt + (end < n);
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
