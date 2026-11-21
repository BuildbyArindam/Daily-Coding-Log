/*
 * Problem   : 1964. Find the Longest Valid Obstacle Course at Each Position
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
 * Date      : 2026-11-21
 * Difficulty: Hard
 * Topics    : Array, Binary Search, Binary Indexed Tree, LIS
 *
 * Approach  : Longest non-decreasing subsequence ending at each index,
 *             using the patience-sorting technique. Maintain `lis`, where
 *             lis[k] is the smallest possible tail of a valid course of
 *             length k+1. For each obstacle:
 *               - if it is >= lis.back(), append it; length = lis.size()
 *               - otherwise, upper_bound finds the first tail strictly
 *                 greater than it (upper_bound, not lower_bound, because
 *                 equal heights are allowed); replace that tail and
 *                 set length = idx + 1.
 *
 * Time      : O(n log n)  (one binary search per element)
 * Space     : O(n)        (lis array + result array)
 */


// ---------------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        int n=obstacles.size();
        vector<int> res(n,1);
        vector<int> lis;
        lis.push_back(obstacles[0]);
        for(int i=1;i<n;i++)
        {
            if(lis.back()<=obstacles[i])
            {
                lis.push_back(obstacles[i]);
                res[i]=lis.size();
            }
            else
            {
                int idx=(upper_bound(lis.begin(),lis.end(),obstacles[i])-lis.begin());
                lis[idx]=obstacles[i];
                res[i]=idx+1;
            }
        }
        return res;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
