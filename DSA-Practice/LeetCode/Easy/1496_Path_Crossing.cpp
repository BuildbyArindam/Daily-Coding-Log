/*
 * Problem   : 1496. Path Crossing
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/path-crossing/
 * Difficulty: Easy
 * Topics    : Hash Table, String
 * Date      : 2026-10-03
 *
 * Approach:
 *   Simulate the walk from the origin (0, 0), tracking the current (i, j)
 *   position. Every visited coordinate is stored in a set. If a move lands
 *   on a coordinate that is already in the set, the path has crossed itself,
 *   so return true. If the walk ends without a repeat, return false.
 *   (insert() reports whether the element was new, so the check and the
 *   insertion happen in a single call.)
 *
 * Complexity:
 *   Time  : O(n log n) with std::set (O(n) average with an unordered_set
 *           and a custom hash or encoded key)
 *   Space : O(n) for the visited coordinates
 */


// ------------------------------ Solution ----------------------------------------------


class Solution {
public:
    bool isPathCrossing(string path) {
        set<vector<int>> visited;
        pair<set<vector<int>>::iterator, bool> res;
        int i = 0, j = 0;
        visited.insert({0, 0});
        for(char c : path){
            switch(c){
                case 'N':
                    res = visited.insert({--i, j});
                    if(!res.second) return true;
                    break;
                case 'S':
                    res = visited.insert({++i, j});
                    if(!res.second) return true;
                    break;
                case 'W':
                    res = visited.insert({i, --j});
                    if(!res.second) return true;
                    break;
                     case 'E':
                    res = visited.insert({i, ++j});
                    if(!res.second) return true;
                    break;
            }
        }
        return false;
    }
};
