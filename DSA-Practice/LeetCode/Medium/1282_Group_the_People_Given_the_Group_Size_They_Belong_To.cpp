/*
 * Problem   : 1282. Group the People Given the Group Size They Belong To
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
 * Difficulty: Medium
 * Topics    : Array, Hash Table, Greedy
 * Date      : 2026-10-07
 *
 * Approach:
 *   Keep a hash map from group size -> the group currently being filled.
 *   Walk through the people in order and append each index to the bucket
 *   for its required size. As soon as a bucket reaches its target size,
 *   move it into the result and clear the bucket so it can start a new
 *   group of that size. Every person is placed exactly once, and the
 *   problem guarantees at least one valid answer.
 *
 * Time Complexity : O(n), each person is pushed once and each group is
 *                   copied into the result once (n elements total).
 * Space Complexity: O(n), for the map buckets and the result.
 */


// ---------------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        unordered_map<int, vector<int>> temp_group;
        vector<vector<int>> result;
        
        for(int i = 0; i < groupSizes.size(); ++i) {
            int size = groupSizes[i];
            temp_group[size].push_back(i);
            
            if(temp_group[size].size() == size) {
                result.push_back(temp_group[size]);
                temp_group[size].clear();
            }
        }
        return result;
    }
};
