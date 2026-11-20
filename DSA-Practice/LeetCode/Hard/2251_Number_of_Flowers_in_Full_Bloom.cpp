/*
 * Problem   : 2251. Number of Flowers in Full Bloom
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/number-of-flowers-in-full-bloom/
 * Date      : 2026-10-07
 * Difficulty: Hard
 * Topics    : Array, Hash Table, Binary Search, Sorting, Prefix Sum, Ordered Set
 *
 * Approach:
 *   A flower is in bloom at time t if start <= t <= end.
 *   Count of blooming flowers at t =
 *       (# flowers with start <= t) - (# flowers with end < t)
 *   Every flower that has ended (end < t) must have already started, so the
 *   subtraction is valid. Sort start times and end times separately, then
 *   binary search for each person:
 *       - upper_bound(start, t) -> number of flowers started by t
 *       - lower_bound(end, t)   -> number of flowers that ended before t
 *
 * Time Complexity  : O((n + m) log n)
 *                    n = flowers.size(), m = people.size()
 * Space Complexity : O(n) for the start/end arrays (excluding output)
 */


// ----------------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        vector<int> start, end;
        for(auto it : flowers){
            start.push_back(it[0]);
            end.push_back(it[1]);
        }
        sort(start.begin(), start.end());
        sort(end.begin(), end.end());

        vector<int> ans;
        for(auto it : people){
            int start_bloom = upper_bound(start.begin(), start.end(), it) - start.begin();
            int end_bloom = lower_bound(end.begin(), end.end(), it) - end.begin();
            ans.push_back(start_bloom - end_bloom);
        }
        return ans;
    }
};
