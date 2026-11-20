/*
 * Problem   : 1436. Destination City
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/destination-city/
 * Difficulty: Easy
 * Topics    : Array, Hash Table, String
 * Date      : 2026-10-03
 *
 * Approach:
 *   The destination city is the only city that never appears as a
 *   starting point. Store every path's source city in a hash set, then
 *   return the first path's destination that is not in the set.
 *
 * Time Complexity : O(n), two passes over n paths with O(1) average
 *                   hash operations (string length treated as constant)
 * Space Complexity: O(n), for the set of source cities
 */


// ----------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> cities;
        for (const auto& path : paths) {
            cities.insert(path[0]);
        }
        for (const auto& path : paths) {
            const std::string& dest = path[1];
            if (cities.find(dest) == cities.end()) {
                return dest;
            }
        }
        return "";
    }
};
